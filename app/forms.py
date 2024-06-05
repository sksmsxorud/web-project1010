from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')


class DiaryForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목이 없자낫!! 다멧!')])
    content = TextAreaField('내용', validators=[DataRequired('내용이 없자낫!! 다멧!')])
    weather = StringField('날씨', validators=[])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('댓글을 입력해주세요')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])