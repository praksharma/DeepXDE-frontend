const { ipcRenderer } = window.require('electron');

// Manage tabs  
function openTab(tabName) {
    // Hide all tab contents
    var tabcontents = document.getElementsByClassName("tabcontent");
    for (var i = 0; i < tabcontents.length; i++) {
        tabcontents[i].style.display = "none";
    }

    // Remove 'active' class from all tab links
    var tablinks = document.getElementsByClassName("tablinks");
    for (var i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
    }

    // Show the selected tab content
    var selectedTab = document.getElementById(tabName);
    if (selectedTab) {
        selectedTab.style.display = "block";

        // Add 'active' class to the clicked tab link
        event.currentTarget.classList.add("active");
    }
}

// VERSION CHECK //

// Modified event listener for the check button
var checkBtn = document.getElementById("checkBtn");
if (checkBtn) {
    checkBtn.addEventListener("click", function() {
        ipcRenderer.send('run-code-request');
    });
}

// Listen for the response from python version checker
ipcRenderer.on('run-code-response', (event, data) => {
    var versionTextbox = document.getElementById("versionTextbox");
    versionTextbox.value = data; // Check if 'result' is the correct property name
    versionTextbox.style.visibility = 'visible'; // Make the textbox visible
});

// PROJECT FILE BROWSER
// Open the file browser
document.getElementById('browseBtn').addEventListener('click', () => {
    ipcRenderer.send('open-file-dialog');
});
// Listen for the response from the file browser
ipcRenderer.on('selected-directory', (event, path) => {
    document.getElementById('projectPath').value = path;
});
