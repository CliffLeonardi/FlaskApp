# Imports
from flask import render_template, flash, redirect
from app import app
#Import Class
from .forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data))
        )
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form,
        providers=app.config['OPENID_PROVIDERS'])

# We don't need to get rid of this yet. If we toss it then the index page goes down.
@app.route('/index')

def index():
    user = {'nickname': 'Fake User'}
    posts = [
        {
            "author": {'nickname': 'Fake User 1'},
            "body": "Look at this beautiful code"
        },
        {
            "author": {'nickname': 'Fake President'},
            "body": "This is the best fake post, people are going to love this post."
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
