"""
합계나 평균 등을 축별로 계산하고 싶을 경우
"""

import numpy as np

# (예) 학생 3명의 국영수 점수

scores = np.array([
    [80, 90, 70],   # 철수의 국어, 영어, 수학점수
    [60, 80, 90],   # 영희의 국어, 영어, 수학점수
    [90, 70, 100]   # 영수의 국어, 영어, 수학점수
])

print(scores.shape)
# 축은 shape의 좌측부터 순차적으로 부여됨
# 현재 scores.shape가 (3, 3)이니까
# 첫 번째 3이 axis=0에 해당 (줄)
# 두 번째 3이 axis=1에 해당 (칸)

# (Q) 전체 합계와 평균
print("전체 합계", np.sum(scores))
print("전체 평균", np.mean(scores))

# (Q) 과목별 합계와 평균
# print(scores[:, 0])
# print(np.sum(scores[:, 0]))
# print(np.mean(scores[:, 0]))
print("과목별 합계", np.sum(scores, axis=0))
print("과목별 평균", np.mean(scores, axis=0))

# (Q) 학생별 합계와 평균
print("학생별 합계", np.sum(scores, axis=1))
print("학생별 평균", np.mean(scores, axis=1))

