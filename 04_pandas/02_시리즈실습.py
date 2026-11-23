"""
# Pandas Series 실습 문제 — 학생 성적 관리

다음은 학생 5명의 시험 점수를 저장한 NumPy 배열입니다.

```python
import numpy as np
import pandas as pd

scores = np.array([75, 90, 85, 60, 95])
names = ["홍길동", "김철수", "이영희", "박민수", "최지우"]
```

## 요구사항

1. `scores` 배열을 Pandas의 `Series`로 변환하세요.
2. `names`를 Series의 인덱스로 지정하세요.
3. 완성된 Series를 출력하세요.
4. `김철수`의 점수를 출력하세요.
5. `박민수`의 점수를 80점으로 변경하세요.
6. 80점 이상인 학생들의 점수만 출력하세요.
7. 전체 학생의 평균 점수를 출력하세요.
8. 90점 이상인 학생이 몇 명인지 출력하세요.

※ 6~8번은 5번에서 수정한 점수를 기준으로 계산하세요.
"""


import numpy as np
import pandas as pd

scores = np.array([75, 90, 85, 60, 95])
names = ["홍길동", "김철수", "이영희", "박민수", "최지우"]

# 1. `scores` 배열을 Pandas의 `Series`로 변환하세요.
# 2. `names`를 Series의 인덱스로 지정하세요.

# 인덱스를 생성과 동시에 지정
# scores = pd.Series(scores, index=names) #한번에

# 인덱스를 나중에 지정하는것도 가능하다
scores = pd.Series(scores)
scores.index = names

# 3. 완성된 Series를 출력하세요.
print(scores, "\n")

# 4. `김철수`의 점수를 출력하세요.
# print(scores[1]) #에러(인덱스가 변경됨)
print(scores["김철수"]) # 약식 표현
print(scores.loc["김철수"]) # 인덱스를 이용한 표현
print(scores.iloc[1]) # 위치를 이용한 표현

print()

# 5. `박민수`의 점수를 80점으로 변경하세요.
scores["박민수"] = 80
print(scores, "\n")

# 6. 80점 이상인 학생들의 점수만 출력하세요.
print(scores[scores >= 80], "\n")
print(scores.loc[scores >= 80], "\n")

# 7. 전체 학생의 평균 점수를 출력하세요.
print(scores.mean(), "\n")

# 8. 90점 이상인 학생이 몇 명인지 출력하세요.
# print(scores[scores >= 90])
# print(len(scores[scores >= 90]))
print(scores[scores >= 90].size) #권장하는 명령
# print((scores >= 90).sum()) #논리로 바꿔서 1(True)의 합계 구하기
# print(scores[scores >= 90].count()) #count는 결측치는 제외하고 셈

