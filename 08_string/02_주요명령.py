"""
문자열의 주요명령
- 같다, 다르다는 숫자와 동일 (==, !=)
"""

song = "떴다 떴다 비행기 \n날아라 날아라"
email = "testuser@naver.com"

# 포함 검사
# email에 @가 들어있는가?
print("@" in email)

# - email에 @가 몇 번 들어갔는가?
print(email.count("@"))
print(song.count("@"))

# - email에서 @가 글자 몇 번째에 있나요?
print(email.find("@"))
print(song.find("@"))  # 없으면 -1로 나옴

# - email이 naver.com으로 끝나나요?
print(email.endswith("naver.com"))
print(email.endswith("@"))

# - email이 @로 시작하나요?
print(email.startswith("@"))