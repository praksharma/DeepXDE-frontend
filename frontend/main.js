const { app, BrowserWindow, ipcMain, ipcRenderer, dialog } = require('electron'); // List of all permissions
const { spawn } = require('child_process'); // allows reading python file's stdout
const os = require('os'); // import the OS module for file browser


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

// Read input from python file
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

// Open file dialog to browse project directory
ipcMain.on('open-file-dialog', (event) => {
  dialog.showOpenDialog(mainWindow, {
    properties: ['openDirectory'],
    defaultPath: os.homedir() // Use the os module to get the home directory
  }).then(result => {
    if (!result.canceled && result.filePaths.length > 0) {
      // Send the selected directory path back to the renderer process
      event.reply('selected-directory', result.filePaths[0]);
    }
  }).catch(err => {
    console.log(err);
  });
});

