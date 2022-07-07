<?php

// Converts a string to ascii values seperated with dashes
// Example: "string" -> "115-116-114-105-110-103"
function str_to_ascii($str)
{
    $ascii_str = "";
    $len = strlen($str);

    for($i = 0; $i < $len; $i++)
    {
        // Convert each character to ascii value
        $to_add = strval(ord($str[$i]));

        // Make sure each ascii value is 3 digits, so this means
        // we need to pad ascii values less than three digits with
        // zeros.
        $pad_zeros = 3 - strlen($to_add); // Count the number of zeros to pad

        // Pad the ascii value with zeros
        for($j = 0; $j < $pad_zeros; $j++)
            $to_add = "0" . $to_add;

        // Add the ascii value to the total ascii string
        $ascii_str .= $to_add;

        // Add delimiter
        if($i != $len - 1)
            $ascii_str .= '-';
    }

    return $ascii_str;
}


?>