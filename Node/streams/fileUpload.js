var fs = require('fs');
var http = require('http');

// Creating a server
http.createServer(function(request, response) {
    // Creating a Write Stream to save the file
    var upload = fs.createWriteStream('uploaded');

    // Piping the request to the stream
    request.pipe(upload);

    // Listening to the 'end' event on the request
    request.on('end', function() {
        // Writing that it was done
        console.log('uploaded');
    }
}).listen(8080);
