from flask import Flask
from flask_restx import Api, Resource, Namespace
from http import HTTPStatus

app = Flask(__name__)
api = Api(app)

ns = Namespace(name="test", description="Flask-RESTx Practice")

@ns.route("/")
class Welcome(Resource):
    def get(self):
        return "Welcome, you're testing a REST API using Flask-RESTx!", HTTPStatus.OK

    def post(self):
        return "Welcome, you're testing a REST API using Flask-RESTx!", HTTPStatus.OK

api.add_namespace(ns, path='/test')

if __name__ == '__main__':
    app.run(debug=True)
