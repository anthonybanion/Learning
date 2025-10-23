<?php
/* @brief showing the data type of each variable.
 * @details using the functions: var_dump, gettype and is_type. 
 * @file var_dump-gettype-is_type.php.
 * @date 27/03/2024.
 * @version 2.0 */

$var1 = 'Hola';
$var2 = 10;
$var3 = true;
$var4 = 10.5;

echo (var_dump($var1));
echo "<br>";
echo (var_dump($var2));
echo "<br>";
echo (var_dump($var3));
echo "<br>";
echo (var_dump($var4)); 
echo "<br>";

echo(gettype($var1)); 
echo "<br>";
echo(gettype($var2)); 
echo "<br>";
echo(gettype($var3)); 
echo "<br>";
echo(gettype($var4));
echo"<br>";

echo(is_string($var1));
echo "<br>";
echo(is_int($var2));
echo "<br>";
echo(is_bool($var3));
echo "<br>";
echo(is_float($var4));
?>