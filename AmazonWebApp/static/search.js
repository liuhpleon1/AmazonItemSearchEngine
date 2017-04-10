var search = $("#search_text");
var myurl = "http://localhost:5000/search/";
var append = $("#cache");
var login = $("#checklogin");
var insert_item = $("#item_content");
var load = $("#loading"); 
var unload = $("#unloading");
var select = $("#select_category")
var startprice = $("#start")
var endprice = $("#end")

function send_query(data){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: data,
		beforeSend: function() {
		    load.show();
	        unload.hide();
		},
	})
	.done(function(result) {
		load.hide();
	    unload.show();

		var items = result.item;
		var username = result.username;
		var rank = result.rank;

		check(username);
        
		append.empty();
		for(var i=0;i<rank.length;i++){
			append.append("<span id=cache"+i+">"+result.rank[i]+"</span>&nbsp&nbsp&nbsp");
		}

        insert_item.empty();  
		for(var i =0;i<Math.min(items.length,1000);i++){
			var item = items[i];
			var title = item.title;
			var price = item.price;
			var image = item.imgurl;
			var asin = item.asin;
			var category = item.category;
			var description = item.description;
			if(description.length>200){
				description = description.substring(0,200)+".......";
			}
			price = price.toString();
			if(price.length>5){
				price = price.substring(0,5);
			}
			insert_item.append("<li id = 'item"+i+"' class = 'item_block'></li>");
            var block = $("#item"+i);
            block.append("<span class = 'item_pic'><img src="+image+" id = 'item_pic' align='left'></div>");
            block.append("<span class = 'item_info' id='info"+i+"'></span>");
            var info = $("#info"+i);
			info.append("<div class = 'item_title' id = 'title"+i+"'>"+title+"</div>");
            info.append("<div id = 'description class='item_description'>"+description+"</div>");
            if(price>0){
                info.append("<div id = 'price' class = 'item_price'>price: $ "+price+"</div>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp");
            }
            else{
            	info.append("<div class = 'item_price'>currently unavailable</div>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp");
            }
            info.append("<div id = 'category' class = 'item_price'>category: "+category+"</div><br>")
            if(username!==''){
            	if(price>0){
                    info.append("<input type='submit' value = 'add to cart' class='item_button' id="+asin+">");
                }
            }
		}
		$('.button_register').each(function(){
	        console.log("hello");
	        console.log($(this).attr('id'));
            $(this).click(function(){
                var thisasin = $(this).attr('id');
                var data = {
        	        "asin":thisasin
                }
                console.log(data);
                buy_item(data);
            });
        });
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
}

function check(user){
    console.log(user);
    login.empty();
    if(user===''){
	    $("#checklogin").append('<a href="http://localhost:5000/" >login</a>');
	}
    else{
	    login.append('<span>welcome</span>&nbsp');
	    login.append('<a href="http://localhost:5000/info">'+user+'</a>&nbsp');
    }
}

$("#search_submit").click(function(event) {
	/* Act on the event */
	var query = {
		"query":search.val(),
		"category":select.val(),
		"startprice":startprice.val(),
		"endprice":endprice.val()
	}
	send_query(query);
	console.log(query);
});

function buy_item(data){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: data,
	})
	.done(function(result) {
		alert("Added!")
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
	
}

send_query("");
load.hide();
