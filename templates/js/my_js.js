//function to validate empty field
function check_empty(){
if(document.getElementById('name').value == "" 
|| document.getElementById('email').value == "" 
||document.getElementById('msg').value == "" ){
alert ("Fill All Fields !");
}
	else {  
	document.getElementById('form').submit();  
	alert ("Form submitted successfully...");
	}
}

//function to display Popup
function div_show(){ 
document.getElementById('abc').style.display = "block";
}

//function to hide Popup
function div_hide(){ 
document.getElementById('abc').style.display = "none";
}

