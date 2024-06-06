from . import db
from app import db
from datetime import datetime
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False) #제목#
    content = db.Column(db.Text(), nullable=False) #내용#
    create_date = db.Column(db.DateTime(), nullable=False) #날짜#
    # 'weather' 필드 추가
    weather = db.Column(db.String(255))
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    image_filename = db.Column(db.String(100), nullable=True)

class Answer(db.Model): #댓글#
    id = db.Column(db.Integer, primary_key=True)
    diary_id = db.Column(db.Integer, db.ForeignKey('diary.id', ondelete='CASCADE')) #일기를 삭제하면 댓글도 삭제되게 연동#
    question = db.relationship('Diary', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)