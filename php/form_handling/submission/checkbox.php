<?php
/*brief The checkbox type allows the user to select multiple options from a set of options.  
 *details We use the value yes yo leave the box checked by default.
 *file checkbox.php
 *date 20/04/2024
 *version 1.0*/

$htmlbox="";
$phpbox="";
$cssbox="";

if(isset($_POST["submit"])){
    $htmlbox = (isset($_POST["htmlbox"])=="si")? "checked":"";
    $phpbox = (isset($_POST["phpbox"])=="si")? "checked":"";
    $cssbox = (isset($_POST["cssbox"])=="si")? "checked":"";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkbox</title>
</head>
<body>
<form action="checkbox.php" method="post">
    <h3>What language do you need?</h3></br>
    HTML<input type="checkbox" <?php echo $htmlbox;?> name="htmlbox" value="si" id=""/></br>
    PHP<input type="checkbox" <?php echo $phpbox;?> name="phpbox" value="si" id=""/></br>
    CSS<input type="checkbox" <?php echo $cssbox;?> name="cssbox" value="si" id=""/></br>
    <input type="submit" name="submit" value="send">
</form>
</body>
</html>