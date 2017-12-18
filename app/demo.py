from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/math/")
def math():
    return "enter item /math/add/4/5"


@app.route("/math/<string:method>/<int:num_one>/<int:num_two>")
def do_math(method, num_one, num_two):
    try:
        solution = {
            "add": add(num_one, num_two),
            "subtract": subtract(num_one, num_two),
            "multiply": multiply(num_one, num_two),
            "divide": divide(num_one, num_two)
        }.get(method)

        return jsonify({"num_one": num_one, "num_two": num_two, "result": solution})
    except Exception as e:
        return str(e)


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
    app.run(host='0.0.0.0', port=5000)
