var EventEmitter = require('events').EventEmitter;

var observer = new EventEmitter();
var observable = new EventEmitter();

observer.on('hello', function(target) {
	console.log('Hello, ' + target);
});

observable.emit('hello', 'world');
