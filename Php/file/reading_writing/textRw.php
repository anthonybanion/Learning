<?php 
/* @brief:  Read and write a file in PHP
* @details: Create a file and write some content in it.
*           Read the content of the file.
* file text_rw.php
* @date: 05/05/2024
 */

$name_file= "D:/program/practices/temp/text/readme.text";
$content = <<<README
welcome to php
a multipurpose programming language
 where are we going to develop backend
README;
$open_file = fopen($name_file, "w") or die("Unable to open file!");
fwrite($open_file, $content);
fclose($open_file);
echo "file created successfully";
echo "<br>";

$text_path = "D:/program/practices/temp/text/readme.text";
$open_file = fopen($text_path, "r") or die("Unable to open file!");
$content_file = fread($open_file, filesize($text_path));
echo $content_file;
fclose($open_file);
?>