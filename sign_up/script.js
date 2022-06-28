function signUp()
{
    let passwordInput = document.getElementById("password_input");
    let confirmInput = document.getElementById("confirm_input");

    if(passwordInput.value != confirmInput.value)
    {
        alert("Passwords don't match");
        return;
    }
}