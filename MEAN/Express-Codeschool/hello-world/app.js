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

// This function does the same as the above but it converts the array
// to JSON in a more explict way
app.get('/explicity_blocks', function(request, response) {
    var blocks = ['fixed', 'movable', 'rotating'];
    response.json(blocks);
});
app.listen(3000);
