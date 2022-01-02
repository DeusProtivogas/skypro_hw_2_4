import json


def get_tags():
    with open("posts.json") as f:
        raw_json = f.read()
    posts = json.loads(raw_json)
    tags = []
    for post in posts:
        tags += [x[1:] for x in post['content'].split(" ") if x.startswith("#")]
    return set(tags)


def search_tags(tag):
    with open("posts.json") as f:
        raw_json = f.read()
    posts = json.loads(raw_json)
    result = []
    for post in posts:
        if tag in post['content']:
            result.append(post)
    print(result)
    return result



print(get_tags())
