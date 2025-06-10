<?php
/* @breif: Session variables are used to store user information 
 * and view on all pages. When you close the browser the 
 * session variables disappear
 * @details: linked whit session_destroy.php
 * @file: session_start.php
 * @date: 05/04/2024
 * version: 1.0*/

session_start();
$_SESSION["user"] = "admin";
$_SESSION["status"] = "active";
$_SESSION["password"] = "admin";

echo "Session begin".":<br>";

if (isset($_SESSION['user'])) {
    echo "Welcome <br>";
    echo "User: ".$_SESSION["user"]."<br>";
    echo "Status: ".$_SESSION["status"]."<br>";
    echo "Password: ".$_SESSION["password"]."<br>";
} else {
    echo "You are not logged in";
}
?>