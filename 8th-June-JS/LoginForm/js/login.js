const API_BASE_URL = "http://localhost:8000";

document
  .getElementById("loginForm")
  .addEventListener("submit", async function (e) {

    e.preventDefault();

    const username =
      document.getElementById("username").value.trim();

    const password =
      document.getElementById("password").value;

    const message =
      document.getElementById("message");

    if (!username || !password) {
        message.innerText =
          "Username and password required";
        return;
    }

    try {

        const response = await fetch(
            `${API_BASE_URL}/api/auth/login`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username,
                    password
                })
            }
        );

        const data = await response.json();

        if (response.ok) {

            /*
             Example expected response:
             {
                "access_token":"xxxxx",
                "token_type":"bearer"
             }
            */

            localStorage.setItem(
                "token",
                data.access_token
            );

            localStorage.setItem(
                "username",
                username
            );

            message.style.color = "green";
            message.innerText =
          `Login successfull!!`;
        } else {

            let errorMessage = "Login failed";

            if (data.detail) {

                if (typeof data.detail === "string") {
                    errorMessage = data.detail;
                }

                if (Array.isArray(data.detail)) {
                    errorMessage =
                      data.detail
                      .map(x => x.msg)
                      .join(", ");
                }
            }

            message.style.color = "red";
            message.innerText =
                `Login failed: ${errorMessage}`;
        }

    } catch (error) {

        message.style.color = "red";
        message.innerText =
          `Login failed: ${error.message}`;

    }

});