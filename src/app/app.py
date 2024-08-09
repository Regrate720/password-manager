from flask import Flask, request, jsonify
from models import db, Password
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/password_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/passwords', methods=['GET', 'POST'])
def manage_passwords():
    if request.method == 'POST':
        data = request.json
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_password = Password(site=data['site'], username=data['username'], password=hashed_password)
        db.session.add(new_password)
        db.session.commit()
        return jsonify({'message': 'Password added'}), 201
    else:
        passwords = Password.query.all()
        return jsonify([{'site': p.site, 'username': p.username, 'password': p.password} for p in passwords])

@app.route('/passwords/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_password(id):
    password = Password.query.get_or_404(id)
    
    if request.method == 'GET':
        response = {
            'site': password.site,
            'username': password.username,
            'password': password.password
        }
        return jsonify(response)
    
    elif request.method == 'PUT':
        data = request.json
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        password.site = data['site']
        password.username = data['username']
        password.password = hashed_password
        db.session.commit()
        return jsonify({'message': 'Password updated'}), 200
    
    elif request.method == 'DELETE':
        db.session.delete(password)
        db.session.commit()
        return jsonify({'message': 'Password deleted'}), 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000)
