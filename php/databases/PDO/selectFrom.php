<?php
/* @brief This code is used to connect to a database and select data from a table.
 * @details used foreach to print the data from the table.
 * @file select_from.php
 * @date 04/04/2024
 * @version 1.0*/

$serve = "localhost";
$user = "root";
$pass = "5_Argentina";
$db = "php";
try {
    $conn = new PDO("mysql:host=$serve;dbname=$db", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $sql = "SELECT * FROM `person`";
    $result = $conn->prepare($sql);
    $result->execute();
    $result = $result->fetchAll(PDO::FETCH_ASSOC);
    
    foreach ($result as $row) {
        echo $row['id'] . " " . $row['name'] . " " . $row['age'] . "<br>";

    }
    echo "Connected successfully";
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

?>
