from flask import request
from flask_restful import Resource
from models import User
from extensions import bcrypt, db
# from app import bcrypt

class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        raw_password = data.get('password')

        if not username or not raw_password:
            return {'message': 'Username and password are required'}, 400
        
        if User.query.filter_by(username=username).first():
            return {'message': 'Username already exists'}, 400
        
        hashed_pw = bcrypt.generate_password_hash(raw_password).decode('utf-8')
        new_user = User(username=username, password=hashed_pw)

        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201