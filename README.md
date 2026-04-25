# 🧠 AI Exam Generator

### *Generate a complete exam paper on any topic — in seconds.*

> You enter your subject and topic. Our AI searches current syllabus content,
> generates structured questions at your chosen difficulty,
> and validates the paper for accuracy — automatically.
> No manual effort. No guesswork. Just your exam, ready to go.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Tavily](https://img.shields.io/badge/Tavily_Search-FF6B35?style=for-the-badge)
![Railway](https://img.shields.io/badge/Deployed_on-Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)

---

## 🔴 The Problem

Creating a good exam paper is harder than it looks.

Teachers and students waste hours on a process that should take minutes:

```
❌  Manually researching syllabus content across textbooks and websites
❌  Writing questions that are actually at the right difficulty level
❌  Verifying that the answer key is correct for every question
❌  Doing all of this from scratch — every single time
```

**AI Exam Generator fixes all of that.**

---

## ✅ What It Does

You enter your topic. The AI does the rest.

```
  You enter          →    AI researches     →    AI generates      →    AI validates
  your details            the syllabus           the exam paper         the quality

  Subject                 Tavily Search          3 MCQs                 Factual check
  Topic                   Live web results       2 Short Answers        Difficulty check
  Difficulty              Current content        Answer Key             Approval status
```

---

## 👥 Who Is This For?

| User | How They Use It |
|------|----------------|
| 👨‍🏫 **Teachers & Professors** | Generate ready-to-use question papers in minutes instead of hours |
| 🎓 **Students** | Create fresh practice papers for self-assessment on any topic |
| 🏫 **Coaching Institutes** | Produce high volumes of topic-specific questions quickly and consistently |

---

## 🤖 How The AI Works — 3 Agents

AI Exam Generator uses a **3-step AI agent pipeline.** Each agent has one job.

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   📝 Your Input                                            │
│   Subject · Topic · Difficulty Level                       │
│                                                            │
└───────────────────────┬────────────────────────────────────┘
                        │
                        ▼
┌────────────────────────────────────────────────────────────┐
│  🔍  AGENT 1 — RESEARCHER                                  │
│                                                            │
│  Searches the web for current syllabus content             │
│  Uses Tavily Search with advanced depth                    │
│  Finds relevant concepts, topics, and academic context     │
└───────────────────────┬────────────────────────────────────┘
                        │
                        ▼
┌────────────────────────────────────────────────────────────┐
│  ✍️  AGENT 2 — EXAM GENERATOR                              │
│                                                            │
│  Uses research context to generate a structured exam       │
│  Produces 3 MCQs with 4 options + correct answer marked    │
│  Produces 2 Short Answer Questions                         │
│  Includes difficulty ratings and a hidden Answer Key       │
└───────────────────────┬────────────────────────────────────┘
                        │
                        ▼
┌────────────────────────────────────────────────────────────┐
│  ⚖️  AGENT 3 — JUDGE (LLM-as-Judge)                        │
│                                                            │
│  The AI checks its own work                                │
│  Scores on: Factual Accuracy · Difficulty Mix · Key Match  │
│  Gives a final Validation Report + Approval Status         │
└────────────────────────────────────────────────────────────┘
                        │
                        ▼
              🎯 Your Exam Paper + Validation Report
```

---

## 📊 Judge Evaluation Rubric

| Criterion | What Is Checked |
|-----------|----------------|
| ✅ **Factual Correctness** | Are all questions and answers factually accurate? |
| 📊 **Difficulty Distribution** | Is there a proper mix of Easy, Medium, Hard questions? |
| 🔑 **Answer Key Accuracy** | Does every answer in the key correctly match its question? |
| 💬 **Clarity** | Are questions clearly worded and unambiguous? |

---

## 📁 Project Structure

```
ai-exam-generator/
│
├── 🐍  app.py              →  Main Streamlit app, UI & agent pipeline
├── 🤖  exam_generator.py   →  Core agent logic (research, generate, judge)
│
├── 📦  requirements.txt    →  Python dependencies
│
├── 🔒  .env                →  Your API keys (never share this)
├── 📄  .env.example        →  Template — shows what keys are needed
└── 🚫  .gitignore          →  Keeps .env out of GitHub
```

---

## 🚀 Run It Locally

**Step 1 — Clone the repo**
```bash
git clone https://github.com/yourusername/ai-exam-generator.git
cd ai-exam-generator
```

**Step 2 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3 — Add your API keys**

Create a `.env` file in the root folder:
```
GEMINI_KEY=your_key_here
TAVILY_KEY=your_key_here
```

| Key | Where to get it | Cost |
|-----|----------------|------|
| `GEMINI_KEY` | [aistudio.google.com](https://aistudio.google.com) | Free tier available |
| `TAVILY_KEY` | [app.tavily.com](https://app.tavily.com) | Free tier available |

**Step 4 — Start the app**
```bash
streamlit run app.py
```

Then open → [http://localhost:8501](http://localhost:8501)

---

## 🚂 Deploy on Railway

**Step 1** — Push your code to GitHub *(make sure `.env` is in `.gitignore`)*

**Step 2** — Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub

**Step 3** — Add your environment variables in the Railway dashboard:
```
Variables tab → Add:
  GEMINI_KEY  =  your_key
  TAVILY_KEY  =  your_key
```

**Step 4** — Railway auto-deploys. Done ✅

---

## 🛠️ Tech Stack

| What | Technology |
|------|-----------|
| **UI** | Streamlit |
| **AI Agents** | Google Gemini 2.5 Flash |
| **Live Search** | Tavily Search API |
| **Deployment** | Railway |
| **Language** | Python 3.10+ |

---

## 🧪 Sample Output

**Input:**
```
Subject:    Computer Science
Topic:      Cloud Computing and AWS
Difficulty: Medium
```

**Output:**
```
✅ 3 MCQs — each with 4 options and correct answer marked
✅ 2 Short Answer Questions
✅ Hidden Answer Key
✅ Judge Validation Report with Approval Status
```

---

## ⚠️ Disclaimer

This tool is an **AI assistant** for educational purposes only.
Always verify generated content before use in official assessments.

---

## 📄 License

MIT License — free to use, modify, and share.

---

<div align="center">

**Built for every teacher who deserves more time, and every student who deserves better practice. 🧠**

*If this helped you, give it a ⭐ on GitHub!*

</div>

link for our ai :-  https://ai-exam-generator-production.up.railway.app/
