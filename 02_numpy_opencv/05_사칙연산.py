"""
numpy 배열의 사칙연산

"""

import numpy as np

a = np.array([10, 20, 30])

# a[0] += 5
# a[1] += 5
# a[2] += 5

# a += 5        # a를 5증가(원본 변경)
print(a + 5)    # a의 모든 값에 5를 더해라. (사본 생성)
print(a - 5)    # a의 모든 값에서 5를 빼라. (사본 생성)
print(a * 5)    # a의 모든 값에 5를 곱해라. (사본 생성)
print(a / 5)
print(a // 5)
print(a % 3)
print(a ** 2)   # 제곱도 가능

# 배열의 통계 기능도 제공
# - 합계, 평균, 최소, 최대, 중앙값, 표준편차
print(np.sum(a))      # 합계
print(np.mean(a))     # 평균
print(np.median(a))   # 중앙값
print(np.std(a))      # 표준편차(클 수록 데이터가 사방팔방에 퍼진 것)
print(np.min(a))      # 최소값
print(np.max(a))      # 최대값

# 배열끼리 계산 가능 (크기가 같아야 함)
# a = np.array([10, 20, 30])
b = np.array([3, 6, 9])

print(a + b)
print(a - b)
print(a * b)
print(a / b)


