var search = $("#search_text")
myurl = "http://localhost:5000/search/"
var append = $("#cache")

function init(start){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: true,
	})
	.done(function(data) {

		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}
var array = [];
function send_query(data){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: data,
	})
	.done(function(result) {
		append.text('');
		for(var i=0;i<result.rank.length;i++){
			append.append("<span class = 'span_search' id=cache"+i+">"+result.rank[i]+"</span>&nbsp&nbsp&nbsp");
		}
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}

send_query("");

$("#search_submit").click(function(event) {
	/* Act on the event */
	var query = {
		"query":search.val()
	}
	console.log(query);
	send_query(query);
});

for(var i=0;i<15;i++){
	var box = $("#cache"+i);
	box.hover(function() {
		/* Stuff to do when the mouse enters the element */

		search.val("works");
	}, function() {
		/* Stuff to do when the mouse leaves the element */
	});
}
