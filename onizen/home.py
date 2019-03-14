from onizen.db import get_db

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('home', __name__, url_prefix='/')

# view for home page
@bp.route('/')
def index():
    return render_template('home/index.html')

@bp.route('/resume')
def resume():
    return render_template('home/resume.html')
