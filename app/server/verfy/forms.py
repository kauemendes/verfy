# app/server/verfy/forms.py


from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, URL, Length


class SearchForm(Form):
    search = StringField('Search URL', [DataRequired(), URL()])


class RegisterForm(Form):
    search = StringField(
        'Search URL',
        validators=[DataRequired(), URL(require_tld=False), Length(min=4, max=1024)])

