var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);

var redis = require('redis');
var redisClient = redis.createClient();

var messages = [];

var storeMessages = function(data)
{
	message = JSON.stringify({data: data});
	redisClient.lpush("messages", message, function(err, response)
		{
			redisClient.ltrim("messages", 0, 9);
		});
};

io.on('connection', function(client) {
    console.log('Client connected...');
    client.emit('messages', {hello: 'world'});
    client.on('messages', function(data) {
        console.log(data);
		var message = client.nickname + ': ' + data;
		client.broadcast.emit('messages', message);
		client.emit('messages', message);
		storeMessages(message);
    });

	client.on('join', function(name)
	{
		client.nickname = name;
		redisClient.lrange("messages", 0, -1, function(err, messages)
		{
			messages = messages.reverse();

			messages.forEach(function(message)
			{
				message = JSON.parse(message);
				client.emit('messages', message.data);
			});
		});

		client.broadcast.emit('add chatter', name);
		redisClient.sadd('chatters', name);

		redisClient.smembers('chatters', function(err, names)
		{
			names.forEach(function(name)
			{
				client.emit('add chatter', name);
			});
		});
	});
});

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

server.listen(8080);
