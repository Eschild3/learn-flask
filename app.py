from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/hello/", methods=["GET", "POST"])
def welcome():
    return "Hello World!"


@app.route("/increment/<int:number>/", methods=["GET"])
def increment(number):
    return f"Incremented Number: {str(number + 1)}"


@app.route("/greeting/<string:name>/", methods=["GET"])
def greet(name):
    return f"Hello {name}!"


@app.route("/person/", methods=["GET"])
def person():
    return jsonify({"firstName": "EJ", "lastName": "Schildnecht"})


@app.route("/numbers/<int:length>/", methods=["GET"])
def numbers(length):
    return jsonify(list(range(length)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=105)
