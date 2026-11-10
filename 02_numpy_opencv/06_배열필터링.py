"""
배열 필터링

논리식을 이용해서 데이터를 원하는 형태로 걸러내는 것
"""

import numpy as np

price_list = np.array([1000, 1500, 3000, 7000])

# (Q) 2000원 이하인 가격들만 필터링
print(price_list <= 2000)   # 동일한 크기의 논리 배열

print(price_list[price_list <= 2000])   # 조건 슬라이싱

# (Q) 2000원 이하인 가격들에 200원씩 추가
# price_list += 200   # 전체 +200원
price_list[price_list <= 2000] += 200
print(price_list)

# (Q) 1500원 이상 5000원 이하인 가격들만 출력
# if 가격 > 1500 and 가격 <= 5000
# print(price_list[(1번조건) & (2번조건)])
print(price_list[(price_list >= 1500) & (price_list <= 5000)])

# (Q) 평균가격보다 비싼 가격만 필터링하여 출력
print(np.mean(price_list))
print(price_list[price_list > np.mean(price_list)])

