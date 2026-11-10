# (Q) 다섯 개의 숫자를 저장한 뒤 합계, 평균, 최대, 최소 등을 구합시다.
#       → 저장하려면 변수가 5개 필요하다.
#       → 문제? 개수가 달라지면 코드를 재작성해야 한다.
#       → 하나의 리스트(list)로 처리할 수 있다.

scores = [50, 60, 70, 75, 81]
print(scores)

# 여러 개의 데이터를 위치(순서)에 기반해서 관리한다.
# scores(리모컨) --------> [50] [60] [70] [75] [81]
#                                      +---+---+---+---+---+
#                                     +0  +1   +2   +3   +4   +5
print(scores[0])  # +0 지점 데이터
print(scores[1])  # +1 지점 데이터
print(scores[2])  # +2 지점 데이터
print(scores[3])  # +3 지점 데이터
print(scores[4])  # +4 지점 데이터
# print(scores[5])  # error (5번째가 아님에 유의)
print("-"*10)
print(scores[-1])  # 맨 뒤에서 -1 지점
print(scores[-2])  # 맨 뒤에서 -2 지점
print(scores[-3])  # 맨 뒤에서 -3 지점
print(scores[-4])  # 맨 뒤에서 -4 지점
print(scores[-5])  # 맨 뒤에서 -5 지점

# 합계
# total = scores[0] + scores[1] + scores[2] + scores[3] + scores[4]

# total = 0
# total += scores[0]
# total += scores[1]
# total += scores[2]
# total += scores[3]
# total += scores[4]

# 반복문과 결합
# total = 0
# for i in range(5) :
#     total += scores[i]

total = 0
for score in scores :
    total += score

print("합계 :", total)

# 랜덤과 결합
import random
print(random.choice(scores))  # 아무거나 하나 뽑아서 출력

