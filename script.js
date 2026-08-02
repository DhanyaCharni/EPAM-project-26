function hideSteps(){

document.getElementById("steps").style.display="none";

}

function validateCustomer(){

let id=document.getElementById("custid").value.trim().toUpperCase();

if(id.includes("XYZ")){

document.getElementById("result").style.color="#7CFC00";

document.getElementById("result").innerHTML="✅ Customer ID Verified Successfully.";

}
else{

document.getElementById("result").style.color="#ff4d4d";

document.getElementById("result").innerHTML="❌ Invalid Customer ID.";

}

}

function generateCoupon(){

let id=document.getElementById("custid").value.trim().toUpperCase();

if(id.includes("XYZ")){

let coupon="DIWALI"+Math.floor(Math.random()*9000+1000);

document.getElementById("result").style.color="#FFD700";

document.getElementById("result").innerHTML="🎉 Congratulations!<br><br>Your Coupon Code:<br><h2>"+coupon+"</h2>";

}
else{

document.getElementById("result").style.color="#ff4d4d";

document.getElementById("result").innerHTML="Please validate a valid Customer ID first.";

}

}