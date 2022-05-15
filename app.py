from flask import Flask, render_template, request, redirect
from api import api
from utils import *

app = Flask(__name__)
app.register_blueprint(api)


@app.route('/')
def index():
    return render_template('index.html', posts=get_posts_all(), bookmarks=get_bookmarks_all())


@app.route('/search/')
def search():
    query = request.values.get('s')
    return render_template('search.html', posts=search_for_posts(query))


@app.route('/posts/<int:post_id>')
def get_post(post_id):
    comments = get_comments_by_post_id(post_id)
    post = get_post_by_pk(post_id)
    string = correct_comment(len(comments))
    return render_template('post.html', post=post, comments=comments, str=string)


@app.route('/users/<username>')
def get_user(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)


@app.route('/tag/<tag_name>')
def get_by_tag(tag_name):
    posts = get_posts_by_tag(tag_name.lower())
    return render_template('tag.html', posts=posts, tag=tag_name)


@app.route('/bookmarks/add/<int:post_id>')
def add_bookmark(post_id):
    add_bm(post_id)
    return redirect('/', code=302)


@app.route('/bookmarks/remove/<int:post_id>')
def delete_bookmark(post_id):
    delete_bm(post_id)
    return redirect('/', code=302)


@app.route('/bookmarks')
def bookmarks():
    return render_template('bookmarks.html', posts=get_bookmarks_all())


if __name__ == '__main__':
    app.run()
