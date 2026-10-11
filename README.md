# 🚀 RepoRadar — Discover Your Next Open-Source Project

<p align="center">
  <strong>Your radar for open-source discovery.</strong>
  <br />
  Explore trending repositories, discover beginner-friendly issues, and find projects that match your interests.
  <br /><br />
  <a href="https://repo04radar.streamlit.app/">
    <strong>🌐 Launch Live Demo</strong>
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/API-GitHub_REST-181717?logo=github&logoColor=white" alt="GitHub REST API" />
  <img src="https://img.shields.io/badge/Status-Live-brightgreen" alt="Live" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
</p>

---

## 📌 Overview

Finding the right open-source project can be overwhelming, especially when you're just getting started.

**RepoRadar** makes open-source discovery easier by bringing GitHub repository search, project insights, and beginner-friendly contribution opportunities into one simple dashboard.

Whether you're exploring AI, machine learning, web development, or other technologies, RepoRadar helps you find projects worth exploring.

## ✨ Features

- 🔥 **Repository Discovery** — Explore repositories ranked by stars, recent updates, and help-wanted issues.
- 🔎 **Smart GitHub Search** — Search for projects using keywords and programming languages.
- 🌱 **Good First Issues** — Find open issues labeled for beginners who want to contribute.
- 📊 **Repository Analytics** — View repository counts, star totals, and language distributions.
- 🎯 **Interest-Based Matching** — Prioritize repositories whose names, descriptions, topics, and languages match your interests.
- 🔗 **Direct GitHub Links** — Visit repositories and issues to explore the code or contribute.
- 🎨 **Dark Maroon Interface** — A developer-focused dashboard designed for comfortable browsing.

## 🌐 Live Demo

Try RepoRadar without installing anything:

### 👉 [Open RepoRadar](https://repo04radar.streamlit.app/)

## 🖥️ Preview

The dashboard provides a searchable repository explorer, project statistics, language charts, and a dedicated Good First Issues mode.

_Add a screenshot of your deployed application here to help visitors see RepoRadar before opening the demo._

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and data processing |
| Streamlit | Interactive web interface |
| GitHub REST API | Repository and issue discovery |
| Requests | HTTP requests to the GitHub API |
| CSS | Dashboard styling |

## 🚀 Run Locally

You can run RepoRadar on your own machine in a few steps.

### Prerequisites

- Python 3.10 or later
- Git
- An internet connection

### 1. Clone the repository

```bash
git clone https://github.com/jahnavi04/RepoRadar.git
cd RepoRadar
```

### 2. Create a virtual environment (recommended)

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

Open the local URL printed in your terminal, usually `http://localhost:8501`.

## 📁 Project Structure

```text
RepoRadar/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

## 🔍 How to Use

1. Open the [live application](https://repo04radar.streamlit.app/).
2. Choose **Trending & Search** or **Good First Issues**.
3. Select a programming language or choose `Any`.
4. Enter search keywords and interests.
5. Click **Explore projects**.
6. Browse repository statistics and follow links to GitHub.

**Tip:** Try interests such as `AI, agents, data science` or search for `machine learning`.

## ⚙️ Configuration

RepoRadar uses the public GitHub REST API. No GitHub token is required for the basic experience, but unauthenticated API requests are subject to rate limits.

If you reach a rate limit, wait before retrying.

## 🗺️ Roadmap

Planned improvements include:

- [ ] Personalized recommendations based on skill level and interests
- [ ] Bookmark and save repositories
- [ ] Trending technology and language insights
- [ ] Open-source contribution progress tracking
- [ ] More advanced repository filters
- [ ] Automated testing and continuous integration
- [ ] Improved accessibility and mobile experience

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome!

1. Fork this repository.
2. Create a branch for your change.
3. Make your changes and test them locally.
4. Commit your changes.
5. Open a pull request describing your improvement.

For larger changes, consider opening an issue first to discuss your idea.

## 🐛 Report a Bug or Suggest a Feature

Found a problem or have an idea? Open an issue in the [RepoRadar repository](https://github.com/jahnavi04/RepoRadar/issues).

## 🔒 Privacy and Security

RepoRadar uses GitHub's public API to retrieve repository and issue information. Do not commit API tokens, passwords, or other secrets to the repository.

## 📄 License

This project is intended to be released under the MIT License. See the `LICENSE` file for the exact license terms.

## 👩‍💻 Author

**Jahnavi S T**

- GitHub: [@jahnavi04](https://github.com/jahnavi04)
- LinkedIn: [Jahnavi S T](https://www.linkedin.com/in/jahnavi-s-t/)

---
