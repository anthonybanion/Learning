<?php
/* @brief Get methos
 * @details A form is used to apply the post get
 * @file get.php
 * @date 30/03/2024
 * @version 1.0*/

    if(isset($_GET['submit'])){
        $name = $_GET['name'];
        $age = $_GET['age'];
        echo "Your name is $name and your age is $age";
    }
?>