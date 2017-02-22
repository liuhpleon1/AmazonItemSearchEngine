var search = $("#search_text")
myurl = "http://localhost:5000/search/"
var append = $("#cache")

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
			append.append("<span id=cache"+i+">"+result.rank[i]+"</span>&nbsp&nbsp&nbsp");
		}
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}

function show_result(result){

}

$("#search_submit").click(function(event) {
	/* Act on the event */
	var query = {
		"query":search.val()
	}
	console.log(query);
	send_query(query);
});
