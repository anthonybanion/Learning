<?php
/* @brief  read api data
 * @details  This file fetches the data from the Dailymotion API 
            and displays it in the form of an object.
 * @file api_dailymotion.php
 * @date 05/05/2024
 * @version 1.0*/ 

$url = "https://api.dailymotion.com/videos?channel=sport&limit=10";

$remove_security = array("ssl"=>array("verify_peer"=>false,"verify_peer_name"=>false));
$file_content = file_get_contents($url,false,stream_context_create($remove_security));
$content_in_object_format = json_decode($file_content);
//print_r($content_in_object_format); 

/*foreach($content_in_object_format->list as $video){
    echo "Title: ".$video->title."<br>";
    echo "id: ".$video->id;
    echo "<br><br>";
}*/
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dailymotion API</title>
</head>
<body>
<h1>Top 10 videos from Dailymotion</h1>
<ul>
<?php foreach($content_in_object_format->list as $video){ ?>
    <li><?php echo "Title: ".$video->title;?></br>
    <?php echo "id: ".$video->id;?></li>
    <?php } ?>
</ul>
</body>
</html>