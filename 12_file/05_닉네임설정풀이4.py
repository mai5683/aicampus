"""
# 파일 입출력 실습 : 닉네임 설정하기

파일명 : `05_닉네임설정.py`

사용자에게 원하는 닉네임을 입력받아 다음과 같이 처리하는 프로그램을 구현하세요

- 프로그램과 같은 위치에 등록된 모든 닉네임이 존재하는 `nicknames.txt`라는 파일이 있습니다 (없으면 생성하고 진행하세요)
- 사용자가 닉네임을 입력하면 다음을 검사합니다
  - 한글, 영어, 숫자 2~10글자인지 검사하고 형식에 맞지 않으면 오류메세지와 함께 프로그램을 중지시킵니다
  - `운영자`라는 단어가 포함되면 오류메세지와 함께 프로그램을 중지시킵니다
  - 이미 등록된 닉네임이라면 오류메세지와 함께 프로그램을 중지시킵니다
- 모든 검사를 통과했다면 `nicknames.txt`에 사용자가 입력한 닉네임을 등록하고 안내메세지와 함께 프로그램을 종료합니다
"""

import re

# ----------------------------------
# 기존 닉네임 불러오는 함수
# ----------------------------------
def load_nicknames():
    # with 구문을 사용하면 생성된 리소스를 구문 종료와 함께 자동 close() 처리한다
    # - 예외 여부와 관계없이 반드시 close()가 됨
    # - 변수명을 as 뒤에 작성
    with open("nicknames1.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    nickname_list = []
    for line in lines:
        nickname_list.append(line.strip())

    return nickname_list

# ----------------------------------
# 신규 닉네임 저장하는 함수
# ----------------------------------
def save_nicknames(nickname_list):
    # file = open("nicknames.txt", "w", encoding="utf-8")
    with open("nicknames1.txt", "w", encoding="utf-8") as file:
        for n in nickname_list:
            file.write(n)
            file.write("\n")
    # file.close()

# ----------------------------------
# 메인 프로그램
# ----------------------------------
nickname_list = load_nicknames()

# 사용자 입력
nickname = input("사용할 닉네임 입력 : ")

# 안되는 조건들을 쭉 나열한 뒤 해당하면 차단하는 방향으로 코드 구현
regexp = r"(?!.*?운영자)[가-힣A-Za-z0-9]{2,10}"
result = re.fullmatch(regexp, nickname)
if result is None:
    print("닉네임은 운영자를 포함하지 않는 한글, 영어, 숫자 2~10글자만 가능합니다")
    exit(0)
if nickname in nickname_list:
    print("이미 사용중인 닉네임입니다")
    exit(0)

# 통과했다면 정상적인 닉네임으로 간주
print("사용 가능한 닉네임입니다")
nickname_list.append(nickname)
save_nicknames(nickname_list)


