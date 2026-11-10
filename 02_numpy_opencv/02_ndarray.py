"""
ndarray (n-dimension array), N차원 배열

- NumPY에서 여러 차원의 데이터를 관리하기 위해 고안된 핵심 도구
- 파이썬의 리스트와 호환 가능
- opencv의 대부분 기능과 호환 가능
"""

import numpy as np

# 여러가지 NumPy 생성 방법
# 1. 파이썬 리스트를 변환
a = np.array([10, 20, 30])
print(a)

# 2. 모든 값이 0인 배열
# b = np.zeros(차원, 형태)
# b = np.zeros((2, 3))
b = np.zeros((2, 3), dtype=np.uint8)
print(b)

# 3. 모든 값이 1인 배열
# c = np.ones(차원, 형태)
c = np.ones((2, 3))
print(c)

# 4. 모든 값이 100인 배열 (원하는 값)
# d = np.full(차원, 값, 형태)
d = np.full((2, 3), 100)
print(d)

# 5. 일정한 간격으로 배열 생성
e = np.arange(1, 11, 2)
print(e)

