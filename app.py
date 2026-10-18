import os
import requests
import streamlit as st
st.set_page_config(
    page_title="RepoRadar",
    page_icon="🚀",
    layout="wide"
)

API = "https://api.github.com/search"
HEADERS = {"Accept": "application/vnd.github+json"}


@st.cache_data(ttl=300)
def github_search(endpoint, params):
    response = requests.get(
        f"{API}/{endpoint}",
        params=params,
        headers=HEADERS,
        timeout=15
    )
    response.raise_for_status()
    return response.json()


def search_repositories(query, language, sort):
    query = query.strip() or "stars:>100"

    if language != "Any":
        query += f" language:{language.lower()}"

    params = {
        "q": query,
        "sort": sort,
        "order": "desc",
        "per_page": 20
    }
    return github_search("repositories", params).get("items", [])


def find_good_first_issues(language):
    query = "is:issue is:open label:good first issue"

    if language != "Any":
        query += f" language:{language.lower()}"

    params = {
        "q": query,
        "sort": "created",
        "order": "desc",
        "per_page": 15
    }
    return github_search("issues", params).get("items", [])


def interest_score(repo, interests):
    text = (
        repo.get("name", "") + " " +
        (repo.get("description") or "") + " " +
        " ".join(repo.get("topics", [])) + " " +
        (repo.get("language") or "")
    ).lower()

    terms = [word.lower() for word in interests.split(",") if word.strip()]
    return sum(term in text for term in terms)


def ai_recommendations(repos, interests):
    key = os.getenv("OPENAI_API_KEY")

    if not key:
        return None

    try:
        from openai import OpenAI

        client = OpenAI(api_key=key)
        candidates = [
            {
                "name": repo["full_name"],
                "description": repo.get("description") or "",
                "language": repo.get("language"),
                "url": repo["html_url"]
            }
            for repo in repos[:12]
        ]

        result = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Recommend GitHub repositories based only on "
                        "the supplied repository data. Explain briefly "
                        "why each is relevant. Do not invent features."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Developer interests: {interests}\n"
                        f"Repositories: {candidates}\n"
                        "Recommend the best 5."
                    )
                }
            ],
            temperature=0.3
        )
        return result.choices[0].message.content
    except Exception:
        return "AI recommendations are unavailable. Try keyword matching."


st.title("🚀 RepoRadar")
st.caption("Your radar for open-source discovery.")
st.markdown(
    "Discover projects to build with, learn from, and contribute to."
)

with st.sidebar:
    st.header("🔎 Discover")
    mode = st.radio(
        "Explore",
        ["Trending & Search", "Good First Issues"]
    )
    language = st.selectbox(
        "Programming language",
        ["Any", "Python", "Java", "JavaScript",
         "TypeScript", "Go", "Rust", "C++"]
    )
    sort = st.selectbox(
        "Sort repositories by",
        ["stars", "updated", "help-wanted-issues"]
    )
    interests = st.text_input(
        "Your interests",
        placeholder="AI, agents, data science"
    )
    use_ai = st.checkbox("Use AI recommendations (optional)")
    search = st.text_input(
        "Search GitHub",
        placeholder="machine learning, chatbot..."
    )
    explore = st.button("Explore projects", type="primary")

if explore or "results" not in st.session_state:
    try:
        with st.spinner("Searching GitHub..."):
            if mode == "Good First Issues":
                st.session_state.results = find_good_first_issues(
                    language
                )
            else:
                query = search or "stars:>100"
                st.session_state.results = search_repositories(
                    query, language, sort
                )
        st.session_state.last_mode = mode
    except requests.RequestException as error:
        st.error(
            "GitHub could not be reached. Please try again later."
        )
        st.caption(str(error))
        st.session_state.results = []

results = st.session_state.get("results", [])

if interests and results:
    results = sorted(
        results,
        key=lambda item: interest_score(item, interests),
        reverse=True
    )

if use_ai and interests and results:
    with st.expander("🤖 AI recommendations", expanded=True):
        if st.button("Generate recommendations"):
            with st.spinner("Finding your best matches..."):
                recommendation = ai_recommendations(results, interests)
            if recommendation:
                st.markdown(recommendation)
            else:
                st.info(
                    "Add OPENAI_API_KEY to your environment to enable "
                    "AI recommendations. Keyword matching still works."
                )

if not results:
    st.info("No results yet. Try a different search or language.")
else:
    st.subheader(
        "🌱 Beginner-friendly issues"
        if mode == "Good First Issues"
        else "🔥 Repository discoveries"
    )
    st.caption(f"{len(results)} results from GitHub")

    for repo in results:
        is_issue = "html_url" in repo and "repository_url" in repo

        with st.container(border=True):
            if is_issue:
                st.markdown(f"### [{repo['title']}]({repo['html_url']})")
                st.write(repo.get("body") or "No description available.")
                st.caption(
                    f"Repository: {repo.get('repository_url', '').replace('https://api.github.com/repos/', '')}"
                )
            else:
                st.markdown(
                    f"### [{repo['full_name']}]({repo['html_url']})"
                )
                st.write(repo.get("description") or "No description available.")

                left, middle, right = st.columns(3)
                left.metric("⭐ Stars", f"{repo.get('stargazers_count', 0):,}")
                middle.metric("🍴 Forks", f"{repo.get('forks_count', 0):,}")
                right.metric("🐛 Open issues", repo.get("open_issues_count", 0))

                st.caption(
                    f"Language: {repo.get('language') or 'Not specified'}"
                    f" · Updated: {repo.get('updated_at', '')[:10]}"
                )

                score = interest_score(repo, interests) if interests else 0
                if interests:
                    st.caption(f"Interest keyword matches: {score}")

st.divider()
st.caption(
    "RepoRadar uses public GitHub data. Results depend on GitHub's "
    "search index and API limits. AI recommendations require an API key."
)
