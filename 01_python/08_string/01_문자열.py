""""
문자열(string)

문자열은 여러 개의 문자가 순서대로 저장된 형태의 데이터
리스트처럼 인덱스를 가지고 슬라이싱이 가능

문자열은 불변이다. (immutable)
"""

a = ["H", "e", "l", "l", "o"]
b = "Hello"

print(type(a))  # list
print(type(b))  # str (string의 약자)

# 형태는 다르지만 명령이 매우 비슷하다.
print(len(a))
print(len(b))

print(a[0], a[1], a[2], a[3], a[4])  # list
print(a[0], a[1], a[2], a[3], a[4])  # str

print(a[:4])  # 잘라내기 [0:4]와 같다
print(b[:4])  # 잘라내기 [0:4]와 같다

# (Q) 끝에서 세 글자
print(a[-3:])

print(b[::-1])  # 거꾸로 -1칸씩

c = "안녕하세요"
print(c[::-1])