# Dockerfile

# Usa una imagen de Python
FROM python:3.9-slim

# Configura el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY app/ /app/

# Instala las dependencias desde el requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecutará la app
EXPOSE 5000

# Comando para ejecutar la app de Flask
CMD ["python", "main.py"]
