"""
데이터프레임을 만드는 또 다른 방법

- dictionary에서 만드는 방법
"""

import pandas as pd

names = ["피카츄", "라이츄", "파이리", "꼬부기"]
data = {
    # "이름" : 데이터
    "국어" : [85, 70, 90, 60],
    "영어" : [90, 80, 85, 75],
    "수학" : [75, 95, 100, 80]
}

df = pd.DataFrame(data, index=names)
print(df)

# 데이터프레임을 원하는 조건으로 필터링

# 1. 전체 점수에서 80점 이상인지 비교하여 논리로 변환
print(df >= 80, "\n")

# 2. 1번에서 True인 데이터만 조회
# (참고) NaN은 Not a Number의 줄임말 (숫자가 아니라는 뜻)
print(df[df >= 80], "\n")

# 3. 국어점수가 80점 이상인 경우를 조회
print(df["국어"] >= 80, "\n")
print(df[df["국어"] >= 80], "\n")

# print(df.loc["국어"] >= 80, "\n")    # 에러
print(df.loc[df["국어"] >= 80], "\n")
print(df.loc[df["국어"] >= 80, :], "\n")

# 나눠서 사용하면...
condition = df["국어"] >= 80
print(df.loc[condition, :], "\n")

# 영어가 60 이상 90 미만인 학생 조회
# condition = 60 <= df["영어"] <= 90    # 파이썬에서만 가능
condition = (60<= df["영어"]) & (df["영어"] < 90)
print(df[condition], "\n")  # best
print(df.loc[condition], "\n")
print(df.loc[condition, :], "\n")

# 영어와 수학이 모두 80점 이상인 학생의 전체 성적 조회
condition = (df["영어"] >= 80) & (df["수학"] >= 80)
print(df[condition], "\n")  # best
print(df.loc[condition], "\n")
print(df.loc[condition, :], "\n")

print(len(df[condition]), "\n")
print(df[condition].shape, "\n")
print(df[condition].shape[0], "\n")


