# Password Security Analyzer

A simple web-based Password Security Analyzer built using Python Flask.

## Features

- Password strength analysis
- Password length checking
- Lowercase letter detection
- Uppercase letter detection
- Number detection
- Special-character detection
- Common-password detection
- Repeated-character detection
- Sequential-pattern detection
- Security score from 0 to 100
- Weak, Medium and Strong classification
- Security suggestions
- Show/Hide password button
- Live password-strength indicator
- Responsive web interface

## Technologies

- Python
- Flask
- HTML
- CSS
- JavaScript

## Privacy

The application does not intentionally store submitted passwords in a
database or file.

The password is analyzed while processing the request.

This project is intended for educational purposes.

## Project Structure

```text
password-security-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
