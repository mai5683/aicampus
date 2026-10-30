"""
랜덤(random)

- 뭐가 나올지 알 수 없는 값
- 범위를 특정할 수 있어야 함

파이썬에서는 기본 명령으로 랜덤을 제공하지 않는다.
랜덤을 사용하고 싶다면 'import'를 써서 모듈을 불러와야 한다.
"""

# random 모듈을 준비해줘!
import random

# random에 점(.)을 찍고 명령이름을 호출하면 사용이 가능

# 6 미만 정수 +1
dice = random.randrange(6)+1
print("dice:", dice)

# 1 이상 7 미만 정수
dice = random.randrange(1, 7)
print("dice:", dice)

# 1~6 정수 (추천)
dice = random.randint(1, 6)
print("dice:", dice)

# 1 이상 6 이하 실수 (추천)
number = random.uniform(1, 6)
print("number:", number)

print()
# (Q) 주사위 열 번 던지세요.
for i in range(10):
    dice = random.randint(1, 6)
    print("number : ", dice)