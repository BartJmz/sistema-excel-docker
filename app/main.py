from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return "Bienvenido a la app de procesamiento de Excel."

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        df = pd.read_excel(file)
        # Procesa el archivo Excel
        return df.to_html()  # Muestra el DataFrame como tabla HTML

if __name__ == '__main__':
    # Escucha en todas las interfaces en el puerto 5005
    app.run(host='0.0.0.0', port=5005)
