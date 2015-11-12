var fs = require('fs');

var file = fs.createReadStream('doge.png');
var newFile = fs.createWriteStream('doge_copy.png');

file.pipe(newFile);
