from flask import request
from flask_restful import Resource
from models import User
from extensions import db, bcrypt
from flask_login import login_user

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        print(f"username: {username}, password: {password}")

        if not username or not password:
            return {'message': 'Username and password required'}, 400
        
        user = User.query.filter_by(username=username).first()

        print(f"user: {user}")

        if not user:
            return {'message': 'Invalid credentials'}, 401

        valid_password = bcrypt.check_password_hash(user.password, password)
        print(f"valid_password: {valid_password}")

        if not valid_password:
            return {'message': 'Invalid credentials'}, 401
        
        login_user(user)
        
        return {'message': f'Welcome back, {username}!'}, 200