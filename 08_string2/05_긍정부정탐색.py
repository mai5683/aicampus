"""
긍정탐색(positive lookahead)과 부정탐색(negative lookahead)

- 긍정탐색은 요구한 형태가 1회 이상 나와야 하는 경우
- 부정탐색은 요구한 형태가 한 번도 나오면 안 되는 경우

- .*[A-Z]는 대문자 알파벳이 나오기 전까지 최대한 많은 내용을 찾고
- .*8?[A-Z]는 대문자 알파벳이 나오기 전까지 가장 적은 내용을 찾는다.

- (ex) 대문자를 반드시 1개 포함시키는 탐색 : (?=.*?[A-Z]) 를 ^ 뒤에 추가
- (ex) 대문자를 1개도 포함시키면 안 되는 탐색 : (?!.*?[A-Z]) 를 ^ 뒤에 추가
"""

import re

# 긍정탐색 예시 : 비밀번호

password = "Testuser1!"
regexp = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!\@\#\$\%\^])[A-Za-z0-9!\@\#\$\%\^]{8,16}$"
result = re.fullmatch(regexp, password)

if result is not None:
    print("올바른 비밀번호 형식입니다")
else :
    print("반드시 대문자, 소문자, 숫자, 특수문자를 1개 이상 포함한 8~16자로 만드세요")


# 부정탐색 예시

nickname = "멋진운영자님"
# regexp = r"^[가-힣0-9]{2,10}$"
regexp = r"^(?!.*운영자)[가-힣0-9]{2,10}$"
result = re.fullmatch(regexp, nickname)
if result is not None:
    print("올바른 닉네임 형식입니다")
else :
    print("잘못된 닉네임 형식입니다")