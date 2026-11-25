"""
학습에 사용할 데이터가 정상저인지 검사

정상적이라 함은...
- 결측치가 없어야 하고
- 이상치도 없어야 하고
- 중복도 없어야 하고
- 범주 내에 포함되어 있어야 하고
"""

import pandas as pd

# 기초 데이터 생성 (행 기준 데이터)
data = [
    {"filename":"001.png", "brightness":120, "area":1500, "result":"good"},
    {"filename":"002.png", "brightness":135, "area":1800, "result":"good"},
    {"filename":"003.png", "brightness":110, "area":1600, "result":"good"},
    {"filename":"004.png", "brightness":None, "area":1700, "result":"good"},
    {"filename":"005.png", "brightness":125, "area":None, "result":"defect"},
    {"filename":"006.png", "brightness":250, "area":9500, "result":"defect"},
    {"filename":"002.png", "brightness":135, "area":1800, "result":"good"},
    {"filename":"002.png", "brightness":126, "area":1550, "result":"good"}
]

df = pd.DataFrame(data)
print(df, "\n")


# 데이터의 전체 구조 확인 명령
# - df.info()
# - non-null count : 결측치가 아닌 실 데이터의 개수
# - Dtype : 컬럼의 자료형
df.info()
print()

# 데이터 통계 확인
# - df.describe()
# - count : 결측치 제외한 데이터 수
# - mean : 평균
# - std : 표준편차
# - min : 최소값
# - max : 최대값
# - 25%, 50%, 75% : 각각의 구간에 해당하는 값 (4분위수)
# - IQR(Interquatile Range, 사분위 범위)
# - 데이터를 크기순으로 정렬했을 때 가운데 50%를 말하는 것
# - 이상치(Outlier)를 탐지하기 위한 기준으로 사용한다.
# - 25%를 Q1(제1사분위수), 50%를 Q2, 75%를 Q3이라고 부름.
# - IQR = Q3 - Q1
# - 정상값의 하한값은 Q1 - 1.5 x IQR 이라고 본다.
# - 정상값의 상한값은 Q3 + 1.5 x IQR 이라고 본다.
print(df.describe(), "\n")

# 결측치 비율 계산
print(df.isna())
print(df.isna().sum())
print(df.isna().mean())
print()

# 중복 데이터 확인
# - 아무 옵션이 없으면 처음을 중복이 아니라고 판정
print(df.duplicated(), "\n")
print(df.duplicated(keep="first"), "\n")
# - 마지막을 중복이 아니라고 판정
print(df.duplicated(keep="last"), "\n")
# - 전부 다 중복이라고 판정
print(df.duplicated(keep=False), "\n")

# (Q) 중복된 데이터만 조회
condition = df.duplicated(keep=False)
# condition = df.duplicated(keep="first") → 마지막이 중복이라고 판정
# condition = df.duplicated(keep="last")  → 처음이 중복이라고 판정
print(df[condition], "\n")

# 특정 항목만 중복이어도 조회
condition = df.duplicated(subset=["filename"], keep=False)
print(df[condition], "\n")

# 중복된 항목 제거
# - df.drop_duplicates(subset, keep)
# - 사본 생성됨

# (Q) 정상치를 벗어난 데이터를 조회
# 정상치의 기준 : Q1 - 1.5*IQR 부터 Q3 + 1.5*IQR 까지
# df.quantile(비율) : 비율은 0~1 사이 값으로 설정
# print(df["brightness"].quantile(0.25))
# print(df["brightness"].quantile(0.5))
# print(df["brightness"].quantile(0.75))
Q1 = df["brightness"].quantile(0.25)
Q3 = df["brightness"].quantile(0.75)

IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
condition = (df["brightness"] < lower) | (df["brightness"] > upper)
print("밝기 이상치 데이터")
print(df[condition], "\n")

Q1 = df["area"].quantile(0.25)
Q3 = df["area"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
condition = (df["area"] < lower) | (df["area"] > upper)
print("면적 이상치 데이터")
print(df[condition], "\n")


