<?php

require __DIR__ . "/../tools.php";

$username = str_to_ascii($_POST["username"]);
$first = str_to_ascii($_POST["first"]);
$last = str_to_ascii($_POST["last"]);
$password = str_to_ascii($_POST["password"]);

$result = shell_exec("python ../data/user.py add_user {$username} {$first} {$last} {$password}");

$code = intval($result);

if($code == 25)
    echo "Successfully created account";
else if($code == -1)
    echo "Username already exists";
else if($code == -2)
    echo "Error connecting to database";
else if($code == -3)
    echo "Invalid username";
else if($code == -4)
    echo "Invalid first or last name";
else if($code == -5)
    echo "Invalid password";
else if($code == 0)
    echo "Some other error";

return;

?>