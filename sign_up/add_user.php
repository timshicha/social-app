<?php

$result = shell_exec("python ../data/user.py add_user " . $_POST["username"] . " " . $_POST["first"] . " " . $_POST["last"] . " -pw:\"". $_POST["password"] . "\"");

$code = intval($result);

if($code == 0)
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

return;

?>