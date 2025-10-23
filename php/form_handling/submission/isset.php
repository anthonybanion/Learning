<?php
/* @brief: used isset to check if the submit button was pressed
 * isset is a function that checks if a variable is set and is not null   
 * @details: isset whit method post 
 * @file: isset.php
 * @date 05/04/2024
 * @update: we add code php into the HTML
 * @version 2.0 */

    if(isset($_POST['submit'])){
        $name = (isset($_POST['name']))?$_POST['name']:"";
        $email = (isset($_POST['email']))?$_POST['email']:"";
    }
?>
<!DOCTYPE html>
<html lang = "es">
<head>
    <meta charset = "UTF-8">
    <meta http-equiv = "X-UA-Compatible" content = "IE=edge">
    <meta name = "viewport" content = "width=device-width, initial-scale=1.0">
    <title>PHP</title>
</head>
<body>
    // we add the php code into the HTML
    <?php if(isset($_POST['submit'])){?>
        <h1>Nombre: <?php echo $name;?></h1>
        <h1>Correo: <?php echo $email;?></h1>
    <?php }?>

    <form action ="isset.php" method = "post">
        <input type = "text" name = "name" placeholder = "Nombre">
        <input type = "text" name = "email" placeholder = "Correo">
        <input type = "submit" name = "submit" value = "Enviar">
</body>
</html>