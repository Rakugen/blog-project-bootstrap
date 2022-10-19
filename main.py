from flask import Flask, render_template
import requests

API_ENDPOINT = "https://api.npoint.io/caeda41b069d168022ac"
app = Flask(__name__)
all_posts = []

response = requests.get(url=API_ENDPOINT).json()
# Creating list for all posts to be later used in directing to individual post html pages
for post in response:
    all_posts.append(post)


# Home route that uses all_posts list to display titles/subtitles/author/date with link to its post page
@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


# Contacts page
@app.route('/contact')
def contact():
    return render_template("contact.html")


# About page
@app.route('/about')
def about():
    return render_template("about.html")


# Individual posts page that takes the post that was clicked from index.html and generates its own page
@app.route('/post/<num>')
def get_post(num):
    found_post = None
    # Looks through each post in all_posts for matching id then passes into a new html
    for current_post in all_posts:
        if current_post["id"] == int(num):
            found_post = current_post
    return render_template("post.html", post=found_post)


if __name__ == "__main__":
    app.run(debug=True)
