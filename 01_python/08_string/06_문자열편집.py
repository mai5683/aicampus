"""
문자열 편집

문자열을 변형하거나 분리, 결합하여 새로운 문자열을 만들어 내는 것
* 문자열은 불변(immutable)이기 때문에 수정이 불가하다.

참고로 리스트는 가변(mutable)입니다.
"""

li = [30, 20, 50, 10, 40]
li.sort()
print("리스트", li)

txt = "Hello"
# txt.upper()  # 대문자 만들기
        # -----> 앞서 .sort로 리스트 정렬을 한 상태라 문자열이 불변하기 떄문에 .upper가 실행되지 않음
txt = txt.upper()
        # -----> txt 값을 새로 만들어서 문자열을 덮어줘야 함
print("대문자", txt)

txt = txt.lower()
        # -----> 위와 마찬가지로 txt 값을 새로 만들어서 문자열을 덮어줘야 함
print("소문자", txt)

# 불필요한 여백
# - 여백이 아닌 첫글자의 앞 (왼쪽 여백)
# - 여백이 아닌 마지막 글자의 뒤 (오른쪽 여백)
url = "         www.naver.com           "
print(url)
print(url.strip())  # 통신 과정에서 붙은 불필요한 것을 제거
print(url.lstrip())
print(url.rstrip())

url = "         www     .naver.com          "
print(url.strip())

# 문자열 치환
note = "I love chicken"
print(note.replace("chicken", "python"))  # chicken을 python으로 변경

# 메소드 체이닝 - 연속으로 .을 찍어서 작업시키는 것
print(note.replace("love", "hate")
      .replace("chicken", "pizza"))
                            # ------> 이렇게 해도 원본은 바뀌지 않는다.

