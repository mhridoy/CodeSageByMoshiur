function updateOutput() {
    const html = document.getElementById('html').value;
    const css = `<style>${document.getElementById('css').value}</style>`;
    const js = `<script>${document.getElementById('js').value}<\/script>`;
    const output = document.getElementById('output');
    const iframeDocument = output.contentDocument || output.contentWindow.document;

    iframeDocument.open();
    iframeDocument.write(html + css + js);
    iframeDocument.close();
}

// Optional: If you want to have a "Run Code" button that updates the iframe without submitting the form
document.getElementById('codeForm').addEventListener('submit', function(event) {
    event.preventDefault();
    updateOutput();
    this.submit();
});
function openInNewTab() {
    const form = document.createElement('form');
    form.target = '_blank';
    form.method = 'POST';
    form.action = '/new-tab';

    const htmlInput = document.createElement('input');
    htmlInput.type = 'hidden';
    htmlInput.name = 'html';
    htmlInput.value = document.getElementById('html').value;

    const cssInput = document.createElement('input');
    cssInput.type = 'hidden';
    cssInput.name = 'css';
    cssInput.value = document.getElementById('css').value;

    const jsInput = document.createElement('input');
    jsInput.type = 'hidden';
    jsInput.name = 'js';
    jsInput.value = document.getElementById('js').value;

    form.appendChild(htmlInput);
    form.appendChild(cssInput);
    form.appendChild(jsInput);
    
    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
}

function saveCode() {
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/save';

    ['html', 'css', 'js'].forEach(type => {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = type;
        input.value = document.getElementById(type).value;
        form.appendChild(input);
    });

    document.body.appendChild(form);
    form.submit();
}






document.addEventListener('DOMContentLoaded', function() {
    // Event listener for all insert buttons
    document.querySelectorAll('.insert-btn').forEach(button => {
        button.addEventListener('click', function() {
            const imageUrl = this.getAttribute('data-url');
            insertImage(imageUrl);
        });
    });
});

function insertImage(url) {
    const editor = document.getElementById('html'); // Ensure you have an element with ID 'html' for your HTML editor
    editor.value += `<img src="${url}" alt="Image">`; // Append an img tag to the editor content
}
