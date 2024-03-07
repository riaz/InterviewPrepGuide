var http = require('http');

port = 8080
/*
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('This is a very simple nodejs server');
    console.log('Hey there');
}).listen(8080);
*/

// achieveing the same differently

var server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type','text/plain');
    res.end('Hello World\n');
})

server.listen(port, () => {
    console.log(`erver is running in the port ${port}`)
})