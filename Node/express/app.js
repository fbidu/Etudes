var express = require('express');

var app = express();

app.get('/', function(request, response){
	response.sendFile(__dirname + "/index.html");
});

app.listen(8080);
