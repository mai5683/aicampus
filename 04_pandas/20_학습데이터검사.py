"""
# Pandas 실습 — Vision AI 학습 데이터 품질 검사

파일명 : `20_학습데이터검사.py`

한 제조업체에서 제품의 정상 및 불량 여부를 판별하기 위해 이미지에서 추출한 특징 데이터를 관리하고 있습니다.
`data/vision_inspection.csv` 파일에는 데이터 수집 과정에서 발생한 결측치, 중복 데이터, 이상치 등이 포함되어 있습니다.
다음 요구사항에 따라 학습 데이터를 검사하고 정제하세요.

1. vision_inspection.csv 파일을 불러오고 전체 데이터의 구조와 기초 통계 정보를 출력하세요.
2. 각 열의 결측치 개수와 결측치 비율을 출력하세요. 비율은 백분율(%)로 출력합니다.
3. 모든 열의 값이 동일한 중복 데이터를 출력하세요. 최초로 등장한 데이터도 포함합니다.
4. 검사 결과(result)가 good 또는 defect가 아닌 데이터를 모두 출력하세요.
5. 파일명(filename)이 중복된 데이터를 모두 출력하세요. 다른 열의 값은 고려하지 않습니다.
6. 다음 조건 중 하나라도 해당하는 데이터를 출력하세요.
   - 밝기가 0~255 범위를 벗어남
   - 면적이 0 이하
   - 둘레가 0 이하
7. 결측치가 하나라도 포함된 행을 모두 제거하세요.
8. 4번과 6번의 조건에 해당하는 데이터를 제거하세요.
9. 파일명이 중복된 데이터를 제거하세요. 최초로 등장한 데이터만 유지합니다.
10. 현재 데이터를 기준으로 밝기, 면적, 둘레의  IQR과 이상치 판별 범위(하한값, 상한값)를 출력하세요.
11. 밝기, 면적, 둘레 중 하나라도 IQR 기준을 벗어난 데이터를 모두 출력한 후 제거하세요.
12. 최초 데이터의 개수, 제거된 데이터의 개수, 남아 있는 데이터의 개수와 비율을 출력하세요.
13. 생산라인별 불량률을 계산하여 출력하세요. 불량률이 높은 순서대로 정렬하고, 불량이 없는 생산라인은 `0%`로 출력하세요.
14. 전체 데이터를 면적이 큰 순으로 정렬하세요. 면적이 같다면 밝기가 낮은 순으로 정렬하세요. 이후 인덱스를 `0`부터 시작하도록 재설정하세요. 기존 인덱스는 유지하지 않습니다.
15. 최종 데이터에 결측치와 파일명 중복이 없는지 확인하고 `data/inspection_clean.csv`로 저장하세요. 인덱스는 제외하고 저장합니다.

# 제한사항
- for, while, if를 사용하지 않습니다.
- 지금까지 배운 Pandas 기능만 사용합니다.
- 각 문제는 앞선 문제의 결과를 이어서 사용합니다.
- 결측치를 임의의 값으로 채우지 않습니다.
- IQR의 배수는 1.5로 설정합니다.
- 이번 실습에서는 IQR 이상치를 제거 대상으로 간주합니다.
- 원본 CSV 파일을 덮어쓰지 않습니다.
- CSV 파일은 `utf-8-sig` 인코딩으로 저장합니다.
"""

import pandas as pd

# pd.set_option("display.max_rows", None) # 모든 행 출력
pd.set_option("display.max_columns", None) # 모든 열 출력
pd.set_option("display.max_colwidth", None) # 긴 문자열 중간 생략 방지
pd.set_option("display.width", None) # 출력 너비 자동 설정

# 1. vision_inspection.csv 파일을 불러오고 전체 데이터의 구조와 기초 통계 정보를 출력하세요.
df = pd.read_csv(
    "./data/vision_inspection.csv",
    encoding="utf-8-sig"
)
# 12번에서 필요한 최초의 데이터 개수를 미리 저장
origin_count = df.shape[0] # len(df)

# print(df, "\n")
df.info()
print()
print(df.describe())
# print(df.describe(percentiles=[0.1, 0.3, 0.9]))
print()

# 2. 각 열의 결측치 개수와 결측치 비율을 출력하세요. 비율은 백분율(%)로 출력합니다.
# - df.isna()
print(df.isna().sum(), "\n")
print(df.isna().mean(), "\n")
print((df.isna().mean() * 100).round(2), "\n")
print((df.isna().mean() * 100).round(2).astype(str) + "%", "\n")

# 3. 모든 열의 값이 동일한 중복 데이터를 출력하세요. 최초로 등장한 데이터도 포함합니다.
condition = df.duplicated(keep=False)
print(df[condition], "\n")

# 4. 검사 결과(result)가 good 또는 defect가 아닌 데이터를 모두 출력하세요.
condition = (df["result"] != "good") & (df["result"] != "defect")
print(df[condition], "\n")

# (참고) isna()로는 unknown과 error와 같은 범주를 벗어난 값을 잡을 수 없다
condition = df["result"].isna()
print(df[condition], "\n")

# 5. 파일명(filename)이 중복된 데이터를 모두 출력하세요. 다른 열의 값은 고려하지 않습니다.
condition = df.duplicated(subset=["filename"], keep=False)
print(df[condition], "\n")
print("개수", df[condition].shape[0], "\n")

