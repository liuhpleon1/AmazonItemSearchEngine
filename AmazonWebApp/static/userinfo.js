var loginurl = "http://localhost:5000/";
var searchurl = "http://localhost:5000/search/";
var myurl = "http://localhost:5000/info/";

function getuserinfo(data){
	$("#password1").hide();
    $("#email1").hide();
    $("#cellphone1").hide();
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: data,
	})
	.done(function(result) {
		var info = result.info;
		var username = info["username"];
		var password = info["password"];
		var email = info["email"];
		var cellphone = info["cellphone"];
		var items = info["item"];
		//console.log(items[1].title);
		$("#username").empty();
		$("#password0").show();
		$("#email0").show();
		$("#cellphone0").show();
		$("#password0").empty();
		$("#email0").empty();
		$("#cellphone0").empty();
		$("#username").append(username);
		$("#password0").append(password);
		$("#email0").append(email);
		$("#cellphone0").append(cellphone);
		var price = 0;
		for(var i=0;i<items.length;i++){
			item = items[i]; 
			price = price+append(item,i);
		}
        $("#totalprice").append(price);
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}
function delete_item(data){
	asin = data.asin;
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: data,
	})
	.done(function(result) {
		var info = result.info;
		var items = info["item"];
		console.log("success");
		location.reload();
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}
function append(item,i){
    var title = item.title;
	var price = item.price;
	var image = item.image;
	var asin = item.asin;
	var category = item.category;
	var amount = item.amount;
	$("#your_item").append("<li id = 'item"+i+"' class = 'item_block'></li>");
    var block = $("#item"+i);
    block.append("<span class = 'item_pic'><img src="+image+" id = 'item_pic'></span>");
    block.append("<span class = 'item_info' id='info"+i+"'></span>");
    var info = $("#info"+i);
	info.append("title:<span id = 'title"+i+"'>"+title+"</span><br>");
    info.append("amount:<span id = 'description'>"+amount+"</span><br>");
    info.append("price:<span id = 'price'>$ "+price+"</span><br>");
    info.append("category:<span id = 'category'>"+category+"</span><br>")
    info.append("<input type ='submit' value='delete' id = '"+asin+"' class='mybutton'>")
    $('.mybutton').each(function(){
	    console.log($(this).attr('id'));
        $(this).click(function(){
            var thisasin = $(this).attr('id');
            var data = {
        	    "asin":thisasin
            }
            console.log(data);
            delete_item(data);
        });
    });
    var payment = amount*price;
    return payment;
}

function buy_item(){
    var data = {
    	"buy":true
    }
    $.ajax({
    	url: myurl,
    	type: 'POST',
    	dataType: 'json',
    	data: data,
    })
    .done(function() {
    	location.reload();
    	console.log("success");

    })
    .fail(function() {
    	console.log("error");
    })
    .always(function() {
    	console.log("complete");
    });
    
}

function changeuserinfo(data){
	alert("your information will change");
    $.ajax({
    	url: myurl,
    	type: 'POST',
    	dataType: 'json',
    	data: data,
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
$("#buy").click(function(event) {
	price = $("#totalprice").text();
	alert("total price is: $"+price);
	buy_item();
	$("#your_item").empty();
	 console.log(price);
});
$("#makechange").click(function(event) {
	var pc = $("#passwordc");
	var ec = $("#emailc");
    var cc = $("#cellphonec");
    var cp = pc.val().length==0?null:pc.val();
    var ce = ec.val().length==0?null:ec.val();
    var ccp = cc.val().length==0?null:cc.val();
	var userinfo={
    	"password":cp,
    	"email":ce,
    	"cellphone":ccp
    };
    console.log(userinfo);
    changeuserinfo(userinfo);
    location.reload();
});

jQuery(document).ready(function($) {
	getuserinfo("");
});


$("#logout").click(function(event) {
	/* Act on the event */
	alert("you will logout your account");
	window.location.assign(loginurl);
});

$("#cancel").click(function(event) {
	/* Act on the event */
	location.reload();
});

$("#c_password").click(function(event) {
	/* Act on the event */
	$("#password0").hide();
	$("#password1").show();
});

$("#c_email").click(function(event) {
	$("#email0").hide();
	$("#email1").show();
});

$("#c_cellphone").click(function(event) {
	$("#cellphone0").hide();
	$("#cellphone1").show();
});

$("#back").click(function(event) {
	/* Act on the event */
	window.location.assign(searchurl);
});

