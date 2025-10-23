<?php
/*brief: The json_decode() function is used to decode a JSON object into a PHP
         object or an associative array.
 *details:  forearch loop to read the content of the object.
 *          The json_decode() function is used to decode a JSON object into a PHP          
 *          json_encode() function is used to encode a PHP object or array into 
 *          a JSON string.           
 *file json_rw.php
 *date 03/05/2024
 *version 1.0*/

 $json_content= '[{"name": "John", "age": 25, "city": "New York"}, 
                  {"name": "Paul", "age": 25, "city": "London"}]';
echo "</br>";
print_r($json_content);
echo "</br>";
//transform a json format (string) into array/object.
$content = json_decode($json_content);
print_r($content);
echo "</br>";
echo "</br>";
//read the content of the arrray
foreach($content as $persona){
    echo (($persona -> name)." ".($persona -> age)." ".($persona -> city)."</br>");
}
$name_person = array("Oscar"=>40, "Juan"=>30, "Maria"=>20);
echo "</br>";
//transform an array into json format (string)
$json = json_encode($name_person);
echo $json;
?>