<html>
<head>
<script type="text/x-mathjax-config">
	MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript"
	src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<style>
	p { font-size:20px; }
	form { font-size:20px; }
	div {font-size:20px; color: blue;}
</style>
</head>

<body>
<?php 
function printArr($arr){
	for ($i=0; $i<count($arr); $i++){
		echo $arr[$i]." ";
	}
}

function correctRate($arr, $ans){
	$number = 0;
	for ($i=0; $i<count($arr); $i++){
		if ($arr[$i]==$ans)
			$number++;
	}
	return $number/count($arr);
}

?>

<?php
$msg = "";
if ($_SERVER["REQUEST_METHOD"] == "POST"){
	if (file_exists("collectAns.txt")){
		$f = fopen("collectAns.txt", "a");
	}else{
		$f = fopen("collectAns.txt", "w");
	}
	$q1 = $_POST["q01"];
	$q2 = $_POST["q02"];
	$q3 = $_POST["q03"].PHP_EOL;
	fwrite($f, $q1." ");
	fwrite($f, $q2." ");
	fwrite($f, $q3."\n");
	fclose($f);
	$msg = "have a nice day!";	
	header('Location: '.$_SERVER["PHP_SELF"]); 
	//prevent submission upon refresh
}
?>

<h1> MY QUESTIONNAIRE </h1>

<form method="POST"
	action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
<p>Q1: What is the value of $\pi$?</p>
<input type="radio" name="q01" value="A">A = 1.23<br>
<input type="radio" name="q01" value="B">B = 3.14<br>
<input type="radio" name="q01" value="C">C = 2.98<br>

<p>Q2: What is(are) the root(s) of $x^2-3x+2=0$?</p>
<input type="radio" name="q02" value="A">A: x=0, x=1<br>
<input type="radio" name="q02" value="B">B: x=1, x=2<br>
<input type="radio" name="q02" value="C">C: x=2, x=3<br>

<p>Q3: What is $(\sqrt{2})^3 (\sqrt[3]7)^5$?</p>
<input type="radio" name="q03" value="A">A: $\sqrt{8}(7^{5/3})$<br>
<input type="radio" name="q03" value="B">B: 2<br>
<input type="radio" name="q03" value="C">C: 12345<br>

<br><input type="submit" name="submitAnswer" value="submit answer"><br>
<?php echo $msg; ?>
</form>

<!---------- analysis collectAns.txt ---------->
<?php 
	$rf = fopen("collectAns.txt", "r");
	$words = fread($rf, filesize("collectAns.txt")); //string
	$length = strlen($words);
	$q1Arr = array();
	$q2Arr = array();
	$q3Arr = array();
	$number = 0;
	
	for ($i=0;$i<$length;$i++){
		$temp = $words[$i];
		if (($temp=='A')||($temp=='B')||($temp=='C')){
			if ($number%3==0){
				array_push($q1Arr, $temp);
			}
			if ($number%3==1){
				array_push($q2Arr, $temp);
			}
			if ($number%3==2){
				array_push($q3Arr, $temp);
			}
			$number++;
		}
	}
?>

<div>
<?php
if ((count($q1Arr)==count($q2Arr))&&(count($q1Arr)==count($q3Arr))){
	echo "Q1 Response: "; printArr($q1Arr); echo "<br>";
	echo "Q1 Correct Rate: ".round(correctRate($q1Arr, 'B'),3)."<br>";
	echo "Q2 Response: "; printArr($q2Arr); echo "<br>";
	echo " Correct Rate: ".round(correctRate($q2Arr, 'B'),3)."<br>";
	echo "Q3 Response: "; printArr($q3Arr); echo "<br>";
	echo "Correct Rate: ".round(correctRate($q3Arr, 'A'),3)."<br>";
}
echo "<br>";
echo var_dump($words);
fclose($rf);
?>
</div>



</body>
</html>