"""
리스트 실습

5명의 시험성적을 입력받은 뒤 반복문과 조건문을 사용하여 다음을 구현하세요.

합격(60점 이상) 학생의 점수만 출력하세요
성적 우수자(90점 이상) 학생의 점수만 출력하세요
합격 인원수와 성적 우수자의 인원수를 각각 구하여 출력하세요
처음 입력한 학생의 등수를 구하여 출력하세요
"""

# 입력 받자!
scores = []

for i in range(5) :  # 다섯 번(5명)
    number = int(input("점수 입력 : "))
    scores.append(number)

# 1
print("<60점 이상 합격자의 점수>")
for score in scores :
    if score >= 60 :
        print("점수 :", score)

# 2
print("<90점 이상 우수자의 점수>")
for score in scores :
    if score >= 90 :
        print("점수 :", score)

# 3
print("<60점 이상 합격자의 인원수>")
pass_count = 0
for score in scores :
    if score >= 60 :
        pass_count += 1
print(f"{pass_count}명")

# 4
print("<90점 이상 우수자의 인원수>")
excellent_count = 0
for score in scores :
    if score >= 90 :
        excellent_count += 1
print(f"{excellent_count}명")

# 5 : 등수는 1+ 나보다 높은 점수 개수
print("<맨 앞 학생의 등수>")
high = 0
for score in scores :
    # print(score, scores[0], score > scores[0])
    if score > scores[0] :
        high += 1

rank = 1 + high
print(f"{rank}등")

