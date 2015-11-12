var fs = require('fs');
var http = require('http');

http.createServer(function(request, response) {
    var upload = fs.createWriteStream('uploaded');
    request.pipe(upload);
}).listen(8080);
