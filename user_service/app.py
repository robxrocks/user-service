from flask import Flask
from flask_restful import Api, Resource
from db import db
from resources.user_api import UserAddApi, UserGetDeleteApi, UserGetByNameApi
from resources.email_api import EmailAddApi, EmailApi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserAddApi, '/user')
api.add_resource(UserGetDeleteApi, '/user/<int:user_id>')
api.add_resource(UserGetByNameApi, '/user/lastname/<string:lastName>/firstname/<string:firstName>')

api.add_resource(EmailAddApi, '/user/<int:user_id>/email')


# Remove this endpoint when finished
api.add_resource(EmailApi, '/email/<int:email_id>')


if __name__ == '__main__':
    db.init_app(app)

    # Ensure FOREIGN KEY for sqlite3
    if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
        def _fk_pragma_on_connect(dbapi_con, con_record):  # noqa
            dbapi_con.execute('pragma foreign_keys=ON')

        with app.app_context():
            from sqlalchemy import event
            event.listen(db.engine, 'connect', _fk_pragma_on_connect)

    app.run(debug=True)
