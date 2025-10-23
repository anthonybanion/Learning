<?php 
/*brief assing null
 *details three ways to assign null
 *file null.php
 *date 27/03/2024
 *version 1.0*/

//assign a value null to the variable
$var1 = null;
//we aren´t assign value to the variable
$var2;
echo (var_dump($var1));
echo'<br>';
echo(var_dump($var2));
echo'<br>';
$var1 = 10;

//destroy the variable
unset($var1);
echo(var_dump($var1));

echo(is_null($var1));
echo'<br>';
echo(is_null($var2));
?>