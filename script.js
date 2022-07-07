$("#nav_bar").load("nav.html");

//add_post("VadimShicha", "https://i.picsum.photos/id/136/200/300.jpg?hmac=vOFG2QkF3OUbTp5DRbf7w58YCDVrvf_g5aPFxxTucpU");

function add_post(username, image)
{
    let div = document.createElement("div");
    let usernameText = document.createElement("h2");
    let img = document.createElement("img");
    let br = document.createElement("br");
    
    usernameText.innerText = username;
    img.src = image;

    div.appendChild(usernameText);
    div.appendChild(img);

    document.getElementById("posts").appendChild(div);
    document.getElementById("posts").appendChild(br);
}

$.ajax
({
    type: 'post',
    url: "load_home.php",
    dataType: 'text',
    data:
    {
        "username": sessionStorage.getItem("username"),
        "token": sessionStorage.getItem("token")
    },
    success: function(response)
    {
        alert(response);
    }
});