from flask import render_template, redirect, Blueprint, url_for
from apps.webs.forms import WpForm
from apps.helpers_function import clean_url
from apps.models import WebWordpress
from apps import db

webs = Blueprint('webs',__name__,template_folder='templates/webs')

@webs.route('/web_add', methods=['POST', 'GET'])
def webs_add():
    form = WpForm()

    if form.validate_on_submit():

        web = WebWordpress(clean_url(form.url.data), form.username.data, form.password.data)
        db.session.add(web)
        db.session.commit()
        return redirect(url_for('webs.webs_list'))

    return render_template('add_web.html',form = form)


@webs.route('/web_list', methods=['POST', 'GET'])
def webs_list():
    webs = WebWordpress.query.all()
    return render_template('list.html', webs = webs)




