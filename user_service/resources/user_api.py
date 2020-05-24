from flask_restful import Resource, reqparse

from models.user import User
from models.email import Email
from models.phone import Phone


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
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='mail is mandatory'
                        )
    parser.add_argument('phoneNumber',
                        type=str,
                        required=True,
                        help='Phone number is mandatory'
                        )

    def post(self):
        request_body = UserAddApi.parser.parse_args()
        user = User(request_body['lastName'], request_body['firstName'])

        try:
            user.save()
            user_id = user.json()['id']
            email = Email(request_body['email'], user_id)
            email.save()
            phone = Phone(request_body['phoneNumber'], user_id)
            phone.save()
        except:
            return {"message": "An error occurred while inserting the user."}
        return user.json(), 201


class UserGetDeleteApi(Resource):
    def get(self, user_id):
        user = User.get_by_id(user_id)
        if user:
            return user.json()
        return {}, 404

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
        return {}, 404
