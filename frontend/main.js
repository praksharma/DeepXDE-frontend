const { app, BrowserWindow,ipcMain, ipcRenderer } = require('electron');
const { spawn } = require('child_process');

// Disable GPU Hardware Acceleration
app.disableHardwareAcceleration();

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow;

function createWindow () {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      enableRemoteModule: true,
      contextIsolation: false,
    }
  });

  // and load the index.html of the app.
  mainWindow.loadFile('index.html');

  // Open the DevTools.
  // mainWindow.webContents.openDevTools();

  // Emitted when the window is closed.
  mainWindow.on('closed', function () {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    mainWindow = null
  });
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow);

ipcMain.on('run-code-request', (event) => {
  const pythonProcess = spawn('python', ['static/version_check.py']);
  let pythonData = '';

  pythonProcess.stdout.on('data', (data) => {
      pythonData += data.toString();
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      event.reply('run-code-response', pythonData);
  });
});

// log error
// Event listener for running Python code
// ipcMain.on('run-code-request', (event) => {
//   // Spawn a Python process
//   const pythonProcess = spawn('python', ['static/version_check.py']);

//   // Event listener for Python process output
//   pythonProcess.stdout.on('data', (data) => {
//       console.log(`Python output: ${data}`);
//       // Send Python output to the renderer process
//       event.reply('run-code-response', data.toString());
//   });

//   // Event listener for Python process error
//   pythonProcess.stderr.on('data', (data) => {
//       console.error(`Python error: ${data}`);
//   });

//   // Event listener for Python process exit
//   pythonProcess.on('close', (code) => {
//       console.log(`Python script exited with code ${code}`);
//   });
// });