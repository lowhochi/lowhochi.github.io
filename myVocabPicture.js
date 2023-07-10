var checks = { zebra_crossing: false };

function showPicture(input, checks){
        alert("checks[input] = "+checks[input]);
        nameID = "pic_"+input;        
        if (check==true){
                document.getElementById(nameID).style.display = "none";
                checks[input] = false;
        }else{
                document.getElementById(nameID).style.display = "block";
                checks[input] = true;
        }
}
