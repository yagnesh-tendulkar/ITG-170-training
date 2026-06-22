const API_BASE_URL = "http://localhost:8000";

document
  .getElementById("registerForm")
  .addEventListener("submit", async function (e) {

    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    const message = document.getElementById("message");

    // Validation
    if (!username || !email || !password) {
        message.innerText = "All fields are required";
        return;
    }

    try {

        const response = await fetch(
            `${API_BASE_URL}/api/auth/register`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username,
                    email,
                    password
                })
            }
        );

        const data = await response.json();

        if (response.ok) {
            message.style.color = "green";
            message.innerText = "Registration successful";

            setTimeout(() => {
                window.location.href = "login.html";
            }, 1000);

        } else {

            message.style.color = "red";

            message.innerText =
                data.detail ||
                data.message ||
                "Registration failed";
        }

    } catch (error) {
        message.innerText = error.message;
    }

});