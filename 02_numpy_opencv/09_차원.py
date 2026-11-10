"""
차원

배열의 차원을 확인하고 이를 변경하거나 하는 기술
"""

import numpy as np

# 1차원
a = np.array([10, 20, 30, 40, 50])

print(a)
print(type(a))
print(a.ndim)   # 차원
print(a.shape)  # 형태
print(a.size)   # 전체 데이터 수
print(len(a))   # a의 길이

print("-"*20)

# 2차원 (표)
b = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(b, type(b))
print(b.ndim)   # 차원
print(b.shape)  # (2, 3) = 2줄 3칸
# (주의) 이미지에서는 너비(width)가 칸이고, 높이(height)가 줄이다.
print(b.size)
print(len(b))   # []로 묶인 게 길이 1

# 2차원의 데이터 접근
# - 하나의 데이터를 부르기 위해서는 반드시 두 번의 접근이 필요
# print(b[0][0])    # 기본 파이썬 문법
print(b[0, 0])      # numpy 문법 (권장)

print(b[0])     # +0행
print(b[1])     # +1행
print(b[:, 0])  # +0열 (참고 : 콜론만 쓰면 전체의 의미를 가짐)
print(b[:, 1])  # +1열
print(b[:, 2])  # +2열

# numpy는 차원 변경이 가능하다.
c = np.arange(1, 13)
print(c)

# (Q) c를 2행 6열로 만들고 싶다.
# - reshape(줄, 칸) 사용
# - 개수가 딱 맞아야 가능
# - reshape도 원본을 공유하므로 복사가 필요하면 .copy() 사용
print(c.reshape(2, 6))
print(c.reshape(3, 4))

print(c.reshape(4, -1))    # -은 관계 없음
print(c.reshape(-1, 2))

d = c.reshape(3, -1)
print()
print(c)
print(d)

d[0, 0] = 100
print(c)
print(d)

# 2차원에서 1차원 변환도 가능할까?
# e = d.reshape(-1)
print(e)

