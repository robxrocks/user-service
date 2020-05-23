from flask_restful import Resource, reqparse

from models.user import User


class UserAddApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('lastName',
                        type=str,
                        required=True,
                        help='lastName is mandatory'
                        )
    parser.add_argument('firstName',
                        type=str,
                        required=True,
                        help='firstName is mandatory'
                        )

    def post(self):
        request_body = UserAddApi.parser.parse_args()
        user = User(**request_body)

        try:
            user.save()
        except:
            return {"message": "An error occurred while inserting the item."}
        return user.json(), 201


class UserGetDeleteApi(Resource):
    def get(self, user_id):
        user = User.get_by_id(user_id)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        user = User.get_by_id(user_id)
        if user:
            user.delete()
        return {'message': 'User deleted'}


class UserGetByNameApi(Resource):
    def get(self, lastName, firstName):
        user = User.get_by_name(lastName, firstName)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404
