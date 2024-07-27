<?php
/* @brief connect to a database using PDO
 * @details PDO is a PHP extension that provides a data-access abstraction layer.
 * @file conn_pdo.php
 * @date 03/04/2024
 * @version 1.0*/

$serve = "localhost";
$user = "root";
$pass = "5_Argentina";
$db = "php";
try {
    $conn = new PDO("mysql:host=$serve;dbname=$db", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully";
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

?>