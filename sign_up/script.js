let firstNameInput = document.getElementById("first_name_input");
let lastNameInput = document.getElementById("last_name_input");

let usernameInput = document.getElementById("username_input");

let passwordInput = document.getElementById("password_input");
let confirmInput = document.getElementById("confirm_input");

function signUp()
{
    // Check if passwords match
    if(passwordInput.value != confirmInput.value)
    {
        alert("Passwords don't match");
        return;
    }

    $.ajax
    ({
        type: 'post',
        url: "add_user.php",
        dataType: 'text',
        data:
        {
            first: firstNameInput.value,
            last: lastNameInput.value,
            username: usernameInput.value,
            password: passwordInput.value
        },
        success: function(response)
        {
            alert(response);
        }
    });
}