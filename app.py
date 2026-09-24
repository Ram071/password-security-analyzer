from flask import Flask, render_template, request
import re

app = Flask(__name__)

COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "welcome",
    "welcome123",
    "letmein",
    "abc123",
    "iloveyou",
    "monkey",
    "dragon",
    "football"
}


def analyze_password(password):
    score = 0
    checks = []
    suggestions = []

    length = len(password)
    lower_password = password.lower()

    # Length
    if length >= 16:
        score += 30
        checks.append({
            "name": "Length",
            "status": "good",
            "message": "Excellent length"
        })
    elif length >= 12:
        score += 25
        checks.append({
            "name": "Length",
            "status": "good",
            "message": "Good length"
        })
    elif length >= 8:
        score += 15
        checks.append({
            "name": "Length",
            "status": "warning",
            "message": "Acceptable length"
        })
        suggestions.append("Use at least 12 characters.")
    else:
        checks.append({
            "name": "Length",
            "status": "bad",
            "message": "Too short"
        })
        suggestions.append("Use at least 12 characters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 10
        checks.append({
            "name": "Lowercase",
            "status": "good",
            "message": "Lowercase letter detected"
        })
    else:
        checks.append({
            "name": "Lowercase",
            "status": "bad",
            "message": "No lowercase letter"
        })
        suggestions.append("Add lowercase letters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 10
        checks.append({
            "name": "Uppercase",
            "status": "good",
            "message": "Uppercase letter detected"
        })
    else:
        checks.append({
            "name": "Uppercase",
            "status": "bad",
            "message": "No uppercase letter"
        })
        suggestions.append("Add uppercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 10
        checks.append({
            "name": "Numbers",
            "status": "good",
            "message": "Number detected"
        })
    else:
        checks.append({
            "name": "Numbers",
            "status": "bad",
            "message": "No number"
        })
        suggestions.append("Add numbers.")

    # Special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
        checks.append({
            "name": "Special Character",
            "status": "good",
            "message": "Special character detected"
        })
    else:
        checks.append({
            "name": "Special Character",
            "status": "bad",
            "message": "No special character"
        })
        suggestions.append(
            "Add special characters such as !, @, # or $."
        )

    # Common password
    if lower_password in COMMON_PASSWORDS:
        score -= 40
        checks.append({
            "name": "Common Password",
            "status": "bad",
            "message": "Common password detected"
        })
        suggestions.append("Avoid commonly used passwords.")
    else:
        checks.append({
            "name": "Common Password",
            "status": "good",
            "message": "Not in the basic common-password list"
        })

    # Repeated characters
    if re.search(r"(.)\1\1", password):
        score -= 10
        checks.append({
            "name": "Repeated Characters",
            "status": "warning",
            "message": "Repeated characters detected"
        })
        suggestions.append(
            "Avoid repeating the same character multiple times."
        )
    else:
        checks.append({
            "name": "Repeated Characters",
            "status": "good",
            "message": "No obvious repeated sequence"
        })

    # Sequential patterns
    sequential_patterns = [
        "1234",
        "2345",
        "3456",
        "4567",
        "5678",
        "6789",
        "abcd",
        "bcde",
        "cdef",
        "qwer",
        "asdf"
    ]

    found_sequence = False

    for pattern in sequential_patterns:
        if pattern in lower_password:
            found_sequence = True
            break

    if found_sequence:
        score -= 10
        checks.append({
            "name": "Sequential Pattern",
            "status": "warning",
            "message": "Sequential pattern detected"
        })
        suggestions.append(
            "Avoid predictable sequences such as 1234 or abcd."
        )
    else:
        checks.append({
            "name": "Sequential Pattern",
            "status": "good",
            "message": "No obvious sequential pattern"
        })

    # Predictable words
    predictable_words = [
        "password",
        "qwerty",
        "admin",
        "welcome"
    ]

    if any(word in lower_password for word in predictable_words):
        score -= 15
        suggestions.append(
            "Avoid predictable words such as password, admin, or welcome."
        )

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    # Strength classification
    if score >= 80:
        strength = "Strong"
    elif score >= 50:
        strength = "Medium"
    else:
        strength = "Weak"

    # Default suggestion
    if not suggestions:
        suggestions.append(
            "Good password characteristics detected. "
            "Use a unique password for each account."
        )

    return {
        "score": score,
        "strength": strength,
        "checks": checks,
        "suggestions": suggestions,
        "length": length
    }


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        password = request.form.get("password", "")
        result = analyze_password(password)

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
