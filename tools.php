<?php

// Converts a string to ascii values seperated with dashes
// Example: "string" -> "115-116-114-105-110-103"
function str_to_ascii($str)
{
    $ascii_str = "";
    $len = strlen($str);

    for($i = 0; $i < $len; $i++)
    {
        $ascii_str .= strval(ord($str[$i]));

        if($i != $len - 1)
            $ascii_str .= '-';
    }

    return $ascii_str;
}


?>