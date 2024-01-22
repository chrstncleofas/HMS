document.addEventListener("DOMContentLoaded", function () {
    var loginSubmitBtn = document.getElementById('loginSubmitBtn');
    loginSubmitBtn.addEventListener('click', function () {
        showAlert('Login Successful. Welcome back!');
    });
});
