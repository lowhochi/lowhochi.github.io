function showPicture(nameID, check){
  alert("hello world");
  if (check==true){
    document.getElementById(nameID).style.display = "none";
    check = false;
  }else{
    document.getElementById(nameID).style.display = "block";
    check = true;
  }
}
