"""
함수 실습 : 함수에서 리스트 사용하기

다음 요구사항에 맞는 함수를 구현하세요

1. count_pass 라는 이름의 함수를 만들어서 점수가 저장된 리스트를 전달하면 60점 이상인 인원수를 반환하도록 구현
2. average_pass라는 이름의 함수를 만들어서 점수가 저장된 리스트를 전달하면 60점 이상인 인원의 평균을 반환하도록 구현
3. lotto라는 이름의 함수를 만들어서 1~45 사이의 로또번호 6개를 추첨하여 반환하도록 구현
"""

# ------------------------------
# 합격 인원수 세는 함수
# ------------------------------
def count_pass(score_list, cutoff=60):
    count = 0
    for socre in score_list :
        if socre >= cutoff:  # 합격(60점 이상)
            count += 1
    return count

# ------------------------------
# 합격자의 평균 점수 계산하는 함수
# ------------------------------
def average_pass(score_list, cutoff=60):
    total = 0
    count = 0
    for score in score_list :
        if score >= cutoff :
            total += score
            count += 1
    # average = total / count
    # return average
    return total / count  # 평균을 구해서 반환

# ------------------------------
# 로또 생성 함수
# ------------------------------
import random
def lotto():
    numbers = list(range(1, 46))  # 1~45
    # choice = random.sample(numbers, 6)
    random.shuffle(numbers)
    choice = numbers[:6]

    choice.sort()
    return choice

# ------------------------------
# main 코드
# ------------------------------
scores = [75, 62, 53, 47, 88, 82, 60, 55, 55, 95]

print("합격 인원 수",count_pass(scores))
print("합격 인원 수",count_pass(scores, 70))

print("합격자 평균", average_pass(scores))
print("합격자 평균", average_pass(scores, 70))

print("로또", lotto())

# 파이썬에서 제공하는 기본 함수
print(sum(scores))
print(len(scores))
print(max(scores))
print(min(scores))
