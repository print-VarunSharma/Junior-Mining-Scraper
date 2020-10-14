from flask import Flask, render_template
from flask.templating import render_template_string
from autopan import send_email
# https://realpython.com/flask-by-example-part-1-project-setup/ for deploying with heroku later.
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template("index.html", title="home")

@app.route("/random")
def about():
    return "All about Flask"

@app.route("/goldpan")
def goldpan():
    return render_template("goldpan.html", title="Pan your Data")

@app.route('/submit_email', methods=['POST'])
def submit_email():
    projectpath = request.form['projectFilepath']
    # your code
    # return a response

# <form action="{{ url_for('submit_email') }}" method="post">
#     <input type="text" name="projectFilepath">
#     <input type="submit">
# </form>

@app.route('/send_email', methods=['POST'])
def send_email(sub, msg, receivers):
    sub = "Test from flask"
    msg = 'This is a test email from flask' # Customize based on user input
    receivers = ['varundevasharma@gmail.com', 'varuns.pybot@gmail.com']
    return 'done'

if __name__ == "__main__":
    app.run(debug=True)