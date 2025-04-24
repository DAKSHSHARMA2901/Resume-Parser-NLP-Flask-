# Resume-Parser-NLP-Flask-

A simple web-based Resume Parser that extracts key information from PDF or DOCX resumes using Natural Language Processing and displays it in a clean user interface.

## 🔍 Features
- Upload resumes in PDF or DOCX format.
- Extracts:
  - Name
  - Email
  - Phone Number
  - Skills
  - Full Text
- Beautiful animated frontend (HTML + CSS + Animate.css)
- Backend powered by Flask and NLP libraries like `pdfplumber`, `docx2txt`, and regex.

## 🚀 Tech Stack
- **Frontend:** HTML, CSS, JavaScript, Animate.css
- **Backend:** Flask
- **NLP Libraries:** pdfplumber, docx2txt, re

## 📦 Installation

```bash
git clone https://github.com/dakshsharma2901/resume-parser-nlp.git
cd resume-parser-nlp
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
