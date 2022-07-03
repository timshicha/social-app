<?php

require __DIR__ . "/../tools.php";

$username = str_to_ascii($_POST["username"]);
$password = str_to_ascii($_POST["password"]);

$result = shell_exec("python ../data/user.py login_user {$username} {$password}");

$code = intval($result);

if($code == 25)
    echo "Successfully logged in";
else if($code == -1)
    echo "Invalid username";
else if($code == -2)
    echo "Invalid password";
    
?>