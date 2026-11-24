"""
데이터 집계 (Aggregation)

여러 데이터에서 합계나 평균처럼 요약된 값을 계산하는 작업
"""

import pandas as pd

df = pd.DataFrame({
    "분류": ["음료", "과자", "음료", "식품", "과자", "음료", "식품", "과자"],
    "가격": [2000, 1500, 3500, 4500, 2500, 1800, 6000, 1200],
    "재고": [15, 3, 0, 8, 2, 20, 1, 12],
    "판매량": [30, 45, 25, 12, 38, 50, 10, 60]
}, index=[
    "콜라", "새우깡", "에너지드링크", "도시락",
    "초코파이", "생수", "샌드위치", "껌"
])

print(df, "\n")

# 전체 상품의 판매량 합계
print(df["판매량"].sum())

# 전체 상품의 평균 가격
print(df["가격"].mean())

# 가장 비싼 상품의 가격
print(df["가격"].max())

# 가장 저렴한 상품의 가격
print(df["가격"].min())

print()
# 집계는 꼭 전체에서만 이루어지는 것은 아니다.
# 공통적으로 많이 등장하는 값(ex : 카테고리, 성별, 등급, ...)으로도 가능
# groupby 명령으로 원하는 그룹을 지정하여 사용한다.
# print(df.groupby("분류"))
# print(df.groupby("분류")["판매량"])
print(df.groupby("분류")["판매량"].sum())
print(df.groupby("분류")["판매량"].mean())
print(df.groupby("분류")["판매량"].max())
print(df.groupby("분류")["판매량"].min())
print(df.groupby("분류")["판매량"].count())  # 종류(가지수), 결측치(None)은 제외하고 셈

print()

# (Q) 분류별 판매량과 재고의 합계를 출력하세요.
print(df.groupby("분류").groups.keys(), "\n")
print(df.groupby("분류").obj.columns, "\n")

print(df.groupby("분류")[["판매량", "재고"]].sum())



