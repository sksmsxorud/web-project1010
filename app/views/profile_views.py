from flask import Blueprint, render_template, request, url_for
from flask import Flask, request, jsonify
from app.models import User
from werkzeug.utils import redirect

from .. import db

bp = Blueprint('profile', __name__, url_prefix='/profile')

profiles = {}

@bp.route('/home')
def home():
    return render_template('html/home.html')

@bp.route('/profile', methods=['POST'])
def save_profile():
    # 프로필 정보를 받아서 저장
    data = request.form
    profile_photo = request.files['photoUpload']
    name = data['name']
    status_message = data['statusMessage']
    
    # 파일을 서버에 저장하기 위한 처리. 여기서는 파일명만 출력해보겠습니다.
    print(f"Received photo file: {profile_photo.filename}")
    
    # 프로필 정보 저장
    profiles[name] = {'name': name, 'status_message': status_message}
    
    # 성공 메시지를 JSON 형태로 리턴
    return jsonify({"message": "프로필 저장 성공", "data": profiles[name]})

@bp.route('/chat', methods=['POST'])
def chat_with_ai():
    # 사용자 메시지 받기
    user_message = request.json['message']
    
    # 여기서는 단순히 사용자 메시지를 반복하는 것으로 AI 응답을 시뮬레이션합니다.
    ai_response = f"당신: {user_message}"
    
    # AI 응답을 JSON 형태로 리턴
    return jsonify({"ai_response": ai_response})

if __name__ == '__main__':
    app.run(debug=True)