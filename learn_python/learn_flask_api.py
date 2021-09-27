from flask import Flask, request
from flask_cors import CORS
import argparse
import logging

from markdown import markdown

App = Flask(__name__)
CORS(App)

port_no = 50055

@App.route("/", methods=["GET"])
def endpoint_root():
    if (request.method == "GET"):
        return f"Hello from api {__name__} running on port {port_no}"

@App.route("/help", methods=["GET"])
def endpoint_help():
    if (request.method == "GET"):
        return f"<h1> help </h1> <a> </a>"


if __name__ == '__main__':
    App.run(port=port_no, debug=True)