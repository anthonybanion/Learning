<?php
/* @brief connect to a database using mysqli
 * @details mysqli is a PHP extension that provides an interface to the MySQL database.
 * @file conn_mysqli.php
 * @date 03/04/2024
 * @version 1.0*/
 
$serve = "localhost";
$user = "root";
$pass = "5_Argentina";
$db = "student management";
$conn = new mysqli($serve, $user, $pass, $db);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
$conn->close();

?>