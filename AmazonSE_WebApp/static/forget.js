var username = $("#username")
var email = $("email")
var cellphone = $("cellphone")
var myurl ="http://localhost:5000/forget/"
var loginurl = "http://localhost:5000/";

function check_password(data){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: data,
	})
	.done(function(result) {
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}

function send_information(data){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: data,
	})
	.done(function(result){
		if(result.email == true||result.cellphone==true){
		    console.log("email has been send");
	    }
	    else{
	    	console.log("error! can not be send")
	    }

	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});	
}

$("#username_submit").click(function(event) {
	/* Act on the event */
	if(username.val().length==0){
		console.log("you didn't input anything");
	}
	else{
		check_password(username.val());
	}
});

$("#userinfo_submit").click(function(event) {
	/* Act on the event */
	var data = {
		"email": email.val(),
		"cellphone": cellphone.val()
	}
	if(data.email.length==0&&data.cellphone.length==0){
		console.log("must input at least email or cellphone");
	}
	else{
		check_password(username.val());
	}
});