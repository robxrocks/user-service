from flask import Flask
from flask_restful import Api, Resource
from db import db
from resources.user_api import UserAddApi, UserGetDeleteApi, UserGetByNameApi

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


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
