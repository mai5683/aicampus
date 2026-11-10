"""
numpy 배열생성 실습
파일명 : 03_배열생성.py

1. 1부터 10까지의 정수가 들어 있는 배열을 만드세요.
2. 0부터 20까지 2씩 증가하는 배열을 만드세요.
3. 0이 10개 들어 있는 정수 배열을 만드세요.
4. 1이 7개 들어 있는 정수 배열을 만드세요.
5. [85, 90, 75, 100] 리스트를 NumPy 배열로 변환하세요.
6. 5부터 50까지 5씩 증가하는 배열을 만드세요.
"""

import numpy as np

# 1. a = np.array([1,2,3,4,5,6,7,8,9,10], dtype=int)
a = np.arange(1, 11, 1, dtype=int)
print(a)

# 2.
b = np.arange(0, 21, 2, dtype=int)
print(b)

# 3. c = np.full(10, 0, dtype=int)
c = np.zeros((10), dtype=int)  # np.zeros(1,10) 으로 하면 []가 2개 생김
print(c)

# 4. np.full(7, 1, dtype=int)
d = np.full((1, 7), 1, dtype=int)
print(d)

# 5.
e = np.array([85, 90, 75, 100])
print(e)

# 6.
f = np.arange(5, 51, 5)
print(f)


