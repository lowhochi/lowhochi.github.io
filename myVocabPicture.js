// <script type="text/javascript" src="myVocabPicture.js"></script>
// <button class="mypic" onclick="showPicture('WORD')">PICTURE</button>
// <img class="mypic" id="pic_WORD" src="myPictures/WORD.jpg" style="display:none;">

var checks = {"zebra_crossing": false,
              "beige": false,
              "xylophone": false,
              "stereo": false,
              "cassette": false,
              "chrysanth": false,
              "grocery": false};

function showPicture(input){
        //alert(checks[input]);
        nameID = "pic_"+input;        
        if (checks[input]==true){
                document.getElementById(nameID).style.display = "none";
                checks[input] = false;
        }else{
                document.getElementById(nameID).style.display = "block";
                checks[input] = true;
        }
}
