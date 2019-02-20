from apps import db
from flask import render_template, redirect, request, url_for, flash, session, Blueprint
from apps.posts.forms import PostUpdte
from apps.models import WebScrapy, PostScrapy
import requests

posts = Blueprint('posts',__name__,template_folder='templates/posts')


@posts.route('/add_posts', methods=['GET', 'POST'])
def add_posts():
    webs = requests.get(session['url_api'])
    url = WebScrapy(session['url_api'])
    db.session.add(url)
    db.session.commit()
    for web in webs.json():
        post = PostScrapy(web['title']['rendered'],
                              web['content']['rendered'], url.id)
        db.session.add(post)
        db.session.commit()

    return redirect(url_for('posts.list_posts'))


@posts.route('/list_posts')
def list_posts():
    posts = PostScrapy.query.all()
    return render_template('list_posts.html', posts=posts)


@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def update_posts(post_id):
    post = PostScrapy.query.get_or_404(post_id)
    form = PostUpdte()

    if form.validate_on_submit():
       post.title = form.title.data
       post.content = form.content.data
       db.session.commit()
       flash(f'El post se actualizo con exito')
       return redirect(url_for('post_update', post_id=post.id))
    elif request.method == 'GET':
       form.title.data = post.title
       form.content.data = post.content

    return render_template('update_post.html', form = form)
