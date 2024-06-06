from flask import Flask
from flask_restx import Api, Resource, Namespace, reqparse
from http import HTTPStatus

app = Flask(__name__)
api = Api(app)

test_ns = Namespace(name="test", description="Flask-RESTx Practice")


@test_ns.route("/")
class Test(Resource):
    @staticmethod
    def get():
        return "Welcome, you're testing a REST API using Flask-RESTx!", HTTPStatus.OK

    @staticmethod
    def post():
        return "Welcome, you're testing a REST API using Flask-RESTx!", HTTPStatus.OK


api.add_namespace(test_ns, path="/test")

hello_parser = reqparse.RequestParser()
hello_parser.add_argument("name", help="Please enter a name")

hello_ns = Namespace(name="hello", description="This is the hello namespace")


@hello_ns.route("/")
class Hello(Resource):
    @staticmethod
    @hello_ns.doc(parser=hello_parser)
    def get():
        args = hello_parser.parse_args()
        name = args["name"]
        return f"Hello {name}!"


api.add_namespace(hello_ns, path="/hello")

if __name__ == '__main__':
    app.run(debug=True)
