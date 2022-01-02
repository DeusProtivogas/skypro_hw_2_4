import json


def get_tags():
    with open("posts.json") as f:
        raw_json = f.read()
    posts = json.loads(raw_json)
    tags = []
    chars_to_strip = "#!?;:.,&*()"
    for post in posts:
        tags += [x.strip(chars_to_strip) for x in post['content'].split(" ") if x.startswith("#")]
    return set(tags)



# print(get_tags())
