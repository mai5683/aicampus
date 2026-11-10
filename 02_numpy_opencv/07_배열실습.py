"""
numpy 배열 연산 실습
파일명 : 07_배열실습.py
다음 데이터를 사용하여 문제를 해결하세요.

scores = np.array([55, 80, 95, 70, 100, 65, 85, 40])

- 80점 이상인 점수만 출력하세요.
- 60점 미만인 점수만 출력하세요.
- 70점 이상 90점 이하인 점수를 출력하세요.
- 60점 미만이거나 90점 이상인 점수를 출력하세요.
- 80점 이상인 학생 수를 출력하세요.
- 60점 미만인 점수를 모두 60점으로 변경하세요.
- 80점 이상인 학생들의 점수 평균을 계산하세요.
"""

import numpy as np

scores = np.array([55, 80, 95, 70, 100, 65, 85, 40])

print("80점 이상 :", scores[scores>=80])
print("60점 미만 :", scores[scores<60])
print("70점 이상 90점 이하 :", scores[(scores>=70) & (scores<=90)])
print("60점 미만이거나 90점 이상 :", scores[(scores<60) | (scores>=90)])
print("80점 이상인 학생 수 :", len(scores[scores>=80]))    # 차원에 따라 오해의 소지가 있음
                            # scores[scores>=80].size
scores[scores<60] = 60
print("60점 미만 점수 모두 60점으로 변경 :", scores)
print("80점 이상의 점수 평균 :", np.mean(scores[scores>=80]))

# (추가) 모든 학생의 점수를 5점씩 증가 (ex : 잘못 출제된 문제)
# scores += 5
# print(scores)
# 값이 범위를 초과하는 경우를 제거
# scores[scores>100] = 100
# scores[scores<0] = 0

# np.clip()을 이용하여 배열 전체의 값을 원하는 범위로 맞출 수 있다. (넘어가는 건 자동 변경)
scores = np.clip(scores+5,0, 100)
print(scores)


