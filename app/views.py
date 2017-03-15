from flask import render_template
from app import app

@app.route('/')
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
