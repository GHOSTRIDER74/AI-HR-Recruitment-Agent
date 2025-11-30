# 🤖 AI HR Recruitment Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![Status](https://img.shields.io/badge/Status-Prototype-green)

An intelligent recruitment assistant that automates the resume screening process using Large Language Models (LLMs). Unlike traditional ATS (Applicant Tracking Systems) that rely on simple keyword matching, this agent utilizes **Google Gemini** to semantically understand candidate profiles, compare them against Job Descriptions (JDs), and provide reasoned decision-making.

## 🚀 Key Features

* **📄 PDF Resume Parsing:** Robust text extraction from PDF documents using `pypdf`.
* **🧠 Context-Aware Analysis:** Uses the **Gemini 1.5 Flash** model to evaluate candidates based on skills, experience, and potential fit, providing a match score (0-100%).
* **👮 Human-in-the-Loop (HITL):** A critical verification layer where a human recruiter reviews the AI's decision before finalization, ensuring fairness and accuracy.
* **📧 Automated Communication:** Generates professional, context-specific email drafts (Interview Invitations or Rejections) based on the final decision.
* **⚡ Portable Design:** Built with relative paths to run seamlessly on any local machine or cloud environment.

## 🛠️ Tech Stack

* **Language:** Python
* **LLM:** Google Gemini API (`google-generativeai`)
* **PDF Processing:** `pypdf`
* **Environment Management:** `python-dotenv`
* **Data Handling:** `pandas` (optional for future expansion)

## 📂 Project Structure

```text
AI-HR-Recruitment-Agent/
├── data/
│   ├── resumes/            # Folder containing candidate PDF resumes
│   └── job_description.txt # The target role description
├── notebooks/
│   └── demo.ipynb          # Interactive demo of the agentic workflow
├── src/
│   ├── agent.py            # Core logic for the Gemini AI agent
│   ├── pdf_parser.py       # Utility to extract text from PDFs
│   └── utils.py            # Helper functions (Email generation, etc.)
├── .env                    # API Keys (Not uploaded to GitHub)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```


## 🏗️ Architecture

```mermaid
flowchart TD

    subgraph Data_Layer[📂 Data Input]
        RES[📄 PDF Resumes]
        JD[📝 Job Description]
    end

    subgraph Core_Logic[⚙️ Application Logic]
        Parser[Python PDF Parser]
        Agent[Recruitment Agent Class]
        Email[Email Generator]
    end

    subgraph External[☁️ External Services]
        Gemini[✨ Google Gemini API]
    end

    subgraph HITL[👤 Human-in-the-Loop]
        User[Recruiter / User]
    end

    %% Flow Connections
    RES --> Parser
    JD --> Parser
    Parser --> Agent
    Agent <-->|Prompt + Context| Gemini
    Agent --> User
    User --> Decision{Approve Decision?}

    Decision -->|Yes| Email
    Decision -->|Override| Email

    Email --> Final[📧 Final Email Output]

    %% Styling
    style Gemini fill:#f9f,stroke:#333,stroke-width:2px
    style User fill:#ff9,stroke:#333,stroke-width:2px
    style Decision fill:#fff,stroke:#333,stroke-width:2px
