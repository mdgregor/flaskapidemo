from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/math/string:method>/<int:num_one>/<int:num_two>")
def do_random_math(method, num_one, num_two):
    solution = {
        "add": add(num_one, num_two),
        "subtract": subtract(num_one, num_two),
        "multiply": multiply(num_one, num_two),
        "divide": divide(num_one, num_two)
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
    app.run(host='0.0.0.0', debug=True)
