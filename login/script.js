let usernameInput = document.getElementById("username_input");
let passwordInput = document.getElementById("password_input");

function login()
{
    $.ajax
    ({
        type: 'post',
        url: "login.php",
        dataType: 'text',
        data:
        {
            username: usernameInput.value,
            password: passwordInput.value
        },
        success: function(response)
        {
            alert(response);

            let result = JSON.parse(response);

            if(parseInt(result[0]) == 25)
            {
                sessionStorage.setItem("username", usernameInput.value);
                sessionStorage.setItem("token", result[1]);
            }
        }
    });
}