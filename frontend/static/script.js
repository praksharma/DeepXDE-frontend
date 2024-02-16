function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

document.addEventListener('DOMContentLoaded', (event) => {
    // Automatically open the first tab
    var tablinks = document.getElementsByClassName("tablinks");
    if(tablinks.length > 0) {
        tablinks[0].click();
    }
    
    // Event listener for the check button
    var checkBtn = document.getElementById("checkBtn");
    if (checkBtn) {
        checkBtn.addEventListener("click", function() {
            fetch('/run-code')
                .then(response => response.json())
                .then(data => {
                    var versionTextbox = document.getElementById("versionTextbox");
                    versionTextbox.value = data.result;
                    // Instead of adding a class, we'll directly change the visibility here
                    versionTextbox.style.visibility = 'visible'; // Make the textbox visible
                })
                .catch(error => console.error('Error:', error));
        });
    }
});

