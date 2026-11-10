"""
문자열 실습 : 로그인 프로그램 (03_로그인.py)
사용자에게 아이디와 비밀번호를 입력 받아 다음과 같이 처리하세요

아이디가 khacademy이고 비밀번호가 aicampus인 경우 로그인 성공 출력
아이디 또는 비밀번호가 맞지 않는 경우 인증이 거부되었습니다 출력
"""

# 사용자 입력
id = input("아이디 : ")
pw = input("비밀번호 : ")

# 판정
# is_login = 아이디 일치 and 비밀번호 일치
# is_login = id == "kdacademy" and pw == "aicampus"
is_login = id.lower() == "kdacademy" and pw == "aicampus"
            # .lower() : 영어를 소문자로 변환하는 명령어
            # .upper() : 대문자로 변환하는 명령어

# 출력
if is_login:
    print("로그인 성공")
else :
    print("인증이 거부되었습니다")