from flask_restful import Resource, reqparse
from swagger import swagger

from models.user import User


class UserAddApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('lastName',
                        type=str,
                        required=True,
                        help='lastName is a mandatory field'
                        )
    parser.add_argument('firstName',
                        type=str,
                        required=True,
                        help='firstName is a mandatory field'
                        )
    parser.add_argument('emails',
                        action='append',
                        required=True,
                        help='emails are mandatory'
                        )
    parser.add_argument('phoneNumbers',
                        action='append',
                        required=True,
                        help='phoneNumbers are mandatory'
                        )

    @swagger.operation(
        notes='Creates a User',
        nickname='create User',
        parameters=[
            {
              "name": "body",
              "description": "User attributes",
              "required": True,
              "allowMultiple": False,
              "dataType": User.__name__,
              "paramType": "body"
            }
          ],
        responseMessages=[
            {
              "code": 201,
              "message": "Created"
            },
            {
              "code": 400,
              "message": "Invalid input"
            }
          ]
        )
    def post(self):
        request_body = UserAddApi.parser.parse_args()
        user = User(request_body['lastName'],
                    request_body['firstName'],
                    request_body['emails'],
                    request_body['phoneNumbers'])

        try:
            user.save()
        except:
            return {"message": "An error occurred while inserting the user."}
        return user.json(), 201


class UserGetDeleteApi(Resource):
    @swagger.operation(
        notes='Returns a User by Id',
        nickname='get User by Id',
        responseMessages=[
            {
              "code": 200,
              "message": "OK"
            },
            {
              "code": 404,
              "message": "Not found"
            }
          ]
        )
    def get(self, user_id):
        user = User.get_by_id(user_id)
        if user:
            return user.json()
        return {}, 404

    @swagger.operation(
        notes='Deletes a User',
        nickname='delete User',
        responseMessages=[
            {
              "code": 200,
              "message": "OK"
            }
          ]
        )
    def delete(self, user_id):
        user = User.get_by_id(user_id)
        if user:
            user.delete()
        return {'message': 'User deleted'}


class UserGetByNameApi(Resource):
    @swagger.operation(
        notes='Returns a User by Name',
        nickname='get User by name',
        responseMessages=[
            {
              "code": 200,
              "message": "OK"
            },
            {
              "code": 404,
              "message": "Not found"
            }
          ]
        )
    def get(self, lastName, firstName):
        user = User.get_by_name(lastName, firstName)
        if user:
            return user.json()
        return {}, 404
