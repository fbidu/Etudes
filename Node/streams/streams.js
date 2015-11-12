var http = require('http');

http.createServer(function(request, response) {
    response.writeHead(200);
    request.on('readable', function() {
        var chunk = null;
        while ((chunk = request.read()) !== null) {
            console.log(chunk.toString());
        }
    });

    request.on('end', function() {
        response.end();
        console.log('Request ended');
    });
}).listen(8080);
