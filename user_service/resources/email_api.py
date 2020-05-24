from flask_restful import Resource, reqparse
from swagger import swagger

from models.email import Email


class EmailAddApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('mail',
                        type=str,
                        required=True,
                        help='mail is mandatory'
                        )

    @swagger.operation(
        notes='Creates an Email',
        nickname='create Email',
        parameters=[
            {
              "name": "body",
              "description": "Email attributes",
              "required": True,
              "allowMultiple": False,
              "dataType": Email.__name__,
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
    def post(self, user_id):
        request_body = EmailAddApi.parser.parse_args()
        email = Email(mail=request_body['mail'], user_id=user_id)

        try:
            email.save()
        except:
            return {"message": "An error occurred while inserting the email."}, 400
        return email.json(), 201


class EmailUpdateApi(Resource):
    @swagger.operation(
        notes='Updated an Email',
        nickname='update Email',
        parameters=[
            {
              "name": "body",
              "description": "Email attributes",
              "required": True,
              "allowMultiple": False,
              "dataType": Email.__name__,
              "paramType": "body"
            }
          ],
        responseMessages=[
            {
              "code": 200,
              "message": "OK"
            }
          ]
        )
    def put(self, email_id):
        request_body = EmailAddApi.parser.parse_args()
        email = Email.get_by_id(email_id)

        if email is None:
            return {'mail': request_body['mail']}
        else:
            email.mail = request_body['mail']
            email.save()

        return email.json()
