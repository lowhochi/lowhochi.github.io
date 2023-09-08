//input = 00, 01, 02, 03, ... and so on
const mySet = new Set();
mySet.add("00");
mySet.add("01");
mySet.add("02");
mySet.add("03");
mySet.add("04");
mySet.add("05");
mySet.add("06");
mySet.add("07");
mySet.add("08");
mySet.add("09");
mySet.add("10");
mySet.add("11");
mySet.add("12");
mySet.add("13");
mySet.add("14");

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
