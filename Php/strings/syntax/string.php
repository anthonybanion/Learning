<?php
/* @brief PHP strings are sequences of characters
 * @details: single quotes; double quotes; Heredoc; Nowdoc .
 * @file string.php
 * @date 29/03/2024
 * @version 1.0*/

 error_reporting(E_ALL);
$string_var = "Hello World!";
$number_var = 25;
class person {
    public $name = "John";
    public $age = 25;
   function next() {
        return "output";
    }
}
$fruit_name = array("apple", "pear", "grape", "tangerine");
$person = new person();

echo '<h3> single quotes </h3>';
echo ' quotes \' and a backslash \\ </br>';
echo 'publish a variable '.$string_var.'</br>';
echo 'publish a number ',$number_var,'</br>';
$total = 10;
$discount = 2;
echo 'publish a difference: $' .($total - $discount).'</br>'; 
echo 'publish an element of a vector: '.$fruit_name[3].'</br>';
echo 'publish an object property: '.$person->name.' and his age is '.$person->age.'</br>';

echo '<h3> in double quotes </h3>';
echo "<h4> simple syntax </h4>";
echo "publish a variable $string_var </br>";
echo "publish a number $number_var </br>";
$total = 10;
$discount = 2;
echo "publish a difference: $ ($total - $discount)</br>"; 
echo "publish an element of a vector: $fruit_name[3]</br>";
echo "publish an object property: $person->name and his age is $person->age</br>";

echo "<h4> complex syntax </h4>";
$out="HOLA";
$in="out";
$output="allready";

function redirecting(){

    return "output";
}

echo "publish an element of a vector: {$fruit_name[3]}</br>";
echo "publish an object property: {$person->name} and his age is {$person->age}</br>";
echo "input and output: {$$in} </br>";
echo "other format: {${$in}}</br>";
echo "function output: {${redirecting()}} </br>";
echo "for object property: {${$person->next()}} </br>";

echo "<h3> access the properties of a class using variables within a string.</h3>";
class foo {
    var $bar = 'Soy bar.';
}

$foo = new foo();
$bar = 'bar';
$baz = array('foo', 'bar', 'baz', 'quux');
echo "{$foo->$bar}</br>";
echo "{$foo->{$baz[1]}}</br>";

// Heredoc
$strHeredoc = <<<EOD
similar to double quotes $string_var </br>
publish an element of a vector: {$fruit_name[3]} </br>

EOD;
echo $strHeredoc;

//Nowdoc
$strNowdoc = <<<'end'
similar to simple quotes $string_var </br>
publish an element of a vector: {$fruit_name[3]}</br>
end;
echo $strNowdoc;

echo strlen($strHeredoc);
?>


