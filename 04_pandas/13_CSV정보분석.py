# ## 제한사항
#
# - for, while, if를 사용하지 않습니다.
# - Pandas의 기능을 최대한 활용합니다.
# - loc, iloc, 불리언 인덱싱을 활용합니다.
# - sum, mean, count, max, min을 활용합니다.
# - groupby, clip, drop을 활용합니다.
# - 원본 CSV 파일은 변경하지 않습니다.
# - 각 문제는 앞선 문제의 결과를 이어서 사용합니다.
# - 원본 열을 변경한 경우 관련 계산 열도 다시 계산합니다.

import pandas as pd

df = pd.read_csv("./data/products.csv")
print(df)
print("-"*70, "\n")


# 1. 전체 상품의 개수를 출력하세요.
print(f"전체 상품 개수 : {df.shape[0]}개")
print(f"전체 상품 개수 : {len(df)}개")     # print(len(df), "\n")
print("-"*70)

# 2. 상품의 분류 종류를 중복 없이 출력하세요.
print(df.groupby("분류").groups.keys())
print(df["분류"].nunique())
print("-"*70)

# 3. 전체 상품의 평균 판매가를 출력하세요.
print(f"평균 판매가 : {df["판매가"].mean():,.0f}")
print(df["판매가"].mean())
print("-"*70)

# 4. 판매가가 50,000원 이상인 상품을 출력하세요.
condition = df["판매가"] >= 50000
print(df.loc[condition, ["상품명"]])
print("-"*70)

# 5. 전자제품 중 판매가가 50,000원 이하인 상품을 출력하세요.
condition = (df["분류"] == "전자제품") & (df["판매가"] <= 50000)
print(df.loc[condition, ["상품명"]])
print("-"*70)

# 6. 현재 판매중인 상품의 개수를 출력하세요.
condition = df["상태"] == "판매중"
print(len(df.loc[condition]))
print("-"*70)

# 7. 입고수량과 판매수량을 이용하여 '재고수량'이라는 새로운 열을 생성하세요.
df["재고수량"] = df["입고수량"] - df["판매수량"]
print(df)
print("-"*70)

# 8. 판매가와 할인율을 이용하여 '할인가'라는 새로운 열을 생성하세요.
# df["할인가"] = df["판매가"] - 할인금액
df["할인가"] = df["판매가"] - df["판매가"] * df["할인율"] / 100
df["할인가"] = df["할인가"].astype(int)
df["할인가"] = (df["판매가"] - df["판매가"] * df["할인율"] / 100).clip(lower=0).astype(int)
# df[""할인가] = df["할인가"].round()     # 반올림만 하고 타입은 유지
print(df)
print("-"*70)

# 9. 할인가와 판매수량을 이용하여 '매출액'이라는 새로운 열을 생성하세요.
df["매출액"] = df["할인가"] * df["판매수량"]
print(df)
print("-"*70)

# 10. 원가, 할인가, 판매수량을 이용하여 '순이익'이라는 새로운 열을 생성하세요.  (기타 비용은 고려하지 않습니다.)
df["순이익"] = (df["할인가"] - -df["원가"]) * df["판매수량"]
# df["순이익"] = df["매출액"] - df["원가"] * df["판매수량"]
print(df)
print("-"*70)

# 11. 재고수량이 0인 품절 상품을 출력하세요.
condition = df["재고수량"] == 0
print(df.loc[condition, ["상품명"]])
print("-"*70)

# 12. 재고수량이 입고수량의 10% 이하인 상품을 출력하세요.
condition = df["재고수량"] / df["입고수량"] <= 0.1
print(df[condition])    # print(df.loc[condition, ["상품명"]]) → 상품명만 출력
print("-"*70)

# 13. 할인율이 20% 이상이고 현재 판매중인 상품을 출력하세요.
condition = (df["할인율"] >= 20) & (df["상태"] == "판매중")
print(df[condition])
print("-"*70)

# 14. 순이익이 100,000원 이상인 상품을 출력하세요.
condition = df["순이익"] >= 100000
print(df[condition])
print("-"*70)

# 15. 분류별 상품 개수를 출력하세요.
group1 = df.groupby("분류")
print("분류별 상품 개수", group1.size())
print("-"*70)

# 16. 분류별 평균 판매가를 출력하세요.
print(group1["판매가"].mean())
# print(group1["판매가"].mean().mean())  # 전체 평균
print("-"*70)

# 17. 분류별 총 판매수량을 출력하세요.
print(group1["판매수량"].sum())
# print(group1["판매수량"].sum().sum())  # 전체 합계
print("-"*70)

# 18. 분류별 총 재고수량을 출력하세요.
print(group1["재고수량"].sum())
print("-"*70)

# 19. 지점별 총 매출액을 출력하세요.
group2 = df.groupby("지점")
print(group2["매출액"].sum())
# print(group2["매출액"].sum().map("{:,}".format))  → map을 이용하면 천단위로 콤마(,)를 찍을 수 있다.
print("-"*70)

# 20. 지점별 총 순이익을 출력하세요.
print(group2["순이익"].sum().map("{:,}".format))
print("-"*70)

# 21. 판매중인 상품만 대상으로 분류별 평균 판매가를 출력하세요.
condition = df["상태"] == "판매중"
on_sale = df[condition]    # 판매중만 필터링
print(on_sale.groupby("분류")["판매가"].mean().astype(int))
print("-"*70)

# 22. 품절 상품만 대상으로 지점별 품절 상품 개수를 출력하세요.
condition = df["재고수량"] == 0
soldout = df[condition]
print(soldout.groupby("지점").size())
print("-"*70)

# 23. 상품코드가 P0001인 상품의 판매가를 5,000원으로 변경하세요.
df.loc["P0001", "판매가"] = 5000
print(df.loc["P0001"])
print("-"*70)

# 24. 전자제품의 할인율을 모두 15%로 변경하세요.
condition = df["분류"] == "전자제품"
df.loc[condition, "할인율"] = 15
print(df[condition])
print("-"*70)

# 25. 모든 상품의 할인율이 20%를 초과하지 않도록 제한하세요.
# → clip() 사용  (상한선)
condition = df["할인율"] > 20
print("before", df[df["할인율"] > 20].shape[0])
df["할인율"] = df["할인율"].clip(upper=20)
print("after", df[df["할인율"] > 20].shape[0])
print("-"*70)

# 26. 판매수량이 입고수량을 초과하지 않도록 제한하세요.
df.loc["P0128", "판매수량"] = 99999999
condition = df["판매수량"] > df["입고수량"]
print("before", df[condition].shape[0])
df["판매수량"] = df["판매수량"].clip(upper=df["입고수량"])
condition = df["판매수량"] > df["입고수량"]
print("after", df[condition].shape[0])
print("-"*70)

# 27. 판매중지 상태인 상품을 모두 제거하세요.
print("before", df.shape[0])
condition = df["상태"] == "판매중지"
df = df.drop(index=df[condition].index)
print("after", df.shape[0])
print("-"*70)

# 28. 변경된 상품 정보를 products_result.csv로 저장하세요.
df.to_csv(
    "./data/products_result.csv",
    encoding="utf-8-sig",
    index_label="상품코드"
)
print("저장 완료")

