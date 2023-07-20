//s = 01, 02, 03, ... and so on
function goToPage(s){
        var myLink = "https://lowhochi.github.io/myVocab";
	var temp = document.getElementById(s).value;
	myLink += temp;
	myLink += ".html";
	window.location.href = myLink;
}
