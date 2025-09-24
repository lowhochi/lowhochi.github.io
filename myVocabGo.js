//input = 00, 01, 02, 03, ... and so on
const mySet = new Set();

var page = 25;
var ss = "";
for (let i=0; i<page; i++){
	if (i<10){
		ss = "0" + i.toString();
	}else{
		ss = i.toString();
	}
	mySet.add(ss);
}

function goToPage(s){
        var myLink = "https://lowhochi.github.io/myVocab";
	var temp = document.getElementById(s).value;
	if (!mySet.has(temp)){
		return;
	}
	if (temp=="00"){
		temp = "Search";
	}
	myLink += temp;
	myLink += ".html";
	//alert(myLink);
	window.location.href = myLink;
}
