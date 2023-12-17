// Initialize Ace Editor
var editor = ace.edit("editor");
editor.setTheme("ace/theme/github");
editor.session.setMode("ace/mode/python");

document.getElementById("run-btn").addEventListener("click", function() {
    // Fetch code from the editor
    var code = editor.getValue();

    // Mock code execution and display output
    // Replace this part with actual code execution logic
    document.getElementById("output").innerText = "Executing Python code:\n" + code;
});
