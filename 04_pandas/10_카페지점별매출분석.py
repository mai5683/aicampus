"""
# Pandas 실습 문제 — 카페 지점별 매출 분석

한 카페 브랜드에서 강남점, 홍대점, 잠실점의 주문 내역을 관리하고 있습니다.
본사에서는 각 지점의 매출을 분석하기 위해 다음 자료를 전달했습니다.

## 제한사항

- `for`, `while`, `if`를 사용하지 않습니다.
- 배운 Pandas의 조건 필터링, 열 추가, `sum()`, `mean()`, `max()`, `count()`, `groupby()`를 활용합니다.
- 취소된 주문은 실제 매출에 포함하면 안 됩니다.
- `sort_values()`, `agg()` 등 배우지 않은 함수는 사용할 필요가 없습니다.
"""

## 기본 데이터

import pandas as pd

df = pd.DataFrame({
    "지점": ["강남", "홍대", "강남", "잠실", "홍대", "잠실", "강남", "홍대"],
    "메뉴": ["아메리카노", "라떼", "라떼", "아메리카노",
           "에이드", "라떼", "에이드", "아메리카노"],
    "가격": [3000, 4500, 4500, 3000, 5000, 4500, 5000, 3000],
    "수량": [2, 1, 3, 4, 2, 1, 1, 5],
    "상태": ["완료", "완료", "취소", "완료",
           "완료", "완료", "완료", "취소"]
}, index=[
    "주문1", "주문2", "주문3", "주문4",
    "주문5", "주문6", "주문7", "주문8"
])

print(df, "\n")


# ## 요구사항

# **1. 주문 금액 계산**
# # 각 주문의 `가격 × 수량`을 계산하여 `주문금액`이라는 새로운 열을 생성하세요.
df["주문금액"] = df["가격"] * df["수량"]
print(df, "\n")

# **2. 정상 주문 확인**
# 주문 상태가 `"완료"`인 주문만 추출하여 `completed`라는 변수에 저장하세요.
# completed = df["상태"] == "완료"
# print(df.loc[completed], "\n")
condition = df["상태"] == "완료"
completed = df[condition]
print(completed, "\n")

# **3. 지점별 매출 분석**
# 취소된 주문을 제외하고, 지점별 주문금액 합계를 출력하세요.
condition = df["상태"] != "취소"
df = df.loc[condition]
print(df.groupby("지점")["주문금액"].sum(), "\n")

# **4. 지점별 평균 주문금액**
# 정상 주문만 대상으로 지점별 주문금액의 평균을 출력하세요.
print(df.groupby("지점")["주문금액"].mean(), "\n")
print(df.groupby("지점")["주문금액"].mean().astype(int), "\n")

# **5. 지점별 주문 건수**
# 각 지점에서 완료된 주문이 몇 건인지 계산하세요.
print(df.loc[condition].groupby("지점")["주문금액"].count(), "\n")  # None을 카운팅하지 않음
print(df.loc[condition].groupby("지점")["주문금액"].size(), "\n")   # None을 카운팅함
print(df.loc[condition].groupby("지점").size(), "\n")             # None을 카운팅함

# **6. 지점별 판매 수량**
# 정상 주문만 대상으로 각 지점에서 판매한 총 수량을 출력하세요.
condition = df["상태"] == "완료"
print(completed.groupby("지점")["수량"].sum(), "\n")
print(df.loc[condition].groupby("지점")["수량"].sum(), "\n")

# **7. 메뉴별 판매 분석**
# 정상 주문을 대상으로 메뉴별 판매 수량의 합계를 출력하세요.
print(completed.groupby("메뉴")["수량"].sum(), "\n")

# **8. 본사 매출 보고서**
# 정상 주문만을 기준으로 다음 정보를 출력하세요.

# - 전체 매출 합계
# - 완료된 주문의 총개수
# - 전체 정상 주문의 평균 주문금액
# - 한 번의 주문에서 발생한 최대 주문금액
print(f"전체 매출 합계 : {completed["주문금액"].sum():,}원")
print(f"완료된 주문 개수 : {completed.shape[0]}개")
# print(f"완료된 주문 개수 : {len(completed)}개")
print(f"평균 주문 금액 : {completed["주문금액"].mean():,.0f}원")
print(f"최대 주문 금액 : {completed["주문금액"].max():,}원")
print()

# ## 추가 도전 문제

# **9. 고액 주문 분석**
# 주문 상태가 `"완료"`이고 주문금액이 10,000원 이상인 주문만 추출하세요.
# 이 주문들을 지점별로 묶어 주문금액 합계를 계산하세요.
# condition = (df["상태"] == "완료") & (df["주문금액"] >= 10000)
condition = completed["주문금액"] >= 10000
high_orders = completed[condition]
print(high_orders, "\n")
# print(completed[condition], "\n")
print(high_orders.groupby("지점")["주문금액"].sum())
# print(completed[condition].groupby("지점")["주문금액"].sum())

