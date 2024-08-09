# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requisitos e instalar dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido del directorio src/ al directorio de trabajo
COPY src/ /app/

# Exponer el puerto en el que la aplicación va a correr
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
