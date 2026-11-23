"""
Pandas 실습 문제 — DataFrame 데이터 선택
다음은 학생 5명의 국어, 영어, 수학 점수를 저장한 NumPy 배열입니다.

import numpy as np
import pandas as pd

scores = np.array([
    [85, 90, 75],
    [70, 80, 95],
    [90, 85, 100],
    [60, 75, 80],
    [95, 70, 85]
])

예상 DataFrame
| | 국어 | 영어 | 수학 |
|---|---:|---:|---:|
| 홍길동 | 85 | 90 | 75 |
| 김철수 | 70 | 80 | 95 |
| 이영희 | 90 | 85 | 100 |
| 박민수 | 60 | 75 | 80 |
| 최지우 | 95 | 70 | 85 |

※ 모든 문제는 loc, iloc 또는 열 선택 문법을 사용하여 해결하세요. 반복문이나 조건문은 사용하지 않습니다.
"""

import numpy as np
import pandas as pd

scores = np.array([
    [85, 90, 75],
    [70, 80, 95],
    [90, 85, 100],
    [60, 75, 80],
    [95, 70, 85]
])

# 요구사항

# 1. scores 배열을 DataFrame으로 변환하세요.
# 2. 행 인덱스를 홍길동, 김철수, 이영희, 박민수, 최지우로 지정하세요.
# 3. 열 이름을 국어, 영어, 수학으로 지정하세요.
# 4. 완성된 DataFrame을 출력하세요.
names = ["홍길동", "김철수", "이영희", "박민수", "최지우"]
subject = ["국어", "영어", "수학"]
df_scores = pd.DataFrame(scores, index=names, columns=subject)
print(df_scores, "\n")

# 5. 모든 학생의 국어 점수를 출력하세요.
print(df_scores["국어"], "\n")

# 6. 영어와 수학 점수만 DataFrame 형태로 출력하세요.
print(df_scores[["영어", "수학"]], "\n")

# 7. 김철수의 모든 과목 점수를 출력하세요.
print(df_scores.loc["김철수"], "\n")

# 8. 이영희의 수학 점수만 출력하세요.
print(df_scores.loc["이영희", "수학"], "\n")

# 9. 홍길동부터 이영희까지의 모든 점수를 출력하세요.
print(df_scores.loc["홍길동":"이영희"], "\n")

# 10. 김철수부터 박민수까지의 국어와 영어 점수만 출력하세요.
print(df_scores.loc["김철수":"박민수", ["국어", "영어"]], "\n")

# 11. 첫 번째 학생의 모든 점수를 출력하세요.
print(df_scores.iloc[0], "\n")

# 12. 마지막 학생의 모든 점수를 출력하세요.
print(df_scores.iloc[-1], "\n")

# 13. 세 번째 학생의 두 번째 과목 점수만 출력하세요.
print(df_scores.iloc[2, 1], "\n")

# 14. 처음 세 학생의 모든 점수를 출력하세요.
print(df_scores.iloc[:3], "\n")

# 15. 마지막 두 학생의 국어와 수학 점수만 출력하세요.
print(df_scores.iloc[-2:, [0, 2]], "\n")

# 추가 도전 문제

# 16. loc를 사용하여 홍길동과 최지우의 수학 점수만 출력하세요.
print(df_scores.loc[["홍길동", "최지우"], "수학"], "\n")

# 17. iloc를 사용하여 모든 학생의 국어와 수학 점수만 출력하세요.
print(df_scores.iloc[:, [0, 2]], "\n")

# 18. loc와 iloc를 각각 사용하여 박민수의 영어 점수를 출력하세요.
print(df_scores.loc["박민수", "영어"])
print(df_scores.iloc[-2, 1])


