from flask import Flask, render_template
# https://realpython.com/flask-by-example-part-1-project-setup/ for deploying with heroku later.
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)