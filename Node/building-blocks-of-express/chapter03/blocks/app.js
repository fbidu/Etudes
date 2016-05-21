var express = require('express');
var app = express();

app.use(express.static('public'))

var blocks = {
    'Fixed': 'Fastened in place',
    'Movable': 'It is moving!!',
    'Rotating': 'You got the idea'
};

app.get('/blocks/:name', function(request, response) {
    var description = blocks[request.params.name];
    if (!description) {
        response.status(404).json('No description found for ' + request.params.name);
    } else {
        response.json(description);
    }
});

app.listen(3000);
