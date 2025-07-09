from flask_restful import Resource
from flask_login import logout_user

class LogoutResource(Resource):
    def post(self):
        logout_user()
        return {'message': 'Logged out successfully'}, 200