from flask import Blueprint, render_template
from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    diary_list = Diary.query.order_by(Diary.create_date.desc())
    return render_template('diary/diary_list.html', diary_list=diary_list)