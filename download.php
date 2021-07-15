<button onclick="goBack()">Go Back</button>

<script>
function goBack() {
  window.history.back();
}

</script>
<?php



$command = "python3 updateNews.py";
$output=null;
$resultcode = null;
#exec($command, $output, $resultcode);
while (@ ob_end_flush()); // end all output buffers if any

$proc = popen($command, 'r');




$liveoutput = "";
echo '<pre>';
while (!feof($proc))
{
    $liveoutput = fread($proc, 4096);
    echo $liveoutput;
    @ flush();
}
echo '</pre>';

if ($resultcode==0){
  echo "successfully updated news";
}

?>

