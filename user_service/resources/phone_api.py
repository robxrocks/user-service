from flask_restful import Resource, reqparse
from models.phone import Phone
from swagger import swagger


class PhoneAddApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('number',
                        type=str,
                        required=True,
                        help='Phone number is mandatory'
                        )

    @swagger.operation(
        notes='Creates a Phone data',
        nickname='create Phone',
        parameters=[
            {
              "name": "body",
              "description": "Phone attributes",
              "required": True,
              "allowMultiple": False,
              "dataType": Phone.__name__,
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
        request_body = PhoneAddApi.parser.parse_args()
        phone = Phone(number=request_body['number'], user_id=user_id)

        try:
            phone.save()
        except:
            return {"message": "An error occurred while inserting the phone number."}, 400
        return phone.json(), 201


class PhoneUpdateApi(Resource):
    @swagger.operation(
        notes='Updates a Phone data',
        nickname='update Phone',
        parameters=[
            {
              "name": "body",
              "description": "Phone attributes",
              "required": True,
              "allowMultiple": False,
              "dataType": Phone.__name__,
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
    def put(self, phone_id):
        request_body = PhoneAddApi.parser.parse_args()
        phone = Phone.get_by_id(phone_id)

        if phone is None:
            return {'number': request_body['number']}
        else:
            phone.number = request_body['number']
            phone.save()

        return phone.json()
