<?php

$url = "https://rss.nzherald.co.nz/rss/xml/nzhtsrsscid_000000698.xml";

$handle = curl_init();

curl_setopt($handle, CURLOPT_URL, $url);

$data = curl_exec($handle);

$xml=simplexml_load_string($url) or die("Error: Cannot create object");
print_r($xml);

$fp = fopen('lidn.xml', 'w');
fwrite($fp, $data);
fclose($fp);
