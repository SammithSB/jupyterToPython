from flask import Flask, request, render_template, send_from_directory
import nbformat
from nbconvert import PythonExporter
import os
import uuid
import re
import textwrap

app = Flask(__name__)
app.config['OUTPUT_FOLDER'] = 'output'

@app.route('/')
def index():
    return render_template('index.html', code=None)

@app.route('/convert', methods=['POST'])
def convert_ipynb_to_py():
    file = request.files['file']
    if file and file.filename.endswith('.ipynb'):
        nb = nbformat.reads(file.read(), as_version=4)
        exporter = PythonExporter()
        source_code, _ = exporter.from_notebook_node(nb)

        # Clean up the source code to remove Jupyter cell references
        clean_code = '\n'.join(line for line in source_code.splitlines()
                                if not line.startswith('# In['))
        # Remove excessive blank lines
        clean_code = re.sub(r'\n\s*\n', '\n\n', clean_code)

        # Optionally, adjust indentation (uncomment the following line if needed)
        # clean_code = textwrap.dedent(clean_code).strip()

        # Generate a unique filename for output
        output_filename = str(uuid.uuid4()) + '.py'
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        with open(output_path, 'w') as output_file:
            output_file.write(clean_code)

        return render_template('index.html', code=clean_code, filename=output_filename)
    return render_template('index.html', error="Invalid file format or no file selected")

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    app.run(debug=True)
