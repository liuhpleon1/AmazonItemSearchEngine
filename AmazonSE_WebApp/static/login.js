var user = $('#username');
var pw = $('#password');
var username = user.val();
var password = user.val();
var myurl = "http://localhost:5000/";
console.log(myurl);

$('#login').click(function(event) {
	console.log('login is good');
	username = user.val();
    password = pw.val();
    if(username.length==0){
    	console.log('username error');
    }
    if(password.length==0){
    	console.log('password error');
    }
    else if(username.length>0&&password.length>0){
	    var userinfo = {
	    	'username': username,
	    	'password': password
	    }
	    senduser(userinfo);
	}
});

$('#clear').click(function(event) {
    console.log('clear is good');
    user.val('');
    pw.val('');
});

function senduser(info){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: info
	})
	.done(function() {
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}

function checkuser(){
	$.ajax({
		url: myurl,
		type: 'Get',
		dataType: 'json',
		data: {param1: 'value1'},
	})
	.done(function() {
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}