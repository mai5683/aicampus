"""
사전형(Dictionary) 데이터

key-value 형태의 저장소
- key : 데이터를 불러내기 위한 열쇠 역할을 하며 중복 불가하다.
- value : key에 연결된 데이터이며 중복 가능하다.

list처럼 데이터를 제한 없이 저장할 수 있는 저장소
"""

student = {
    "name" : "피카츄",     # name = 피카츄
    "age" : 25,           # age = 25
    "score" : 80          # score = 80
}

print(student)
print(type(student))
print(len(student))

# 어떻게 쓰는가?
# 이름(key)을 이용해서 데이터를 변경하거나 불러온다.
# print(student[0], student[1], student[2])  # list의 경우
print(student["name"])  #student 중에서 key=name인 데이터
print(student["age"])
print(student["score"])
# print(student["hobby"])  # 없는 이름이면 Error 발생

# 데이터 추가, 수정
# - 이름을 라이츄로 변경
student["name"] = "라이츄"     # 존재하는 key에 데이터를 넣으면 수정
student["country"] = "한국"    # 존재하지 않는 key에 데이터를 넣으면 추가

# - 나이 1살 증가시켜 보세요.
# student["age"] = student["age"] + 1
student["age"] += 1

print(student)


# 삭제
# - 국가 정보를 제거
# del student["country"]    # '지운다'는 개념
student.pop("country")      # '빼낸다'는 개념

print(student)


# 검색
# - age라는 key가 존재하는지 확인
print("age" in student)
print("age2" in student)