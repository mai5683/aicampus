"""
파일 입출력 실습 : 닉네임 설정하기
파일명 : 05_닉네임설정_파일출력.py

사용자에게 원하는 닉네임을 입력받아 다음과 같이 처리하는 프로그램을 구현하세요

- 프로그램과 같은 위치에 등록된 모든 닉네임이 존재하는 nicknames.txt라는 파일이 있습니다 (없으면 생성하고 진행하세요)
- 사용자가 닉네임을 입력하면 다음을 검사합니다
- 한글, 영어, 숫자 2~10글자인지 검사하고 형식에 맞지 않으면 오류메세지와 함께 프로그램을 중지시킵니다
- 운영자라는 단어가 포함되면 오류메세지와 함께 프로그램을 중지시킵니다
- 이미 등록된 닉네임이라면 오류메세지와 함께 프로그램을 중지시킵니다
- 모든 검사를 통과했다면 nicknames.txt에 사용자가 입력한 닉네임을 등록하고 안내메세지와 함께 프로그램을 종료합니다
"""


file = open("nicknames.txt", "w", encoding="utf-8")

nickname = input("사용할 닉네임 : ")


condition1 = "운영자" not in nickname
condition2 = "admin" not in nickname
condition3 = len(nickname) >= 2 and len(nickname) <= 10
condition4 = not nickname[0].isdigit()

can_use = condition1 and  condition2 and  condition3 and condition4

if can_use :
    print("닉네임 설정이 완료되었습니다.")
else :
    print("사용할 수 없는 닉네임 형태입니다.")

file.write(nickname)
file.close()