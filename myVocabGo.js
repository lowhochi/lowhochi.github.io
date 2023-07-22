//s = 01, 02, 03, ... and so on
function goToPage(s){
        var myLink = "https://lowhochi.github.io/myVocab";
	var temp = document.getElementById(s).value;
	if (temp=="00"){
		temp = "Search";
	}
	myLink += temp;
	myLink += ".html";
	//alert(myLink);
	window.location.href = myLink;
}
