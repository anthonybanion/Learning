<?php
/*brief The radio type allows the user to select only one option from a set of options.  
 *details We use terniary condition to leave the default value checked.
 *file radio.php
 *date 20/04/2024
 *version 2.0*/

$language = "";
    if(isset($_POST['submit'])){
        $language = $_POST['language'];
        echo "You have selected: ".$language;
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Radio</title>
</head>
<body>
    <form action="radio.php" method="post">
        <h3>What language do you need?</h3></br>
        HTM<input type="radio" <?php echo($language=="html")? "checked":""; ?>
            name="language" value="html" id=""/><br>
        PHP<input type="radio"  <?php echo($language=="php")? "checked":""; ?> 
            name="language" value="php" id=""/><br>
        CSS<input type="radio"  <?php echo($language=="css")? "checked":""; ?> 
            name="language" value="css" id=""/><br>
        <input type="submit" name="submit" value="Send">
</body>
</html>