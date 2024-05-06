// <script type="text/javascript" src="myVocabPicture.js"></script>
// <button class="mypic" onclick="showPicture('WORD')">PICTURE</button></p>
// <img class="mypic" id="pic_WORD" src="myPictures/WORD.jpg" style="display:none;">

var checks = {"zebra_crossing": false,
              "beige": false,
              "zodiac": false,
              "xylophone": false,
              "stereo": false,
              "cassette": false,
              "chrysanth": false,
              "grocery": false,
              "bruise": false,
              "sling": false,
              "cash_register": false,
              "backdrop": false,
              "quad-bike": false,
              "tickle": false,
              "harness": false,
              "scaffolding": false,
              "roundabout": false,
              "incubator": false,
              "lip-balm": false,
              "pickup": false,
              "santa-claus": false,
              "frown": false,
              "bucket": false,
              "overpass": false,
              "bridge": false,
              "scouring_pad": false,
              "crown-braid": false,
              "curb": false,
              "tally": false,
              "candle": false};

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
