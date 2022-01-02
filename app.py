from flask import Flask, request, render_template, send_from_directory
from functions import *

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    tags = get_tags()
    return render_template("index.html", tags=tags)


@app.route("/tag")
def page_tag():
    tag = '#' + request.args.get("tag")
    print(tag)
    found_posts = search_tags(tag)
    return render_template("post_by_tag.html", tag=tag[1:].title(), posts=found_posts)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)

