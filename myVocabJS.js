const shorthands = ["_", "/ae", "/@r", "@", "/6", "U", "I", "S", "/2", "O", "T", "D", "Z", "N", "/3"];
const htmlCodes = ["&#39;", "&#230;", "&#602;", "&#601", "&#594;", "&#650;", "&#618;", "&#643;", "&#652;",
		   "&#596;", "&theta;", "&eth;", "&#658;", "&#331;", "&#604;"];
					
function showIPA(){	
	for (let i=0; i<vocabs.length; i++){
		let symbol = document.getElementById(vocabs[i]).value;
		if (symbol==="") continue;
			
		for (let j=0; j<shorthands.length; j++){
			symbol = symbol.replaceAll(shorthands[j], htmlCodes[j]);
		}			
		document.getElementById("show_"+vocabs[i]).innerHTML = symbol;
		document.getElementById(vocabs[i]).value = symbol;
	}
}

function showPicture(clickedID){
	let name = clickedID.substring(6);
	let display = "show_"+clickedID.substring(10);
	if (eval(display)){
		document.getElementById(name).innerHTML.style.display = "none";
		eval(display) = false;
	}else{
		document.getElementById(name).innerHTML.style.display = "block"; 
		eval(display) = true;
	}
}

var myDiv = document.getElementById("myDiv");
var myUL = document.createElement("ul");
myUL.className = "navigation";
for (let i=0; i<vocabs.length; i++){
	var myLI = document.createElement("li");
	var myAtag = document.createElement("a");
	let temp = vocabs[i];
	temp = temp.replaceAll("_", "<br>");
	temp = temp.replaceAll("-", " ");
	myLI.className = "navigation";
	myAtag.href = "#"+"show_"+vocabs[i]; //remain on current page
	myAtag.innerHTML = temp;
	/*
	if (temp.length>=12){
		myAtag.style.fontSize = "1vw";
	}
	*/
	myLI.appendChild(myAtag);
	myUL.appendChild(myLI);
}
myDiv.appendChild(myUL);

window.onload = showIPA();
	
