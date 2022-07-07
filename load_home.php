<?php

$SUCCESS_CODE = 25;

require __DIR__ . "/validate_user.php";

echo validate_user($_POST["username"], $_POST["token"]);
return;

if(isset($_POST["username"]) == true && isset($_POST["token"]) == true && validate_user($_POST["username"], $_POST["token"]) == $SUCCESS_CODE)
    echo "logged in as " . $_POST["username"];

else
    echo "not logged in";
?>