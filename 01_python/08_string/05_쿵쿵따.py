"""
문자열 실습 : 공포의 쿵쿵따
다음 규칙에 따라 진행되는 게임을 구현하세요

제시어는 보리차 입니다.
사용자에게 문자열을 입력받습니다.
입력받은 문자열이 3글자여야 합니다.
입력받은 문자열은 한글이라고 가정합니다.
입력받은 문자열은 제시어와 이어져야 합니다.
규칙에 어긋나는 경우 게임오버 메세지를 출력 하고 프로그램을 종료합니다.
규칙에 맞는 경우 게임을 계속 진행합니다.

추가해볼 내용

사용자가 입력한 단어들을 모두 기억해두었다가 종료되면 여태까지 입력한 단어들을 최신순으로 출력해주세요
"""

word_list = []
word = "보리차"

while True :
    user = input("문자 입력 : ")
    if len(user) != 3 or user[0] != word[-1]:
        print("게임오버")
        break
    else :
        word = user
        continue


word_list.append(user)
word_list.reverse()
print(word_list)