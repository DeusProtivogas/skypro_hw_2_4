from flask import Flask, request, render_template, send_from_directory
from functions import *

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    tags = get_tags()  # Получаю тэги при каждом переходе на главную страницу
    return render_template("index.html", tags=tags)


@app.route("/tag")
def page_tag():  # Предполагаю, что проверка будет ненужной, если переходить по тэгам с главной страницы
    tag = '#' + request.args.get("tag")
    found_posts = search_tags(tag)
    return render_template("post_by_tag.html", tag=tag[1:].title(), posts=found_posts)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    if request.method == "GET":  # Вывод формы для поста
        return render_template("post_form.html")
    # Иначе обрабатываю пост
    content = request.form.get("content")
    pic = request.files['picture']
    pic.save(UPLOAD_FOLDER + "/" + pic.filename)
    post = {
        "pic": UPLOAD_FOLDER + "/" + pic.filename,
        "content": content
    }
    add_post(post)
    return render_template("post_uploaded.html", post=post, upload=UPLOAD_FOLDER)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

