# app/main.py

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar_archivo():
    # Aquí procesaríamos el archivo de Excel
    file = request.files['file']
    df = pd.read_excel(file)

    # Ejemplo de proceso: mostrar los primeros 5 registros
    return df.head().to_html()

if __name__ == '__main__':
    app.run(debug=True)
