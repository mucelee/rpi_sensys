// Run the window
const ip = "localhost";

const {app, BrowserWindow} = require('electron');
let mainWindow;

function createWindow () {
  mainWindow = new BrowserWindow({width: 800, height: 600, show: false});
  mainWindow.loadFile('index.html');
  //mainWindow.webContents.openDevTools()
  mainWindow.on('closed', function () {
    mainWindow = null
  });
  mainWindow.once('ready-to-show', () => {
    mainWindow.show()
    listen();
    subscribe();
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    unsubAll();
    setTimeout(quit, 3000);
  }
});

function quit(){
  app.quit();
}

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow()
  }
});

//#region Listener

// Server to listen for published messages from CB
var objectPresence = false;

const http = require('http');
const port = 1234;

var subscriptionIds = new Set();

const requestHandler = (request, response) => {
  //console.log("request.headers: " + JSON.stringify(request.headers));
  let body = [];
  request.on('data', (chunk) => {
    body.push(chunk);
  }).on('end', () => {
    body = Buffer.concat(body).toString();
    var bodyJson = JSON.parse(body);
    subscriptionIds.add(bodyJson.subscriptionId);
    console.log("Json: " + JSON.stringify(bodyJson));
    objectPresence = bodyJson.data[0].objectPresence.value;;
    console.log("Value: " + objectPresence);
    mainWindow.webContents.send('objectPresence', objectPresence);
  });
}

const server = http.createServer(requestHandler)

function listen(){
  server.listen(port, (err) => {
    if (err) {
      return console.log('something bad happened', err)
    }
    console.log(`server is listening on ${port}`);
  });
}


//#endregion

//#region Subscription

// Send subscribe request
var fs = require('fs');
var subscription = JSON.parse(fs.readFileSync('subscription.json', 'utf8'));

const request = require('request');

function options(){
  return {
    method: 'POST',
    url: 'http://' + ip + ':1026/v2/subscriptions',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify(subscription)
  };
}

function subscribe(){
  request(options(), (err, res, body) => 
  {
    if (err) return console.log("err: " + err);
  })
  .on('response', function(response){
    console.log(response.statusCode);
    console.log("response.headers: " + JSON.stringify(response.headers));
  });
}

function unsubscribe(subId){
  console.log("unsubscribing: " + subId);
  request.delete(
    'http://' + ip + ':1026/v2/subscriptions/' + subId
  ).on('error', function(err){
    console.log(err);
  }).on('response', function(response){
    console.log(response.statusCode);
    console.log("unsubscribe response.headers: " + JSON.stringify(response.headers));
  });
}

function unsubAll(){
  console.log(subscriptionIds);
  var removed = new Set();
  for (var it = subscriptionIds.values(), subId = null; subId = it.next().value; ) {
    unsubscribe(subId);
    removed.add(subId);
  }
  subscriptionIds.forEach((id) => {
    subscriptionIds.delete(id);
  });
}

//#endregion

