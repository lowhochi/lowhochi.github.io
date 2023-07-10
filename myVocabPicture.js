var checks = { zebra_crossing: false };

function showPicture(input, checks){
        alert("HELLO WORLD");
        nameID = "pic_"+input;        
        if (check==true){
                document.getElementById(nameID).style.display = "none";
                checks[input] = false;
        }else{
                document.getElementById(nameID).style.display = "block";
                checks[input] = true;
        }
}
