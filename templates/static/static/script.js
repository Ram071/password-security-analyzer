const passwordInput = document.getElementById("password");
const togglePassword = document.getElementById("togglePassword");
const strengthBar = document.getElementById("strengthBar");
const liveText = document.getElementById("liveText");


/* Show / Hide Password */

if (togglePassword && passwordInput) {
    togglePassword.addEventListener("click", function () {

        if (passwordInput.type === "password") {
            passwordInput.type = "text";
            togglePassword.textContent = "Hide";
        } else {
            passwordInput.type = "password";
            togglePassword.textContent = "Show";
        }

    });
}


/* Calculate password strength */

function calculateStrength(password) {

    let score = 0;

    if (password.length >= 8) {
        score += 20;
    }

    if (password.length >= 12) {
        score += 20;
    }

    if (password.length >= 16) {
        score += 10;
    }

    if (/[a-z]/.test(password)) {
        score += 10;
    }

    if (/[A-Z]/.test(password)) {
        score += 10;
    }

    if (/[0-9]/.test(password)) {
        score += 10;
    }

    if (/[^A-Za-z0-9]/.test(password)) {
        score += 20;
    }

    return Math.min(score, 100);
}


/* Live strength indicator */

if (passwordInput && strengthBar && liveText) {

    passwordInput.addEventListener("input", function () {

        const password = passwordInput.value;

        if (!password) {

            strengthBar.style.width = "0%";
            strengthBar.style.background = "#94a3b8";

            liveText.textContent =
                "Start typing to check strength";

            return;
        }

        const score = calculateStrength(password);

        strengthBar.style.width = score + "%";

        if (score < 50) {

            strengthBar.style.background = "#ef4444";
            liveText.textContent = "Weak password";

        } else if (score < 80) {

            strengthBar.style.background = "#f59e0b";
            liveText.textContent = "Medium password";

        } else {

            strengthBar.style.background = "#22c55e";
            liveText.textContent = "Strong password";
        }

    });
}
