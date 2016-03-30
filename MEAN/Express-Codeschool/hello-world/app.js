var express = require('express');
var app = express();

app.get('/', function(request, response) {
    response.send('Hello, world!');
});

app.get('/blocks', function(request, response) {
    var blocks = ['fixed', 'movable', 'rotating'];
    // Express will serialize 'blocks' to json!
    response.send(blocks);
});

app.listen(3000);
