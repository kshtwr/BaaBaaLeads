# 🚀 A Webscraping LeadGen Tool

This is a free and open-source lead generation tool built with Streamlit. You can input a company name and target role, and the tool will use Google Search to identify potential leads from LinkedIn, guess their professional email addresses, score them, and generate an outreach message draft.

---

## 🔧 Features

- Google-powered LinkedIn lead search
- Smart email guess generation based on name and domain
- Lead scoring system based on heuristics (email quality, LinkedIn presence, role relevance, etc.)
- Auto-generated outreach drafts
- CSV download of filtered leads
- Streamlit-powered interactive UI

---

## 🧐 How It Works

1. You enter a company and role.
2. The tool uses Google Search to find relevant LinkedIn profiles.
3. Names are extracted and cleaned, email addresses are guessed.
4. Leads are scored based on relevance and completeness.
5. Email drafts are auto-generated using your pitch.
6. You can filter and download leads directly from the UI.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/leadgen-tool.git
cd leadgen-tool
```

### 2. Create virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run main.py
```

---

## 📄 Files

- `main.py`: Streamlit frontend logic
- `scraper.py`: Lead scraping logic using Google Search
- `utils.py`: Name cleaning, email guessing, title extraction, and lead scoring

---

## ❗Note

This tool uses Google Search to extract LinkedIn profile links. It does not scrape LinkedIn directly, respecting their [Terms of Service](https://www.linkedin.com/legal/user-agreement).

---

## ✨ Future Ideas

- Integrate real-time email verification APIs
- Use LLMs for smarter title parsing
- Export in other formats (e.g., JSON, XLSX)

