from flask import render_template, redirect, request, url_for, flash, session, Blueprint
from apps.core.forms import UlrForm
from helpers_function import clean_url
import requests

core = Blueprint('core', __name__)

@core.route('/', methods=['GET', 'POST'])
def home():
    form = UlrForm()

    if form.validate_on_submit():
        url = clean_url(form.url.data) + 'wp-json/wp/v2/posts/'
        api = requests.get(url)
        if api.status_code == requests.codes.ok:
            session['url_api'] = url
            return redirect(url_for('posts.add_posts'))
        else:
            flash('Lo sentimos no se puede analizar la web')
            return redirect(url_for('core.home'))

    return render_template('home.html', form=form)
