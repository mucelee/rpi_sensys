// Boilerplate to run the window
const {app, BrowserWindow} = require('electron')
let mainWindow

function createWindow () {
  mainWindow = new BrowserWindow({width: 800, height: 600})
  mainWindow.loadFile('index.html')
  // mainWindow.webContents.openDevTools()
  mainWindow.on('closed', function () {
    mainWindow = null
  })
}

app.on('ready', createWindow)

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow()
  }
})

// Our code
// Server to listen for published messages from CB
const http = require('http')
const port = 1234

const requestHandler = (request, response) => {
  //console.log(request.url)
  console.log("request.headers: " + JSON.stringify(request.headers));
  console.log("request.body: " + JSON.stringify(request.body));
}

const server = http.createServer(requestHandler)

server.listen(port, (err) => {
  if (err) {
    return console.log('something bad happened', err)
  }

  console.log(`server is listening on ${port}`)
})

// Send subscribe request
var fs = require('fs');
var subscription = JSON.parse(fs.readFileSync('subscription.json', 'utf8'));

const request = require('request');

var options = {
  method: 'POST',
  url: 'http://192.168.0.110:1026/v2/subscriptions',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(subscription)
};
 
request(options, (err, res, body) => 
{
  if (err) return console.log("err: " + err);
  console.log("body.url: " + body.url);
  console.log("body.explanation: " + body.explanation);
})
.on('response', function(response){
  console.log(response.statusCode);
  console.log("response.headers: " + JSON.stringify(response.headers));
  console.log("response.body: " + JSON.stringify(response.body));
})
.on('data', function(data) {
  console.log("data: " + data);
});


// subscription example
/* {
  "entities": [
      {
          "type": "Sensor",
          "id": "san_2_ir_sensor"
      }
  ],
  "attributes": [
      "objectPresence"
  ],
  "reference": "http://192.168.0.103:5555",
  "duration": "P1D",
  "notifyConditions": [
      {
          "type": "ONCHANGE",
          "condValues": [
              "objectPresence"
          ]
      }
  ],
  "throttling": "PT2S"
} */
	
