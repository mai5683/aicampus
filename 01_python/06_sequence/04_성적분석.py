"""
리스트 실습

5명의 시험성적을 입력받은 뒤 반복문과 조건문을 사용하여 다음을 구현하세요.

합격(60점 이상) 학생의 점수만 출력하세요
성적 우수자(90점 이상) 학생의 점수만 출력하세요
합격 인원수와 성적 우수자의 인원수를 각각 구하여 출력하세요
처음 입력한 학생의 등수를 구하여 출력하세요
"""

scores = []
pass_count = 0
excellent_count = 0
rank = 1

for score in range(5) :
    score = int(input("성적 입력 : "))
    scores.append(score)

    if score >= 60 :
        pass_count += 1
        print(f"합격 학생의 점수 : {score}점")
    if score >= 90 :
        excellent_count += 1
        print(f"성적 우수 학생의 점수 : {score}점")

for i in scores :  # scores 리스트 안에 있는 값을 처음부터 하나씩 꺼내서 i에 넣는다. i 대신 other_score 등 다른 변수명 사용 추천
    if scores[0] < i :
        rank += 1

print(f"합격생 인원수 : {pass_count}명")
print(f"성적 우수자 인원수 : {excellent_count}명")
print(f"첫 번째 학생 등수 : {rank}등")