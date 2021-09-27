from flask import Flask, request

App = Flask(__name__)

@App.route("/", methods=["GET"])
def endpoint_root():
    if (request.method == "GET"):
        return "Hello"


if __name__ == "__main__":
    App.run(port=50012, debug=True)