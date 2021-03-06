var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);

io.on('connection', function(client) {
    console.log('Client connected...');
    client.emit('messages', {hello: 'world'});
    client.on('messages', function(data) {
        console.log(data);
		var message = client.nickname + ': ' + data;
		client.broadcast.emit('messages', message);
		client.emit('messages', message);
    });

	client.on('join', function(name)
	{
		client.nickname = name;
	});
});

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

server.listen(8080);
