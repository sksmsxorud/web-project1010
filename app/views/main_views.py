from flask import Blueprint, url_for
from werkzeug.utils import redirect
from flask import Blueprint, render_template, request, url_for
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, world!'


@bp.route('/')
def index():
    # 'home' 뷰 함수로 리다이렉트하도록 변경
    return redirect(url_for('main.home'))  # 'main'은 블루프린트 이름, 'home'은 뷰 함수 이름

@bp.route('/home')
def home():
    return render_template('html/home.html')

@bp.route('notifications')
def notice():
    return render_template('html/notifications.html')

@bp.route('profile')
def profile():
    return render_template('html/profile.html')