from flask import Flask, request, render_template

application = Flask(__name__)



@application.route("/", methods = ["GET"])

def predict():
    return "this is a sample application"
if __name__ == "__main__":
    application.run(debug=True)
