"""
문자열 실습 : 닉네임 설정 프로그램
사용자에게 원하는 닉네임을 입력받아 설정하는 프로그램을 구현하세요

요구사항
- 운영자, admin과 같은 단어는 포함시킬 수 없습니다.
- 닉네임은 최소 2글자 이상 최대 10글자 이하로 설정해야 합니다
"""

nickname = input("닉네임을 입력하세요 : ")

if "운영자" in nickname or "admin" in nickname :
    print("사용할 수 없는 닉네임입니다.")
elif len(nickname) >= 2 and len(nickname) <= 10 :
    print("사용 가능한 닉네임입니다.")
else :
    print("닉네임은 최소 2글자 이상 최대 10글자 이하로 설정해야 합니다.")
