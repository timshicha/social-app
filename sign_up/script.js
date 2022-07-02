let firstNameInput = document.getElementById("first_name_input");
let lastNameInput = document.getElementById("last_name_input");

let userNameInput = document.getElementById("username_input");

let passwordInput = document.getElementById("password_input");
let confirmInput = document.getElementById("confirm_input");

function signUp()
{
    if(passwordInput.value != confirmInput.value)
    {
        alert("Passwords don't match");
        return;
    }

    $.ajax
    ({
        type: 'POST',
        url: "add_user.php",
        dataType: 'text',
        data:
        {
            first: firstNameInput.value,
            last: lastNameInput.value,
            username: userNameInput.value,
            password: passwordInput.value
        },
        success: function(response)
        {
            alert(response);
        }
    });
}