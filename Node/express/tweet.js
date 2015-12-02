// App that, given a twitter username, fetches the latest 10 tweets
// and displays them

var request = require('request');
var url = require('url');
var express = require('express');
var config = require('config');

var app = express();

app.get('/tweets/:username', function(req, response){
	var username = req.params.username;

	options = {
		protocol: "https:",
		host: 'api.twitter.com',
		pathname: '/1.1/statuses/user_timeline.json',
		query: { screen_name: username, count: 10 }
	}
	oauth = {
	   	consumer_key: config.get("Twitter.consumer_key"),
		consumer_secret: config.get("Twitter.consumer_secret")
	}

	var twitterUrl = url.format(options);
	request({url: twitterUrl, oauth:oauth}, function(err, res, body) {
		var tweets = JSON.parse(body); // getting the tweets from the body
		response.locals = {tweets: tweets, name: username};
		response.render('tweets.ejs');
	});
});

app.listen(8080);
