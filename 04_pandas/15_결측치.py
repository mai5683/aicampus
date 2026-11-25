"""
결측치에 대한 처리

값이 비어있거나 누락된 상태를 결측치라고 합니다.

결측치는 왜 생기나?
1. csv 자체에 비어있는 값이 존재하는 경우
2. 인덱스가 서로 다른 DataFrame, Series끼리 연산하면 발생
3. 데이터 변환에 실패한 경우 (ex : 문자열 → 숫자)
   - "100" → 100
   - "85" → 85
   - "미응시" → NaN
   - "오류" → NaN
4. 정상적인 연산 결과가 나오지 않는 경우
   - 10 / 2 = 5
   - 10 / 0 = error
   - 0 / 0 = NaN
   - NaN + 5 = NaN

결측치의 종류 및 탐지방법은?
   - None : 파이썬에서 값이 없음을 나타내는 방법
   - np.nan : NumPy 결측치
   - pd.NA : Pandas 결측치
   - pd.NaT : 날짜 및 시간 결측치
"""


import pandas as pd

df = pd.DataFrame({
    "이름" : ["피카츄", "라이츄", "파이리", "꼬부기"],
    "국어" : [80, 90, None, 70],
    "수학" : [70, None, 90, 80]
})

print(df, "\n")


# -----------------------------------------------
# 결측치 확인
# -----------------------------------------------
# df.isna() - 결측치의 위치 확인 (True면 결측치)
print(df.isna())

# (Q) 결측치 개수는?
print("결측치 개수", df.isna().sum(), "\n")          # 항목별로 찾기
print("결측치 개수", df.isna().sum().sum(), "\n")    # 합한 개수 찾기

# -----------------------------------------------
# 결측치 제거
# -----------------------------------------------
# - df.dropna()
# - 원본은 제거되지 않음
drop_result = df.dropna()
print(drop_result, "\n")

drop_result = df.dropna(subset=["국어"])   # "국어"의 결측치만 제거
print(drop_result, "\n")

drop_result = df.dropna(subset=["수학"])   # "수학"의 결측치만 제거
print(drop_result, "\n")


# -----------------------------------------------
# 결측치를 다른 값으로 채우기
# -----------------------------------------------
# - (위험! - 원래 데이터가 오염될 수도 있다.)
# - df.fillna(값)

fill_result = df.copy()     # 원본을 지키기 위해 복사
# fill_result["국어"] = fill_result["국어"].fillna(0)     # "국어" 결측치 → 0
# fill_result["수학"] = fill_result["수학"].fillna(0)     # "수학" 결측치 → 0
fill_result[["국어", "수학"]] = fill_result[["국어", "수학"]].fillna(0)
print(fill_result, "\n")

# 결측치를 평균으로 채우기
mean_result = df.copy()
# mean_result["국어"] = mean_result["국어"].fillna(mean_result["국어"].mean())
# mean_result["수학"] = mean_result["수학"].fillna(mean_result["수학"].mean())
mean_result[["국어", "수학"]] = mean_result[["국어", "수학"]].fillna(mean_result[["국어", "수학"]].mean())
print(mean_result, "\n")


