var express = require('express');
var app = express();
var logger = require('./logger');

app.use(logger);
app.use(express.static('public'))

app.get('/blocks', function(request, response){
    var blocks = ['fixed', 'movable', 'rotating'];
    response.json(blocks);
});

app.listen(3000);
