<?php

// Converts a string to an ascii string. Each character in the
// string is converted into a 3 digit ascii string and combined
// to represent the total string.
//
// Example: "string" -> "115116114105110103"
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
    }

    return $ascii_str;
}

?>