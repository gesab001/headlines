<?php

$file = "news.json";
$news = $_POST["news"];
$rss =  $_POST["rss"];
echo $news;
echo $rss;
$json = json_decode(file_get_contents($file), true);
$json[$user] = array($news => $rss);

file_put_contents($file, json_encode($json));
echo "added successfully";
?>
