"""
데이터 정렬

정렬(sort)은 특정 기준에 따라 데이터의 순서를 바꾸는 작업을 의미한다.
- 오름차순(ascending) → 줄여서 asc : 데이터를 기준에 따라 가장 작은 것부터 나열 (번호순, 이름순, ...)
- 내림차순(descending) → 줄여서 desc : 데이터를 기준에 따라 가장 큰 것부터 나열 (성적순, 최신순, ...)

Pandas에서는 sort_values()로 정렬을 수행한다.
(중요) 정렬의 결과는 사본으로 생성된다.
"""

import pandas as pd

df = pd.DataFrame({
    "제품번호": ["A001", "A002", "B001", "B002", "A003"],
    "생산라인": ["A", "A", "B", "B", "A"],
    "무게": [100.5, 98.2, 102.4, 105.3, 99.8],
    "불량개수": [2, 5, 1, 5, 3]
})

print("<원본>")
print(df, "\n")

print("<무게 오름차순>")
print(df.sort_values("무게"))    # 옵션이 없으면 기본적으로 오름차순
print(df.sort_values("무게", ascending=True), "\n")

print("<무게 내림차순>")
print(df.sort_values("무게", ascending=False), "\n")

# 두 가지 항목으로 정렬
print("<불량 많은 순 (같으면 무게 적은 순)>")
# result = df.sort_values("항목", 정렬방식)
result = df.sort_values(
    ["불량개수", "무게"],
    ascending=[False, True]
)
print(result, "\n")

# 인덱스 재설정 (사본 생김)
# - 과거의 인덱스를 남겨주는 것이 기본 옵션
# - 제거하고 싶다면 drop=True 설정
print("<설정 전>")
print(result.iloc[0], "\n")

print("<인덱스 재설정>")
result = result.reset_index()
# result = result.reset_index(drop=True)
print(result, "\n")

print("<설정 후>")
print(result.iloc[0], "\n")
# 확인 결과 reset_index()와 iloc는 상관이 없다.

# 원본은 잘 있나?
print("<원본>")
print(df, "\n")


