"""
# Pandas 실습 — 공장 검사 데이터 관리

파일명 : `16_공장검사데이터관리.py`

한 공장에서 생산한 부품의 무게와 검사 결과를 관리하고 있습니다.
일부 부품은 측정값이 누락되었으며, 불량품도 포함되어 있습니다.
다음 요구사항에 따라 검사 데이터를 정리하고 분석하세요.

## 제한사항

- `for`, `while`, `if`는 사용하지 않습니다.
- 현재까지 배운 Pandas 기능만 사용합니다.
- 원본 데이터와 결측치를 제거한 데이터는 서로 구별하여 관리하세요.
"""


## 기본 데이터

import pandas as pd

df = pd.DataFrame({
    "제품번호": ["A001", "A002", "B001", "B002", "A003", "B003", "A004"],
    "생산라인": ["A", "A", "B", "B", "A", "B", "A"],
    "무게": [100.5, 98.2, None, 105.3, 101.1, None, 99.8],
    "검사결과": ["정상", "정상", "불량", "정상", "불량", "정상", "정상"]
})

print(df)

# 파일 경로(절대경로)를 여러 가지 이유로 직접 구해야 하는 경우가 있다.


#-------------------------------------------------------------------
# **1. 데이터 저장**
# DataFrame을 `data/inspection.csv`라는 파일로 저장하세요.
# - 디렉터리가 존재하지 않으면 Path를 이용하여 생성합니다.
# - 행 인덱스는 저장하지 않습니다.
# - 한글 데이터가 깨지지 않도록 인코딩을 지정합니다.
df.to_csv("./data/inspection.csv", encoding="utf-8-sig", index=False)
print("CSV 저장 완료")

# **2. 데이터 불러오기**
# 저장한 CSV 파일을 다시 불러와 `data` 변수에 저장하세요.
data = pd.read_csv("./data/inspection.csv")
print(data)

# **3. 데이터 확인**
# 불러온 데이터의 처음 5행, 행과 열의 개수, 열별 자료형을 출력하세요.
print(data.head(), "\n")
print(data.head(5), "\n")
print(data.iloc[:5], "\n")
# print(data.shpae, , "\n")
rows, cols = data.shape     # cols = columns 줄임말로 많이 사용한다.
print(f"행 개수 = {rows}, 열 개수 = {cols}")
print(data.dtypes)
print()

# **4. 누락된 데이터 확인**
# 각 열에 결측치가 몇 개 있는지 출력하세요.
print(data.isna().sum())
print()

# **5. 결측치 제거**
# 무게 측정값이 없는 제품을 제외한 DataFrame을 `clean` 변수에 저장하세요.
# clean = data.dropna()
clean = data.dropna(subset=["무게"])
print(clean, "\n")

# **6. 정상 제품 추출**
# `clean`에서 검사 결과가 `"정상"`인 제품만 추출하세요.
condition = clean["검사결과"] == "정상"
print(clean[condition], "\n")

# **7. 생산라인별 분석**   → '~~별'이 나오면 무조건 group
# 결측치를 제거한 `clean`을 기준으로 생산라인별 평균 무게를 출력하세요.
print(clean.groupby("생산라인")["무게"].mean(), "\n")

# **8. 불량품 확인**
# 원본 `data`에서 검사 결과가 `"불량"`인 제품의 제품번호와 생산라인만 출력하세요.
condition = data["검사결과"] == "불량"
print(data.loc[condition, ["제품번호", "생산라인"]])

# **9. 데이터 수정**
# `clean`의 `A002` 제품 무게가 잘못 기록된 것을 발견했습니다.
# 해당 제품의 무게를 `99.5`로 수정하세요.
# ※ 제품번호 열의 값을 조건으로 사용하세요.
condition = clean["제품번호"] == "A002"
clean.loc[condition, "무게"] == 99.5      # clean.loc["A002"] 로 쓸 수 없다. index가 없기 때문에!
print(clean, "\n")

# **10. 결과 파일 저장**
# 수정을 마친 `clean` DataFrame을 `inspection_result.csv`로 저장하세요.
clean.to_csv(
    "./data/inspection.csv",
    index=False,
    encoding="utf-8-sig"
)
print("저장 완료")

