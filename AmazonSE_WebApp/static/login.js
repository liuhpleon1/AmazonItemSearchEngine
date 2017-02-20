var user = $('#username');
var pw = $('#password');
var username = user.val();
var password = user.val();
var myurl = "http://localhost:5000/";
var searchurl = "http://localhost:5000/search";
console.log(myurl);

/*submit the login value*/
$('#login').click(function(event) {
	console.log('login is good');
	username = user.val();
    password = pw.val();
    if(username.length==0){
    	console.log('username error');
    	//window alert "you did not enter username"
    	clean();
    }
    if(password.length==0){
    	console.log('password error');
    	//window alert "you did not enter password"
    	clean();
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
	/* Act on the event */
	clean();
});
/* send info to backend and get the return json format check data, result has two attribute 
   boolean username and boolean password
*/
function senduser(info){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: info
	})
	.done(function(result) {
		console.log(result.username+" "+result.password);
		console.log(typeof(result.username))
		checkuser(result.username,result.password);
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
}
/*check username and password if to see their status 
  based on different value we result differnt result,
  a alert window or jump to another page
*/
function checkuser(correct_username,correct_password){
	console.log(correct_username);
	clean();
	if(correct_username===false&&correct_password===false){
        console.log("wrong username");
        // window one shows: Sorry you are not registered as a user

	}
	else if(correct_username===true&&correct_password===false){
        console.log("wrong password");
        // window two shows: Sorry your password was wrong

	}
	else{
        console.log("successful login");
        window.location.assign(searchurl);
        // jump to search engine

	}
}
/*clean the username and password*/
function clean(){
    user.val('');
    pw.val('');
}