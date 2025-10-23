<?php
/* @brief basic calculator
 * @details calculator whit post method
 * @file claculator.php
 * @date 30/03/2024
 * @version 1.0*/

if(isset($_POST['submit'])){
        $number1 = $_POST['number1'];
        $number2 = $_POST['number2'];
        echo "La suma es: ".($number1 + $number2)."<br>";
        echo "La resta es ".($number1 - $number2)."<br>";
        echo "La multiplicacion es ".($number1 * $number2)."<br>";
        echo "La division es ".($number1 / $number2)."<br>";
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>POST</title>
</head>
<body>
    <form action="calculator.php" method = "post">
        <input type="text" name="number1" placeholder="Enter the first number">
        <input type="text" name="number2" placeholder="Enter the second number">
        <input type="submit" name="submit" value="Submit">

    </form>
</body>
</html>