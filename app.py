from flask import Flask
from models import db

app = Flask(__name__)

# Configuración de la base de datos (ajusta según tus necesidades)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@db:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
