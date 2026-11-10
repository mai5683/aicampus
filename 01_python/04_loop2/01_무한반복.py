"""
while 반복

특정 조건을 만족하는 동안 실행되는 반복문
= 특정 시점까지 실행되는 반복문
"""

import random

count = 0

while True :  # 무한 반복 (언제나 실행해라)
    dice = random.randint(1, 6)
    print(f"주사위 = {dice}")
    count += 1

    # 주사위가 6이 나오면 그만둬라
    # = 주사위가 6이 나올 때까지 던져라
    if dice == 6 :
        break
# else를 쓰면 while이 한번도 실행되지 않은 경우 실행됨

print(f"주사위를 총 {count}번 던졌습니다.")