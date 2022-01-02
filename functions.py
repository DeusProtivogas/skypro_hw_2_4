import json


def get_tags():  # прохожу по списку постов, выделяю тэги
    with open("posts.json") as f:
        raw_json = f.read()
    posts = json.loads(raw_json)
    tags = []
    for post in posts:
        tags += [x[1:] for x in post['content'].split(" ") if x.startswith("#")]
    return set(tags)


def search_tags(tag):  # прохожу по постам и ищу все посты, содержащие переданный тэг
    with open("posts.json") as f:
        raw_json = f.read()
    posts = json.loads(raw_json)
    result = []
    for post in posts:
        if tag in post['content']:
            result.append(post)
    return result


def add_post(post):  # добавляю пост во файл posts.json
    with open("posts.json") as f:
        raw_json = f.read()

    posts = json.loads(raw_json)
    posts.append(post)
    raw_json = json.dumps(posts, ensure_ascii=False)

    with open("posts.json", "w") as f:
        f.write(raw_json)

