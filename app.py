from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello World!")

@app.route("/about")
def about_us():
    return render_template("about.html", title="About Us")