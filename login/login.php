<?php

$SUCCESS_CODE = 25;

require __DIR__ . "/../tools.php";

$username = str_to_ascii($_POST["username"]);
$password = str_to_ascii($_POST["password"]);

$result = intval(shell_exec("python ../data/user.py login_user {$username} {$password}"));

$return_data = array($result, "");

// If logging in ran successfully, start a session for the user and send them the session token
if($result == $SUCCESS_CODE)
{
    session_start();
    $_SESSION["username"] = $_POST["username"]; // Store username in session
    $return_data[1] = session_id(); // Return the session ID back to JS
}

echo json_encode($return_data)
    
?>