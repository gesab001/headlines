
<!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<body>
<div id="admin"> 
<form action="addnewscgi.py" method="post">
<input type="text" name="keyword" placeholder="keyword"/>

<input type="text" name="title" placeholder="title"/>

<input type="text" name="url" placeholder="xml address"/>

<input type="submit" value="add"/>
</form>
<br>
<form action="../cgi-bin/deletenews.py" method="post">
<input type="text" name="keyword" placeholder="keyword"/>
<input type="submit" value="delete"/>
<br>
</form>
</div>
<select id="selection" name="news" onchange="loadNews(this.value)"></select>

<p id="test"></p>
<p id="dateUpdate"></p>
<div id="demo"></div>

<script>

var windowlocation = window.location.href;

if (windowlocation.includes("192")){
	document.getElementById("admin").style.display = "inline-block";
}else{
	document.getElementById("admin").style.display = "none";
}
var xhttp = new XMLHttpRequest();
var news;
loadSelectionTitles();


function loadSelectionTitles(){
   xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       var myArr = JSON.parse(this.responseText);
       loadSelection(myArr);
	  
    }else{
	//document.getElementById("demo").innerHTML = "its  not working";
	}
 };
 xhttp.open("GET", "newstitles.json", true);
 xhttp.send();
}


function loadSelection(myArrTitles){

 xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
	
       var myArr = JSON.parse(this.responseText);
       for (var x in myArr){
		  var title = myArrTitles[x];
		 if(x=="nzherald"){
			document.getElementById("selection").innerHTML += "<option selected value='"+x+"'>"+title+"</option>";
         }else{			 
			document.getElementById("selection").innerHTML += "<option value='"+x+"'>"+title+"</option>";
		 }
       }
	   var news = document.getElementById("selection").value;
       //changeNews(news);
	   loadNews(news);
    }
 };
 xhttp.open("GET", "news.json", true);
 xhttp.send();
}


function loadNews(news){
 xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
	  //var news = document.getElementById("selection").value;
      //if (news=="pa"){
	   	//loadYoutubeLinks(this);
	  //}else{
       displayFeeds(this);
      //}
	}
 };
 xhttp.open("GET", news+".xml", true);
 xhttp.send();
}

function getYoutubeID(link){
 var split = link.split("=");
 var id = split[1];
 return id;
}

function getEmbedURL(youtubeid){
  url = "https://www.youtube.com/embed/"+youtubeid;
return url;
}

function loadYoutubeLinks(xml){
  var text = "";
  var xmlDoc = xml.responseXML;
  var entries = xmlDoc.getElementsByTagName("entry");
  for (var x=0; x<entries.length;x++){  
	  var entry = entries[x]; 
	  var title = entry.getElementsByTagName("title")[0].childNodes[0].nodeValue;
	  var link = entry.getElementsByTagName("link")[0].getAttribute("href");
          var youtubeid = getYoutubeID(link);
          var embedurl = getEmbedURL(youtubeid);
          var urladdress = "./pl-youtube.html?embedurl="+embedurl;         
  text += "<a href='"+urladdress+"'>"+title+"</a><br><br>";
  }
  document.getElementById("demo").innerHTML = text;

}

function displayFeeds(xml) {
 var xmlDoc = xml.responseXML;
 //document.getElementById("test").innerHTML = xmlDoc;

    var items = xmlDoc.getElementsByTagName("item");
	if (items.length<1){
       loadYoutubeLinks(xml);
	}else{
		var text = "";
		var xmlDoc = xml.responseXML;
		var items = xmlDoc.getElementsByTagName('item');
		for(var x=0; x<items.length;x++){
		  try{
			var item = items[x];
			var title = item.getElementsByTagName('title')[0].childNodes[0];
			var description = item.getElementsByTagName('description')[0].childNodes[0];
			link = item.getElementsByTagName('link')[0].childNodes[0];
			text += "<h3><a href='"+link.nodeValue+"'>"+title.nodeValue +"</a></h3>"+ description.nodeValue;
		  }catch{}
		}
		document.getElementById("demo").innerHTML =
		text; 
	}
	updateDate();
}


function myFunction(xml) {
  var xmlDoc = xml.responseXML;
 //document.getElementById("test").innerHTML = xmlDoc;

    var items = xmlDoc.getElementsByTagName("item");
	if (items.length<1){
       loadYoutubeLinks(xml);
	}else{
		var text = "";
		var xmlDoc = xml.responseXML;
		var items = xmlDoc.getElementsByTagName('item');
		for(var x=0; x<items.length;x++){
			var item = items[0];
			var title = item.getElementsByTagName('title')[0].childNodes[0];
			var description = item.getElementsByTagName('description')[0].childNodes[0];
			link = item.getElementsByTagName('link')[0].childNodes[0];
			text += "<h3><a href='"+link.nodeValue+"'>"+title.nodeValue +"</a></h3>"+ description.nodeValue;
		}
		document.getElementById("demo").innerHTML =
		text; 
	}
	updateDate();
}

function updateDate(){
  var news = document.getElementById("selection").value + ".xml";
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
           var text = this.responseText;
           document.getElementById("dateUpdate").innerHTML = "Updated: " + text;
    }
    else{
         //document.getElementById("dateUpdate").innerHTML = "error";
    }
  };
  xhttp.open("GET", "lastNewsUpdate.txt", true);
  xhttp.send();
}
</script>

</body>
</html> 
