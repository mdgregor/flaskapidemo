from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/math/<int:num_one>/<int:num_two>/<string:method>")
def do_random_math(num_one, num_two, method):
    solution = {
        "+": add(num_one, num_two),
        "-": subtract(num_one, num_two),
        "*": multiply(num_one, num_two),
        "/": divide(num_one, num_two)
    }.get(method)

    return jsonify({"num_one": num_one, "num_two": num_two, "result": solution})


@app.route("/")
def default():
    return "Default Route"


def add(num_one, num_two):
    return num_one + num_two


def subtract(num_one, num_two):
    return num_one - num_two


def multiply(num_one, num_two):
    return num_one * num_two


def divide(num_one, num_two):
    return num_one / num_two


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
