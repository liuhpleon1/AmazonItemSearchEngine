var username = $("#username")
var email = $("email")
var cellphone = $("cellphone")
var myurl ="http://localhost:5000/forget/"
var loginurl = "http://localhost:5000/";

function find_password(data){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: data,
	})
	.done(function(result) {
		if(result.password==null){
			alert("no information found in database");
		}
		else{
			alert("your password is: "+result.password);
		}
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}

function find_information(data){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: data,
	})
	.done(function(result){
		var username = result.username;
		var password = result.password;
		if(username!=null&&password!=null){
			alert("yor username: "+username+"    your password:"+password);
		}
	    else{
	    	console.log("server error!");
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
		alert("please input your username");
	}
	else{
		find_password({"username":username.val()});
	}
});

$("#userinfo_submit").click(function(event) {
	/* Act on the event */
	var data = {
		"email": email.val(),
		"cellphone": cellphone.val()
	}
	if(email.val()==null && cellphone.val()==null){
		alert("must input at least email or cellphone");
	}
	else{
		find_information(data);
	}
});

$("#go_back_submit").click(function(event) {
	/* Act on the event */
	window.location.assign(loginurl);
});