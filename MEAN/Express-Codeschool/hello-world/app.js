var express = require('express');
var app = express();

app.get('/', function(request, response) {
    response.send('Hello, world!');
});

app.get('/blocks', function(request, response) {
    var blocks = ['fixed', 'movable', 'rotating'];
    // Express will serialize 'blocks' to json!
    // and will change the content-type header accordingly
    response.send(blocks);
});

// This function does the same as the above but it converts the array
// to JSON in a more explict way. Also changes the content-type header
app.get('/explicity_blocks', function(request, response) {
    var blocks = ['fixed', 'movable', 'rotating'];
    response.json(blocks);
});


// When sending a plain string, the content-type will be text/html
app.get('/plain_blocks', function(request, response) {
    var blocks = 'fixed, movable, rotating';
    response.send(blocks);
});

// When sending a string containing HTML tags, the content-type header
// will be set to text/html
app.get('/html_blocks', function(request, response) {
    var blocks = '<ol><li>fixed</li><li>movable</li><li>rotating</li></ol>'
    response.send(blocks);
});

// When sending a string with response.write and response.end, there will be no
// content-type header. It was probably added by Express and the .write and .end
// methods are native to Node
app.get('/raw_blocks', function(request, response) {
    var blocks = '<ol><li>fixed</li><li>movable</li><li>rotating</li></ol>'
    response.write(blocks);
    response.end();
});



// The request headers may be checked using curl -i or httpie
app.listen(3000);
