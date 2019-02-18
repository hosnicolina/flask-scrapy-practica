from apps import app
from flask import render_template, redirect, request, url_for, flash, session
from apps.forms import UlrForm
import requests
import json


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UlrForm()

    if form.validate_on_submit():
        url = form.url.data + '/wp-json/wp/v2/posts/1171'
        api = requests.get(url)
        print(api.status_code)
        if api.status_code == requests.codes.ok:
            session['url_api'] = url
            return redirect(url_for('scrapy'))
        else:
            flash('Lo sentimos no se puede analizar la web')
            return redirect(url_for('home'))

    return render_template('home.html', form=form)


@app.route('/scrapy',methods=['GET', 'POST'])
def scrapy():
    content = requests.get(session['url_api'])
    return render_template('scrapy.html', content = content.json())




if __name__ == '__main__':
    app.run(debug=True)
