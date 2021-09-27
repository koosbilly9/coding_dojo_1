from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def return_root():
    if request.method == "GET":
        return(jsonify(response1='Hello World 2'))
    else:
        return Response(status=404)

@app.route("/help", methods = ['GET'])
def return_help():
    return "<h1> End points </h1>" \
           "<ul>" \
           "<li> /help - shows endpoints  </li>" \
           "</ul> "

@app.route("/food/<food>", methods = ['GET'])
def return_food(food):
    if request.method == "GET":
         return jsonify({'food':food, 'fat':155})

if __name__ == "__main__":
    app.run(port=50012, debug=True)