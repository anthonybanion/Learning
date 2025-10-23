<?php
/*brief The text area type allows the user to enter multiple lines of text.  
 *details We use the text area tag to create a text area. 
 *file text_area.php
 *date 22/04/2024
 *version 1.0*/

 $opinion="";
    if(isset($_POST)){
        $opinion = (isset($_POST["opinion"]))? $_POST["opinion"]: "";
        }
 print_r($_POST);
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Area</title>
</head>
<body>
        <?php echo "You opinion is: $opinion"; ?></br>

    <h1>Text Area</h1></br>
    <h3>What is your opinion</h3></br>
    <form action= "text_area.php" method="post">
        <textarea name="opinion" id="" cols="20" rows="10">
        <?php echo $opinion; ?>
        </textarea>
        </br>
    <input type="submit" value="submit">
    </form>
    
</body>
</html>