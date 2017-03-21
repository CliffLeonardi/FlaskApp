from flask_wtf import Form
from wtfforms import Stringfield, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form)
    openid = Stringfield('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
