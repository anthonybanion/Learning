<?php
/* @brief A form is used to apply the post method
 * @details used isset
 * @file post.php
 * @date 30/03/2024
 * @version 1.0*/

    if(isset($_POST['submit'])){
        $name = $_POST['name'];
        $age = $_POST['age'];
        echo "Your name is $name and your age is $age";
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
    <form action="post.php" method = "Post">
        <input type="text" name="name" placeholder="Enter your name">
        <input type="text" name="age" placeholder="Enter your age">
        <input type="submit" name="submit" value="Submit">

    </form>
</body>
</html>