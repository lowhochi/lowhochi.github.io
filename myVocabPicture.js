var checks = { "zebra_crossing": false };

function showPicture(input){
        alert(checks[input]);
        nameID = "pic_"+input;        
        if (checks[input]==true){
                document.getElementById(nameID).style.display = "none";
                checks[input] = false;
        }else{
                document.getElementById(nameID).style.display = "block";
                checks[input] = true;
        }
}
