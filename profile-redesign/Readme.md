<p align="center">
  <img src="images/hero.svg" width="100%" alt="Pavan Kumar — AI Engineer. I build AI agents, real-time voice AI and automation that runs real operations."/>
</p>

<p align="center">
  <a href="https://portfolio-u-pavankumar.web.app"><img src="images/buttons/portfolio.svg" height="44" alt="Portfolio"/></a>&nbsp;
  <a href="https://linkedin.com/in/u-pavankumar"><img src="images/buttons/linkedin.svg" height="44" alt="LinkedIn"/></a>&nbsp;
  <a href="mailto:pavan.aidev@gmail.com"><img src="images/buttons/email.svg" height="44" alt="Email pavan.aidev@gmail.com"/></a>
</p>

<p align="center">
  <img src="images/impact.svg" width="100%" alt="2,000+ financial documents processed per month · 100K+ records through Python–SQL pipelines · 6 AI and ML systems built · 4 LLM fallback layers per answer"/>
</p>

## ⚡ `whoami --verbose`

```python
class PavanKumar(AIEngineer):
    """I turn manual business queues into AI systems that run on their own."""

    role       = "AI Engineer @ Envision Beyond"
    experience = {
        "Envision Beyond":    "multi-tenant e-Invoicing (2,000+ docs/mo) · Graph API + Odoo CRM automation",
        "Spire Technologies": "Data Analyst Consultant · Python–SQL pipelines, 100K+ records",
    }
    builds     = ["AI agents", "real-time voice AI", "RAG", "enterprise ETL", "LLM failover"]
    education  = "B.E. Computer Science (Data Science) · MVJ College of Engineering · 2020–24"
    certified  = ["Google Data Analytics (Coursera)", "HackerRank: Python", "HackerRank: Problem Solving"]
```

## 🚀 Things I've built

<p align="center">
  <a href="https://github.com/UPavankumar/discord-insights"><img src="images/projects/discord-insights.svg" width="49%" alt="Discord Insights — conversational analytics agent with AST-validated SQL, SSE streaming and 4-tier LLM failover"/></a>
  <a href="https://portfolio-u-pavankumar.web.app"><img src="images/projects/aria.svg" width="49%" alt="Aria — real-time voice AI assistant over WebRTC with interruption handling"/></a>
</p>
<p align="center">
  <a href="https://portfolio-u-pavankumar.web.app"><img src="images/projects/e-invoice.svg" width="49%" alt="e-Invoice Pipeline — multi-tenant ETL filing Malaysian LHDN e-Invoices, 2,000+ documents a month"/></a>
  <a href="https://portfolio-u-pavankumar.web.app"><img src="images/projects/sales-agent.svg" width="49%" alt="AI Sales Agent — email ingestion, company research, personalised drafts and CRM sync"/></a>
</p>
<p align="center">
  <a href="https://github.com/UPavankumar/Portfolio_Assistant"><img src="images/projects/alfred.svg" width="49%" alt="Alfred — AI portfolio assistant grounded in a résumé knowledge base"/></a>
  <a href="https://github.com/UPavankumar/Ecommerce-Churn-ML"><img src="images/projects/churn-ml.svg" width="49%" alt="E-commerce Churn ML — XGBoost churn prediction tuned with grid search"/></a>
</p>

## 🏗️ Under the hood — Discord Insights

An LLM that writes SQL is only useful if it can't hurt the database. Every answer goes through a failover chain of models and a validation layer before anything touches Postgres:

```mermaid
flowchart LR
    Q(["💬 Plain-English question"]) --> O["⚡ FastAPI agent<br/>orchestrator"]
    O <--> LLM
    subgraph LLM ["🧠 LLM failover chain"]
        direction TB
        G["Groq · Llama 3.3 70B"] -->|429 / error| GM["Gemini 2.5 Flash"]
        GM -->|429 / error| OA["GPT-4o-mini"]
        OA -->|429 / error| OFF["Offline rule engine"]
    end
    O --> P["🔌 Auto-discovered plugins<br/>query · chart · summary"]
    P --> V[["🛡️ sqlglot AST guard<br/>SELECT-only · table whitelist"]]
    V -->|safe| DB[("🐘 PostgreSQL<br/>read-only · 500 rows · 5s")]
    V -.->|rejected| X["⛔ blocked"]
    DB --> UI["📡 SSE stream<br/>React + Chart.js"]

    classDef ai fill:#2e1065,stroke:#a78bfa,color:#ede9fe
    classDef guard fill:#052e16,stroke:#3fb950,color:#dcfce7
    classDef io fill:#0c1d33,stroke:#58a6ff,color:#e0f2fe
    classDef bad fill:#3b0a0a,stroke:#f85149,color:#fee2e2
    class G,GM,OA,OFF,O ai
    class V,DB guard
    class Q,P,UI io
    class X bad
    style LLM fill:#0d1117,stroke:#7c3aed,color:#c4b5fd
```

<details>
<summary><b>🎙️ How Aria's voice loop fits together</b></summary>
<br/>

```mermaid
flowchart LR
    U(["🗣️ User speaks"]) -->|WebRTC audio| PC["Pipecat pipeline"]
    PC --> STT["Whisper STT<br/>domain-tuned recognition"]
    STT --> LLM["Groq LLaMA"]
    LLM --> OUT["🔊 Spoken reply"]
    OUT -->|WebRTC audio| U
    U -. "talks over the bot" .-> INT["✋ Interruption handling<br/>stop · listen · respond"]
    INT -.-> PC

    classDef ai fill:#2e1065,stroke:#a78bfa,color:#ede9fe
    classDef io fill:#0c1d33,stroke:#58a6ff,color:#e0f2fe
    class PC,STT,LLM ai
    class U,OUT,INT io
```

</details>

## 🧰 Stack

<p align="center">
  <img src="images/stack.svg" width="100%" alt="Tech stack — AI & LLMs: Groq LLaMA, Whisper, Pipecat, Gemini, GPT-4o-mini, RAG, AI agents, prompt engineering. Backend & APIs: Python, FastAPI, Pydantic, REST, OAuth 2.0, SSE, WebRTC, React, Streamlit. Data & ML: PostgreSQL, SQL, MongoDB, sqlglot, XGBoost, scikit-learn, Power BI, Chart.js. Infra & integrations: Docker, AWS, Git, GitHub Actions, Microsoft Graph API, Odoo CRM, Firebase."/>
</p>

## 📈 Activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/UPavankumar/UPavankumar/output/github-snake-dark.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/UPavankumar/UPavankumar/output/github-snake.svg"/>
    <img alt="Contribution graph being eaten by a snake" src="https://raw.githubusercontent.com/UPavankumar/UPavankumar/output/github-snake-dark.svg"/>
  </picture>
</p>

<p align="center">
  <a href="https://git.io/streak-stats"><img src="https://streak-stats.demolab.com?user=UPavankumar&mode=weekly&hide_border=true&border_radius=16&background=0D1117&stroke=30363D&ring=7C3AED&fire=A78BFA&currStreakNum=E6EDF3&sideNums=E6EDF3&currStreakLabel=A78BFA&sideLabels=8B949E&dates=6E7681&card_width=900" alt="GitHub streak"/></a>
</p>

---

<p align="center">
  <i>Building autonomous enterprise AI layers that run operations, eliminate manual queues, and scale under strict governance.</i>
  <br/><br/>
  <img src="https://komarev.com/ghpvc/?username=UPavankumar&style=flat-square&color=7C3AED&label=profile+views" alt="Profile views"/>
</p>
