import json


def get_posts_all():
    with open('data/data.json', "r", encoding='utf-8') as data:
        return json.load(data)


def get_posts_by_user(user_name):
    posts = get_posts_all()
    return [post for post in posts if post["poster_name"] == user_name]


def get_comments_by_post_id(post_id):
    with open('data/comments.json', "r", encoding='utf-8') as data:
        comments = json.load(data)
    return [comment for comment in comments if comment["post_id"] == post_id]


def search_for_posts(query):
    posts = get_posts_all()
    return [post for post in posts if query.lower() in post["content"].lower()]


def get_post_by_pk(pk):
    posts = get_posts_all()
    return [post for post in posts if post["pk"] == pk][0]


def correct_comment(length):
    if 5 > length % 10 > 1 and length // 10 != 1:
        return 'комментария'
    elif length % 10 == 1 and length // 10 != 1:
        return 'комментарий'
    else:
        return 'комментариев'


def get_posts_by_tag(tag):
    posts = get_posts_all()
    return [post for post in posts if '#' + tag in post['content']]


def get_bookmarks_all():
    with open('data/bookmarks.json', "r", encoding='utf-8') as data:
        return json.load(data)


def add_bm(post_id):
    bookmarks = get_bookmarks_all()
    posts = get_posts_all()
    bookmarks.extend([post for post in posts if post["pk"] == post_id and post not in bookmarks])
    with open('data/bookmarks.json', "w", encoding='utf-8') as data:
        json.dump(bookmarks, data, indent=2, ensure_ascii=False)


def delete_bm(post_id):
    bookmarks = get_bookmarks_all()
    with open('data/bookmarks.json', "w", encoding='utf-8') as data:
        json.dump([post for post in bookmarks if post['pk'] != post_id], data, indent=2, ensure_ascii=False)
