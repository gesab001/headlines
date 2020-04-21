
<!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<body>
<form action="../cgi-bin/addnews.py" method="post">
<input type="text" name="keyword" placeholder="keyword"/>

<input type="text" name="title" placeholder="title"/>

<input type="text" name="url" placeholder="xml address"/>

<input type="submit" value="add"/>
<br>
<form action="../cgi-bin/deletenews.py" method="post">
<input type="text" name="keyword" placeholder="keyword"/>
<input type="submit" value="delete"/>
<br>
</form>
<select id="selection" name="news" onchange="changeNews(this.value)"></select>

<p id="dateUpdate"></p>
<div id="demo"></div>

<script>

var xhttp = new XMLHttpRequest();
var news;
//changeNews(news);
loadSelectionTitles();


function loadSelectionTitles(){

 xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       var myArr = JSON.parse(this.responseText);
       loadSelection(myArr);
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
       changeNews(news);
    }
 };
 xhttp.open("GET", "news.json", true);
 xhttp.send();
}

function changeNews(news){
 news = news;
 xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       loadNews(news);
    }
 };
 xhttp.open("GET", "../../cgi-bin/headlines2.py?news="+news, true);
 xhttp.send();
}

function loadNews(news){

 xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    displayFeeds(this);
    }
 };
 xhttp.open("GET", news+".xml", true);
 xhttp.send();
}

function displayFeeds(xml) {
    var xmlDoc = xml.responseXML;
    var titles = xmlDoc.getElementsByTagName("title");
    var text ="";
	var title = "";
    for (var x=0; x<titles.length;x++){
		 if (titles[x].childNodes[0].nodeValue!=title)
           text += "<p>"+titles[x].childNodes[0].nodeValue+"</p>";
    }     
    document.getElementById("demo").innerHTML = text;
    updateDate();
}

function updateDate(){
  var news = document.getElementById("selection").value + ".xml";
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
           var text = this.responseText;
           document.getElementById("dateUpdate").innerHTML = text;
    }
    else{
         document.getElementById("dateUpdate").innerHTML = "error";
    }
  };
  xhttp.open("GET", "updateDate.php?news="+news, true);
  xhttp.send();
}


</script>

</body>
</html> 
