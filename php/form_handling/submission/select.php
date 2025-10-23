<?php
/*brief The select type allows the user to select only one option from a set of options.  
 *details We use the select tag to create a dropdown list. 
 *file select.php
 *date 22/04/2024
 *version 1.0*/
$language="";
if(isset($_POST)){
    $language = (isset($_POST["language"]))? $_POST["language"]: "";
    }
    print_r($_POST);
  
?>   
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Select</title>
</head>
<body>
    <h3>What language do you need?</h3></br>
    <?php 
    echo "You selected: $language";
    ?>
    <br>
    <form action="select.php" method="post">
    <select name="language" id="" >
        <option value="none">>Select a language</option>
        <option value="html" <?php echo($language=="html")? "selected": "";?> >HTML</option>
        <option value="css" <?php echo($language=="css")? "selected": "";?> >CSS</option>
        <option value="javascript" <?php echo($language=="javascript")? "selected":"";?> >JavaScript</option>
        <option value="php" <?php echo($language=="php")? "selectedS":"";?>  >PHP</option>
    </select> 
</br> 
    <input type="submit" value="Submit">
    </form>
</body>
</html>