from flask import Flask, render_template
from flask.templating import render_template_string
# https://realpython.com/flask-by-example-part-1-project-setup/ for deploying with heroku later.
app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')

@app.route("/")
def home():
    return render_template_string('Hello World')


if __name__ == "__main__":
    app.run(debug=True)