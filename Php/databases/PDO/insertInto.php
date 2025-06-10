<?php
/* @brief This code is used to connect to a database and insert data in a table.
 * @details executing sql statement.
 * @file insert_into.php
 * @date 04/04/2024
 * @version 1.0*/

$serve = "localhost";
$user = "root";
$pass = "5_Argentina";
$db = "php";
try {
    $conn = new PDO("mysql:host=$serve;dbname=$db", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $mysql = "INSERT INTO `php`.`person`(name, age) VALUES ('marcos', 56)";
    $conn->exec($mysql);

    echo "Connected successfully";
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

?>