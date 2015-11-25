var fs = require('fs');
var http = require('http');

// Creating a server
http.createServer(function(request, response) {
    // Creating a Write Stream to save the file
    var upload = fs.createWriteStream('uploaded');

    // Getting the total size
    var fileBytes = request.headers['content-length'];

    // How many bytes were uploaded?
    var uploadedBytes = 0;

    // Updating the progress!
    request.on('readable', function() {
        var chunk = null;
        while(null !== (chunk = request.read())) {
            uploadedBytes += chunk.length;
            var progress = (uploadedBytes / fileBytes) * 100;
            response.write("Progress: " + parseInt(progress, 10) + "%\n");
        }
    });

    // Piping the request to the stream
    request.pipe(upload);

    // Listening to the 'end' event on the request
    request.on('end', function() {
        // Writing that it was done
        console.log('uploaded');
    })
}).listen(8080);
