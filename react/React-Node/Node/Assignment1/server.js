const http = require('http');
const helper = require('./helper');

// Log message from helper module
console.log(helper.getMessage());

// Create the server
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Welcome to Node.js!');
});

//server listen on port 3000
server.listen(3000, () => {
  console.log('Server is running on port 3000');
});
