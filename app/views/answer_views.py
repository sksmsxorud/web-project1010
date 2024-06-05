from datetime import datetime

from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from app import db
from ..forms import AnswerForm
from app.models import Diary, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:diary_id>', methods=('POST',))
def create(diary_id):
    form = AnswerForm()
    diary = Diary.query.get_or_404(diary_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now())
        diary.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('diary.detail', diary_id=diary_id))
    return render_template('diary/diary_detail.html', diary=diary, form=form)
