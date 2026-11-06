"""
딕셔너리 조회

"""

# 이름과 점수를 같이 저장하기 위한 딕셔너리 생성
data = {
    "홍길동" : 70,
    "임꺽정" : 75,
    "장보고" : 70,
    "이순신" : 90
}

# [1] key만 출력
print("<key 출력>")
for key in data:
    # print(key)
    print(key, data[key])

# [2] value만 출력 (권장하지 않음, value로는 key 추측 불가)
print("<value 출력>")
for value in data.values():
    print(value)

# [3] key, value를 한번에 출력
print("<한 번에 조회>")
print(data.items())
# for (key, value) in data.items():
for key, value in data.items():     # ,가 있으면 튜플이다. ()로 묶지 않아도 된다.
    print(key, value)


