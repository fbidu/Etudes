#! /usr/bin/env node

var exec = require('child_process').exec;

var userArgs = process.argv.slice(2);
var searchPattern = userArgs[0];

var child = exec('ls -a | grep ' + searchPattern, function(err, stdout, stderr)
				 {
					console.log(stdout);
				 });
