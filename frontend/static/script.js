document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("checkBtn").addEventListener("click", function() {
        fetch('/run-code')  // Make sure this matches your Flask route.
            .then(response => response.json())
            .then(data => {
                document.getElementById("readonlyTextbox").value = data.result;
                document.getElementById("readonlyTextbox").style.display = "block";
            })
            .catch(error => console.error('Error:', error));
    });
});

