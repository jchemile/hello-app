from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/getmsg/', methods=['GET'])
def respond():
    name = request.args.get("name", None)
    print(f"got name{name}")
    response = {}

    if not name:
        response["ERROR"] = "No name found"
    elif str(name).isdigit():
        response["ERROR"] = "Name can't be numeric"
    else:
        response["MESSAGE"] = f"Welcome {name} to me first hello world app"

    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)

    if param:
        return jsonify({
            "Message": f"Welcome to me first hello world app",
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name"
        })

@app.route('/')
def index():
    return "<h1> Welcome to my first server !! </h1>"


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
