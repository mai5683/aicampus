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


# 파일에서 닉네임 목록을 불러오기
file = open("nicknames1.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

nickname_list = []
for line in lines:
    nickname_list.append(line.strip())

# 사용자 입력
nickname = input("사용할 닉네임 입력 : ")

if nickname in nickname_list:
    print("이미 사용중인 닉네임입니다")
else:
    print("사용 가능한 닉네임입니다")
    nickname_list.append(nickname)
    # nickname 또는 nickname_list를 파일 저장
    # - nickname을 추가하려면 a(ppend)모드가 필요
    # - nicknames를 추가하려면 w(rite) 모드가 필요 (선택)
    file = open("nicknames1.txt", "w", encoding="utf-8")
    for n in nickname_list:
        file.write(n)
        file.write("\n")
    file.close()




