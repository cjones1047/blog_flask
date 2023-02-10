from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_posts_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_posts_response.raise_for_status()
blog_posts = blog_posts_response.json()


@app.route('/')
def home():
    global blog_posts

    return render_template("index.html", blog_posts=blog_posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    global blog_posts
    post = None
    for this_post in blog_posts:
        if this_post["id"] == post_id:
            post = this_post
            break

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
