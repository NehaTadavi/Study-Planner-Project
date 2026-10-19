
document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    const message = document.getElementById("message");

    if (username.length > 0 && password.length > 0) {
        message.textContent = "Login form submitted successfully!";
        message.style.color = "green";
    } else {
        message.textContent = "Please enter username and password.";
        message.style.color = "red";
    }
});
