from flask import Flask, render_template, request, jsonify
import spacy
import docx2txt
import pdfplumber
import re
import os

app = Flask(__name__)
nlp = spacy.load("en_core_web_md")

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_text(file_path, filename):
    if filename.endswith('.pdf'):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    elif filename.endswith('.docx'):
        return docx2txt.process(file_path)
    else:
        return ""

def extract_email(text):
    email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return email_match.group() if email_match else "Not Found"


def extract_phone(text):
    phone_match = re.search(r"\b\d{10}\b", text)
    return phone_match.group() if phone_match else "Not Found"


def extract_name(text):
    # Get lines from the resume text
    lines = text.strip().split("\n")
    for i, line in enumerate(lines):
        # Heuristic: Name is usually right above or near the email
        if "@" in line:
            # Check previous lines for a name-like string
            for j in range(i - 1, max(i - 3, -1), -1):
                candidate = lines[j].strip()
                if 1 < len(candidate.split()) <= 4 and all(x.isalpha() or x.isspace() for x in candidate):
                    return candidate
    return "Not Found"


def extract_skills(text):
    skills = ["Python", "Java", "SQL", "Machine Learning", "Deep Learning", "Communication", "Leadership"]
    found = [s for s in skills if s.lower() in text.lower()]
    return ", ".join(found) if found else "Not Found"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["resume"]
    filename = file.filename
    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)

    text = extract_text(path, filename)
    results = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "full_text": text
    }
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
