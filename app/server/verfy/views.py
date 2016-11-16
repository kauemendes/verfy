# app/server/verfy/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request
from flask_login import login_user, logout_user, login_required

from app.server import bcrypt, db
from app.server.verfy.forms import SearchForm, RegisterForm
from app.server.verfy.models import Urls
import json

################
#### config ####
################

verfy_blueprint = Blueprint('verfy', __name__,)


################
#### routes ####
################

@verfy_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        url = Urls(
            url=form.search.data,
        )
        db.session.add(url)
        db.session.commit()

        flash('Search is complete.', 'success')
        return redirect(url_for("verfy.result"))

    return render_template('verfy/search.html', form=form)


@verfy_blueprint.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('verfy/result.html', url=json.dumps({}))
