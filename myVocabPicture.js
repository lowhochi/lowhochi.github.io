var check_zebra_crossing = false;

function showPicture(nameID, check){
  alert(check);
  if (check==true){
    document.getElementById(nameID).style.display = "none";
    check = false;
  }else{
    document.getElementById(nameID).style.display = "block";
    check = true;
  }
}
