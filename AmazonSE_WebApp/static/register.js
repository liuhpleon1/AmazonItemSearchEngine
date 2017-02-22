var username = $("#username").val();
var password = $("#password").val();
var confirm = $("#confirm").val();
var cellphone = $("#cellphone").val();
var email = $("#email").val();
var myurl ="http://localhost:5000/signup/"
var loginurl = "http://localhost:5000/";
/*check if the password==confrim*/
function judge(pw,cpw){
    if(pw!=cpw){
    	console.log("your password are different")
    }
    else{
    	console.log("right password")
    }
}
/*check the signup information is completed or not*/
function page_check(){
	username = $("#username").val();
	password = $("#password").val();
	confirm = $("#confirm").val();
	cellphone = $("#cellphone").val();
	email = $("#email").val();
	if(username.length==0||password.length==0||confirm.length==0||cellphone.length==0||email.length==0){
		console.log("your information is not complete");
		return null;
	}
	else if(password!=confirm){
		console.log('please input same password');
		return null;
	}
	else{
		var new_user={
			"username":username,
			"password":password,
			"cellphone":cellphone,
			"email":email
		}
		return new_user;
	}
}
/*clean all the input*/
function clean(){
	$("#username").val("");
	$("#password").val("");
	$("#confirm").val("");
	$("#cellphone").val("");
	$("#email").val("");
}

/*check if successfully regiestered*/
function signup_check(has_username,has_email,has_cellphone){
    if(has_username==true){
        console.log("username exist")
        clean()
    }
    else if(has_email==true){
        console.log("email exist")
        clean()
    }
    else if(has_cellphone==true){
        console.log("cellphone exist")
        clean()
    }
    else{
    	console.log("successfully")
    	clean()
    	window.location.assign(loginurl);
    }
}

/*communicate with the backend to register user*/
function register(new_user){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: new_user,
	})
	.done(function(result) {
		console.log(result)
		signup_check(result.username,result.email,result.cellphone)
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}

/*submit button*/
$("#submit").click(function(event) {
	/* Act on the event */
	var new_user = page_check();
	if(new_user==null){
        clean();
        console.log("miss information");
	}
	else{
		console.log("vaild input");
		console.log(new_user);
        register(new_user)
	}
});

/*cancel button*/
$("#cancel").click(function(event) {
	/* Act on the event */
	clean();
	window.location.assign(loginurl);
});