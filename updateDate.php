<?php
 $file = $_REQUEST["news"];
 echo "Last updated: ".date("F d Y H:i:s.", filemtime($file));
?>