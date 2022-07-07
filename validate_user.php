<?php

$SUCCESS_CODE = 25;
$FAIL_CODE = -1;

// Validate a user based on their token.
//
// Background:
// When a user logs in, they are given a token so that they don't need
// to provide their password each time they want to make an action that
// requires user authentication. This happens in /login/login.php.

function validate_user($username, $token)
{
    // If a session wasn't started
    if(session_id() == "")
    {
        return $FAIL_CODE; // Return fail
    }

    // Make sure the session actually has the username and token keys set
    if(isset("username", $_SESSION) == false || isset("token", $_SESSION) == false)
    {
        return $FAIL_CODE; // Return fail
    }

    // Now make sure the username and token match the session.
    // If they match, return success.
    if($_SESSION["username"] == $username && $_SESSION["token"] == $token)
        return $SUCCESS_CODE;

    // If they don't match, return fail
    return $FAIL_CODE;
}

?>