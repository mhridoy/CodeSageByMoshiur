from flask import Flask, render_template, request, redirect, url_for
import uuid
import os

app = Flask(__name__)

# In-memory storage for demonstration purposes
# In a real application, consider using a database
code_storage = {}

@app.route('/')
def index():
    return render_template('editor.html')

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
        <title>Output</title>
        <style>{css_content}</style>
    </head>
    <body>
        {html_content}
        <script>{js_content}</script>
    </body>
    </html>
    """
    return full_html

if __name__ == '__main__':
    app.run(debug=True)
