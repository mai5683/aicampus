"""
random 모듈과 list를 사용해서 로또번호를 추첨하는 프로그램을 만들고 싶습니다.
계획은 다음과 같습니다.

로또 통 대신 리스트를 사용해서 1부터 45까지의 숫자를 리스트에 등록해둔다
random 모듈의 shuffle 명령을 이용해서 리스트를 섞는다
섞인 리스트에서 6개의 숫자를 가져와 화면에 보여준다

(Q1) 천원 추첨 결과를 출력하세요 (1회)
(Q2) 오천원 용지 한장을 출력하세요 (5회)

인터넷에 로또 검색하시면 천원, 오천원 용지가 나옵니다.
"""

import random

# (방법1) 복원추출, 중복이 발생하는 추첨방법
# lotto = []
#
# while len(lotto) < 6:
#     number = random.randint(1, 45)
#     if number not in lotto:    # number가 lotto에 없을 때만
#         lotto.append(number)   # 추가하세요
# print(lotto)

# (방법2) 비복원추출, 중복이 발생하지 않는 추첨방법

# numbers = [1,2,3,4,5,6,...,42,43,44,45]
# lotto = []
# for numbers in range(1,45):
#     lotto.append(numbers)

# 리스트 컴프리헨션 (한 줄짜리 for구문)   - 비추천
# number = [i for i in range(1,46)]

# 리스트 변환 명령
numbers = list[int](range(1,46))

for i in range(5):
    # shuffle
    random.shuffle(numbers)
    lotto = numbers[:6]
    lotto.sort()
    print(lotto[:6])