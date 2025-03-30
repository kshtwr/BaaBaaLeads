# 🐑 BaaBaaLeads – AI-Powered Webscraping LeadGen Tool

BaaBaaLeads is a free, AI-enhanced lead generation tool built with Streamlit and powered by OpenAI. It lets you find high-quality LinkedIn leads, generate email guesses, score leads with AI, and draft personalized outreach messages—ready for download as a CSV.

Live Demo: 

---

## 🚀 Features

- 🔍 Google-powered LinkedIn lead discovery
- 🧠 AI-driven name validation and formatting via OpenAI
- ✉️ Smart email guess generation (name + company domain)
- 📊 Lead scoring using heuristics and GPT validation
- 💬 Auto-generated outreach message drafts with OpenAI
- 🧹 Real-time filtering by lead score
- 📁 Download leads and messages as CSV
- ⚡ Simple Streamlit interface (runs locally or on Streamlit Cloud)

---

## ⚙️ How It Works

1. You enter a **Company** and **Target Role**.
2. The app uses Google Search to find matching LinkedIn profiles.
3. Names are extracted, cleaned, and  verified via the OpenAI API.
4. Email guesses are generated based on name and company domain.
5. The OpenAI API then validates matches and drafts personalized outreach messages.
6. Leads are scored (powered by AI validation) and displayed with filtering options.
7. Export to CSV with all details and drafts ready to send.

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/BaaBaaLeads.git
cd BaaBaaLeads
```

### 2. Create and activate a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Create a `.env` file or set it in your terminal:

```bash
export OPENAI_API_KEY=sk-xxxxxx
```

Or in `.env`:

```
OPENAI_API_KEY=sk-xxxxxx
```

### 5. Run the app

```bash
streamlit run main.py
```

---

## 📁 File Structure

- `main.py`: Streamlit frontend + session state
- `scraper.py`: LinkedIn profile finder via Google Search
- `utils.py`: Name cleaning, GPT validation, email guessing, scoring, and messaging
- `requirements.txt`: All dependencies
- `.env`: Stores your secret API key (not tracked in git)

---

## ✅ Requirements

- Python 3.8+
- [OpenAI API key](https://platform.openai.com/account/api-keys)
- Internet access (for Google + OpenAI)

---

## ⚠️ Notes

- BaaBaaLeads uses Google Search to **find** LinkedIn profiles (not scraping LinkedIn directly).
- AI-based name validation and cross-checking are **optional**, but improve scoring accuracy.
- You are responsible for complying with usage and outreach laws (CAN-SPAM, GDPR, etc.).

---

## 💡 Future Enhancements

- ✅ Role extraction from LinkedIn titles
- 📨 Email validation API integration
- 📊 Analytics dashboard
- 🔌 CRM integrations (HubSpot, Notion, etc.)