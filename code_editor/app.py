from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
import uuid

UPLOAD_FOLDER = 'static/upload'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB
app.secret_key = 'your_secret_key_here'

# In-memory storage for demonstration purposes
code_storage = {}

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('editor.html', files=files)

@app.route('/save', methods=['POST'])
def save():
    unique_id = str(uuid.uuid4())
    code_storage[unique_id] = {
        'html': request.form['html'],
        'css': request.form['css'],
        'js': request.form['js']
    }
    return redirect(url_for('view', unique_id=unique_id))

@app.route('/view/<unique_id>')
def view(unique_id):
    code = code_storage.get(unique_id)
    if code:
        return render_template('view.html', code=code)
    return 'Code not found', 404

@app.route('/new-tab', methods=['POST'])
def new_tab():
    html_content = request.form['html']
    css_content = request.form['css']
    js_content = request.form['js']
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Open in New Tab</title>
        <style>{css_content}</style>
    </head>
    <body>
        {html_content}
        <script>{js_content}</script>
    </body>
    </html>
    """
    return full_html


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded')
    else:
        flash('Invalid file format or file is too large.')
    return redirect(url_for('index'))

@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
