from flask_login import current_user
from flask_restful import Resource

class CheckSessionResource(Resource):
    def get(self):
        if current_user.is_authenticated:
            return {'authenticated': True, 'username': current_user.username}, 200
        else:
            return {'authenticated': False}, 401