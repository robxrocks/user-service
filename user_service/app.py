from db import db
from flask import Flask
from flask_restful import Api
from resources.email_api import EmailAddApi, EmailUpdateApi
from resources.phone_api import PhoneAddApi, PhoneUpdateApi
from resources.user_api import UserAddApi, UserGetDeleteApi, UserGetByNameApi
from swagger import swagger

app = Flask(__name__)
# TODO move database uri to env variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
api = swagger.docs(Api(app), apiVersion='0.1', description="API docs for user-service")
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserAddApi, '/user')
api.add_resource(UserGetDeleteApi, '/user/<int:user_id>')
api.add_resource(UserGetByNameApi, '/user/<string:lastName>/<string:firstName>')

api.add_resource(EmailAddApi, '/user/<int:user_id>/email')
api.add_resource(EmailUpdateApi, '/email/<int:email_id>')

api.add_resource(PhoneAddApi, '/user/<int:user_id>/phone')
api.add_resource(PhoneUpdateApi, '/phone/<int:phone_id>')


if __name__ == '__main__':
    # Ensure FOREIGN KEY for sqlite3
    if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
        def _fk_pragma_on_connect(dbapi_con, con_record):  # noqa
            dbapi_con.execute('pragma foreign_keys=ON')

        with app.app_context():
            from sqlalchemy import event
            event.listen(db.engine, 'connect', _fk_pragma_on_connect)

    app.run(debug=True)
