"""
# 반복 카운트 실습 (04_카운트실습.py)

다섯명의 학생 점수를 입력받아 `합격자`와 `불합격자`의 수를 출력하세요
(합격의 기준은 `60점` 이상이며, 사람들은 0~100 사이의 숫자만 입력합니다)
"""

# 반복 5회 적용 - for i in range(5)

count_pass = 0
count_fail = 0

for i in range(5):
    score = int(input("점수 입력 : "))
    if score >= 60:
        count_pass += 1
    else:
        count_fail += 1

# print("합격자 수 :", count_pass)
# print("불합격자 수 :", count_fail)
print(f"합격자 수 : {count_pass}명")
print(f"불합격자 수 : {count_fail}명")