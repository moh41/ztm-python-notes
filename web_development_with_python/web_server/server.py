from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/<username>")
def hello_user(username=None):
    return render_template("user.html", name=username)

@app.route("/<username>/<int:post_id>")
def hello_user_post_id(username=None, post_id=None):
    return render_template("user.html", name=username, post_id=post_id)