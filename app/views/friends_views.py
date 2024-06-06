""" from flask import Blueprint, render_template, request, jsonify
from app.views.auth_views import login_required
from app.models import Friendship, User
from werkzeug.utils import redirect
from .. import db
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user

friends_bp = Blueprint('friends', __name__, url_prefix='/friends')

@staticmethod
def get(user_id):
    user_data = get_user_from_db(user_id)  # 데이터베이스 접근 함수
    if user_data:
        return User(user_data.id, user_data.username)
    return None



@friends_bp.route('/add_friend', methods=['POST'])
def add_friend():
    data = request.get_json()
    user_id = data.get('user_id')
    friend_id = data.get('friend_id')
    
    # 유효성 검사: 자기 자신을 친구로 추가하는 경우
    if user_id == friend_id:
        return jsonify({'message': '자기 자신을 친구로 추가할 수 없습니다.'}), 400

    # 유효성 검사: 이미 친구 관계가 있는지 확인
    existing_friendship = Friendship.query.filter_by(user_id=user_id, friend_id=friend_id).first()
    if existing_friendship:
        return jsonify({'message': '이미 친구입니다.'}), 400

    # 친구 관계 생성
    new_friendship = Friendship(user_id=user_id, friend_id=friend_id)
    db.session.add(new_friendship)
    db.session.commit()
    
    return jsonify({'message': '친구가 추가되었습니다.'}), 200

@friends_bp.route('/friends/<int:user_id>', methods=['GET'])
@login_required
def get_friends(user_id):
    # 사용자가 user_id인 친구 관계 조회
    friendships1 = Friendship.query.filter_by(user_id=user_id).all()

    # 친구 목록 생성
    friend_ids = set()
    for friendship in friendships1:
        friend_ids.add(friendship.friend_id)

    # 친구 정보 조회
    friends = User.query.filter(User.id.in_(friend_ids)).all()

    # 여기서 HTML 파일을 렌더링하고 친구 목록을 전달합니다.
    return render_template('/html/friends_list.html', friends=friends)  """
