const fs = require('fs');
const logMessage = 'This is a log file.\n';
// Append log every time script runs
fs.appendFileSync('log.txt', logMessage);

// synchronousfunction
function readFileBlocking() {
  const data = fs.readFileSync('log.txt', 'utf8');
  console.log('Blocking read:');
  console.log(data);
}

//async function
function readFileNonBlocking() {
  fs.readFile('log.txt', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('Non-blocking read:');
    console.log(data);
  });
}

//call both functions
readFileBlocking();
readFileNonBlocking();

//event loop demonstration
console.log('Start');

setTimeout(() => {
  console.log('setTimeout');
}, 0);

setImmediate(() => {
  console.log('setImmediate');
});

process.nextTick(() => {
  console.log('process.nextTick');
});
console.log('End');
