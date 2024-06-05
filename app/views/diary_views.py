from flask import Blueprint, render_template, request, url_for

from app.models import Diary
from app.forms import DiaryForm, AnswerForm
from datetime import datetime
from werkzeug.utils import redirect

from .. import db

bp = Blueprint('diary', __name__, url_prefix='/diary')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)  # 페이지
    diary_list = Diary.query.order_by(Diary.create_date.desc())
    diary_list = diary_list.paginate(page=page, per_page=10)
    return render_template('diary/diary_list.html', diary_list=diary_list)


@bp.route('/detail/<int:diary_id>/')
def detail(diary_id):
    form = AnswerForm()
    diary = Diary.query.get_or_404(diary_id)
    return render_template('diary/diary_detail.html', diary=diary, form=form) 

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = DiaryForm()
    if request.method == 'POST' and form.validate_on_submit():
        diary = Diary(subject=form.subject.data, content=form.content.data, weather=form.weather.data, create_date=datetime.now())
        db.session.add(diary)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('diary/diary_form.html', form=form)