from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    blog_posts_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_posts_response.raise_for_status()
    blog_posts = blog_posts_response.json()

    return render_template("index.html", blog_posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)
