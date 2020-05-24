from flask_restful import Resource, reqparse

from models.email import Email


class EmailAddApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='mail is mandatory'
                        )

    def post(self, user_id):
        request_body = EmailAddApi.parser.parse_args()
        email = Email(mail=request_body['email'], user_id=user_id)

        try:
            email.save()
        except:
            return {"message": "An error occurred while inserting the email."}, 400
        return email.json(), 201


class EmailApi(Resource):
    def get(self, email_id):
        email = Email.get_by_id(email_id)
        if email:
            return email.json()
        return {}, 404
