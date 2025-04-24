# 📄 Resume Parser using NLP & Flask

A clean and user-friendly web application that parses resumes in PDF or DOCX format, extracts key information using NLP techniques, and displays it neatly on the frontend.

🔗 **Live Soon** | 📦 **Repo:** [Resume-Parser-NLP-Flask-](https://github.com/DAKSHSHARMA2901/Resume-Parser-NLP-Flask-)

## ✨ Features

- Upload resume files (`.pdf`, `.docx`)
- Automatically extracts:
  - Full Name
  - Email Address
  - Phone Number
  - Key Skills
  - Full Resume Text
- Clean frontend (HTML + CSS + Animate.css)
- Backend built with Flask
- Uses pdfplumber & docx2txt for text extraction
- Simple error handling & loading UI

## 🚀 Tech Stack

- **Frontend**: HTML, CSS, Animate.css
- **Backend**: Python Flask
- **NLP Tools**: `re`, `pdfplumber`, `docx2txt`

## 📦 Installation

```bash
git clone https://github.com/DAKSHSHARMA2901/Resume-Parser-NLP-Flask-.git
cd Resume-Parser-NLP-Flask-
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
