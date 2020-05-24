from flask_restful import Resource, reqparse

from models.phone import Phone


class PhoneAddApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('number',
                        type=str,
                        required=True,
                        help='Phone number is mandatory'
                        )

    def post(self, user_id):
        request_body = PhoneAddApi.parser.parse_args()
        phone = Phone(number=request_body['number'], user_id=user_id)

        try:
            phone.save()
        except:
            return {"message": "An error occurred while inserting the phone number."}, 400
        return phone.json(), 201


class PhoneUpdateApi(Resource):
    def put(self, phone_id):
        request_body = PhoneAddApi.parser.parse_args()
        phone = Phone.get_by_id(phone_id)

        if phone is None:
            return {'number': request_body['number']}
        else:
            phone.number = request_body['number']
            phone.save()

        return phone.json()


class PhoneApi(Resource):
    def get(self, phone_id):
        phone = Phone.get_by_id(phone_id)
        if phone:
            return phone.json()
        return {}, 404
