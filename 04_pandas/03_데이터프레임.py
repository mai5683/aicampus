"""
데이터프레임(DataFrame)

행과 열이 존재하는 2차원 표를 저장하는 도구
- index : 각 행을 구분하는 이름표
- columns : 각 열의 이름
- shape : (행 개수, 열 개수) 튜플 정보
- dtypes : 각 열의 자료형
"""

import numpy as np
import pandas as pd

# 데이터 준비 - 행, 열, 데이터
names = ["피카츄", "라이츄", "파이리", "꼬부기"]
subject = ["국어", "영어", "수학"]
scores = [
    [85, 90, 75],
    [70, 80, 95],
    [90, 85, 100],
    [60, 75, 80]
]

# DataFrame 생성

# (1) 생성 후 인덱스와 컬럼을 설정
# df_scores = pd.DataFrame(scores)
# df_scores.index = names
# df_scores.columns = subject

# (2) 생성과 동시에 인덱스, 컬럼을 설정
df_scores = pd.DataFrame(scores, index=names, columns=subject)

print(df_scores, "\n")

# 정보 분석
print(df_scores.index)
print(df_scores.columns)
# print(df_scores.ndim)   # 차원 (무조건 2)
print(df_scores.shape)  # 2차원(행, 열)
print(df_scores.dtypes) # 열별 자료형
print(df_scores.size)   # 데이터 개수
print(len(df_scores))   # 행의 개수 (가장 높은 차원의 개수)

# NumPy로 변환 (index, columns는 사라짐)
print(df_scores.to_numpy())

print()

# 특정 항목을 출력
# - 약식으로 호출하면 무조건 열이름으로 인식
# print(df_scores["피카츄"])   # 에러
print(df_scores["국어"])      # 가능

# - 보고 싶은 열이 두 개 이상이면...
# print(df_scores["국어", "영어"])    # 에러 (콤마가 차원구분 기호로 오해)
print(df_scores[["국어", "영어"]])    # 가능

print()

# loc 사용 (설정된 행과 열의 정보를 이용해서 데이터를 탐색)
# .loc[행정보, 열정보]
print(df_scores.loc["피카츄"], "\n")
print(df_scores.loc["피카츄", "국어"], "\n")
print(df_scores.loc["피카츄":"파이리", "수학"], "\n")   # 마지막 포함

# iloc 사용 (배열의 기본 인덱스에 의한 데이터 탐색)
# .iloc[행위치, 열위치]
print(df_scores.iloc[0], "\n")    # df_scores.loc["피카츄"]
print(df_scores.iloc[-1], "\n")
print(df_scores.iloc[1:3], "\n")  # 마지막 미포함

print(df_scores.iloc[1, 2])       # 행, 열 모두 지정
# (Q) 수학 점수만 확인
print(df_scores.iloc[:, 2], "\n")   # 행 무관, 열
print(df_scores.iloc[:, -1], "\n")  # 행 무관, 열



