<?php
/*brief The archive type allows the user to select a file to upload.
 *details: We use the enctype attribute to specify how the form-data
 *         should be encoded when submitting it to the server.
 *         move_uploaded_file() function moves an uploaded file to a new location.
 *file archive.php
 *date 03/05/2024
 *version 1.0*/

$file="";
    if(isset($_POST["send"])){
        print_r($_POST);
        print_r($_FILES);

        echo " </br> el nombre es: ";
        print_r($_FILES["archive"]["name"]);
        echo "</br> la ruta temporal es: ";
        print_r($_FILES["archive"]["tmp_name"]);
        echo "</br>";

        $file=$_FILES["archive"]["name"];
        $temporal=$_FILES["archive"]["tmp_name"];

        move_uploaded_file($temporal,"D:/program/practices/temp/image/".$file);
        
    }?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Archive</title>
</head>
<body>
    <form action="archive.php" enctype="multipart/form-data" method="post">
        <h3>Imagen</h3>
        <input type="file" name="archive" id=""></br>
        <input type="submit" name="send" value="submit">
    </form>
    
</body>
</html>