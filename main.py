from flask import Flask, render_template
import requests

API_ENDPOINT = "https://api.npoint.io/caeda41b069d168022ac"
app = Flask(__name__)

all_posts = requests.get(url=API_ENDPOINT).json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post')
def get_post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