# 6. 다음 조건 중 하나라도 해당하는 데이터를 출력하세요.
#    - 밝기가 0~255 범위를 벗어남
#    - 면적이 0 이하
#    - 둘레가 0 이하
condition = (
    (df["brightness"] < 0) |
    (df["brightness"] > 255) |
    (df["area"] <= 0) |
    (df["perimeter"] <= 0)
)
print(df[condition], "\n")

# 7. 결측치가 하나라도 포함된 행을 모두 제거하세요.
df = df.dropna()
print(df, "\n")

# 8. 4번과 6번의 조건에 해당하는 데이터를 제거하세요.
condition = (df["result"] != "good") & (df["result"] != "defect")
df = df[~condition] # 조건에 해당되지 않는 것만 필터링하여 덮어쓰기

condition = (
    (df["brightness"] < 0) |
    (df["brightness"] > 255) |
    (df["area"] <= 0) |
    (df["perimeter"] <= 0)
)
df = df[~condition] # 조건에 해당되지 않는 것만 필터링하여 덮어쓰기
print(df, "\n")

# 9. 파일명이 중복된 데이터를 제거하세요. 최초로 등장한 데이터만 유지합니다.
df = df.drop_duplicates(subset=["filename"], keep="first")
print(df, "\n")

# 10. 현재 데이터를 기준으로 밝기, 면적, 둘레의  IQR과 이상치 판별 범위(하한값, 상한값)를 출력하세요.
brightness_Q1 = df["brightness"].quantile(0.25)
brightness_Q3 = df["brightness"].quantile(0.75)
brightness_IQR = brightness_Q3 - brightness_Q1
brightness_lower = brightness_Q1 - 1.5 * brightness_IQR
brightness_upper = brightness_Q3 + 1.5 * brightness_IQR
print("밝기 IQR", brightness_IQR)
print("밝기 상한", brightness_upper)
print("밝기 하한", brightness_lower)
print()

area_Q1 = df["area"].quantile(0.25)
area_Q3 = df["area"].quantile(0.75)
area_IQR = area_Q3 - area_Q1
area_lower = area_Q1 - 1.5 * area_IQR
area_upper = area_Q3 + 1.5 * area_IQR
print("면적 IQR", area_IQR)
print("면적 상한", area_upper)
print("면적 하한", area_lower)
print()

perimeter_Q1 = df["perimeter"].quantile(0.25)
perimeter_Q3 = df["perimeter"].quantile(0.75)
perimeter_IQR = perimeter_Q3 - perimeter_Q1
perimeter_lower = perimeter_Q1 - 1.5 * perimeter_IQR
perimeter_upper = perimeter_Q3 + 1.5 * perimeter_IQR
print("둘레 IQR", perimeter_IQR)
print("둘레 상한", perimeter_upper)
print("둘레 하한", perimeter_lower)
print()

# 11. 밝기, 면적, 둘레 중 하나라도 IQR 기준을 벗어난 데이터를 모두 출력한 후 제거하세요.
condition1 = (df["brightness"] < brightness_lower) | (df["brightness"] > brightness_upper)
condition2 = (df["area"] < area_lower) | (df["area"] > area_upper)
condition3 = (df["perimeter"] < perimeter_lower) | (df["perimeter"] > perimeter_upper)
condition = condition1 | condition2 | condition3
print("<이상치 데이터>")
print(df[condition], "\n")
df = df[~condition] # 이상치 데이터 제거

# 12. 최초 데이터의 개수, 제거된 데이터의 개수, 남아 있는 데이터의 개수와 비율을 출력하세요.
current_count = df.shape[0] # len(df)
remove_count = origin_count - current_count
remain_ratio = current_count / origin_count * 100
print(f"데이터 수 : 최초={origin_count}개, 현재={current_count}개, 제거={remove_count}개")
print(f"남은 데이터 비율 = {remain_ratio:.2f}%")
print()

# 13. 생산라인별 불량률을 계산하여 출력하세요. 불량률이 높은 순서대로 정렬하고, 불량이 없는 생산라인은 `0%`로 출력하세요.
condition = df["result"] == "defect"
# defect_count = df[condition].groupby("line").size() #없으면 안나옴
defect_count = condition.groupby(df["line"]).sum() #없어도 0으로나옴
total_count = df.groupby("line").size()
print(defect_count, "\n")
print(total_count, "\n")
defect_ratio = defect_count / total_count * 100
defect_ratio = defect_ratio.sort_values(ascending=False)

print("<생산라인별 불량율(%)>")
print(defect_ratio.round(2).astype(str) + "%", "\n")

# 14. 전체 데이터를 면적이 큰 순으로 정렬하세요.
#     면적이 같다면 밝기가 낮은 순으로 정렬하세요.
#     이후 인덱스를 `0`부터 시작하도록 재설정하세요.
#     기존 인덱스는 유지하지 않습니다.
df = df.sort_values(
    ["area", "brightness"],
    ascending=[False, True]
)
df = df.reset_index(drop=True)
print(df, "\n")

# 15. 최종 데이터에 결측치와 파일명 중복이 없는지 확인하고 `data/inspection_clean.csv`로 저장하세요. 인덱스는 제외하고 저장합니다.
missing_count = df.isna().sum().sum()
print(f"결측치 개수 = {missing_count}")

duplicate_count = df.duplicated(subset=["filename"]).sum()
print(f"중복 데이터 수 = {duplicate_count}")

if missing_count > 0:
    print("결측치가 제거되지 않았습니다")
    exit(1)
if duplicate_count > 0:
    print("중복이 제거되지 않았습니다")
    exit(1)

df.to_csv(
    "./data/inspection_clean.csv",
    index=False,
    encoding="utf-8-sig"
)
print("최종 결과 저장 완료")


