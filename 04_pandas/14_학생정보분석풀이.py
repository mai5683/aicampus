"""
## Pandas 종합 실습 — 교육생 성적 및 출결 관리

국비지원 교육기관에서 교육생의 성적 및 출결 정보를 student_records.csv 파일로 관리하고 있습니다.
전체 교육일수는 20일이며, 필기점수와 실기점수를 기준으로 교육생의 평가결과를 관리하고자 합니다.
다음 요구사항을 순서대로 해결하세요.

# 제한사항

- for, while, if를 사용하지 않습니다.
- 지금까지 배운 Pandas 기능만으로 해결합니다.
- 각 문제는 앞선 문제의 결과를 이어서 사용합니다.
- 원본 CSV 파일을 덮어쓰지 않습니다.
- 비율은 백분율(%)로 출력합니다.
- 결측치 처리 기능을 사용하지 않습니다.
"""

# 1. student_records.csv 파일을 불러오세요.    학번을 인덱스로 지정하세요.

import pandas as pd

df = pd.read_csv(
    "./data/student_records.csv",
    index_col="학번")
print(df)
print("-"*70)

# 2. S010 학생의 모든 정보를 출력하세요.
print(df.loc["S010"])
# print(type(df.loc["S010"]))  # Series
print("-"*70)

# 3. 전체 데이터의 행 개수, 열 개수, 자료형을 출력하세요.
print(f"전체 데이터의 행 개수 : {len(df)}")
print(f"전체 데이터의 행 개수 : {df.shape[0]}")
print(f"전체 데이터의 열 개수 : {df.shape[1]}")
print(f"전체 데이터의 자료형 : {df.dtypes}")
print("-"*70)

# 4. 모든 학생의 이름, 필기점수, 실기점수만 출력하세요.
# print(df["이름", "필기점수", "실기점수"])    # error
print(df[["이름", "필기점수", "실기점수"]])
print("-"*70)

# 5. 출석일수가 20일을 초과하는 학생의 정보를 출력하세요.
condition = df["출석일수"] > 20
# condition = df.loc[:, "출석일수"] > 20
print(df[condition])
print("-"*70)

# 6. 처음 5명의 정보와 마지막 5명의 정보를 출력하세요.
print("처음 5명 :")
# print(df.iloc[:5])    # iloc 사용 가능
print(df.head())
print("마지막 5명 :")
# print(df.iloc[-5:])   # iloc 사용 가능
print(df.tail())
print("-"*70)

# 7. 필기점수 또는 실기점수가 0~100 범위를 벗어난 학생의 정보를 출력하세요.
condition = ((df["필기점수"] > 100) | (df["필기점수"] < 0)) | ((df["실기점수"] > 100) | (df["실기점수"] < 0))
print(df[condition])
print("-"*70)

# 8. 세 번째 학생부터 일곱 번째 학생까지의 정보를 출력하세요.
print(df.iloc[2:7])
print("-"*70)

# 9. S010 학생의 이름과 출석일수만 출력하세요.
print(df.loc["S010", ["이름", "출석일수"]])
print("-"*70)

# 10. 출석일수가 0~20 범위를 벗어나지 않도록 제한하세요.
condition = (df["출석일수"] < 0) | (df["출석일수"] > 20)
print(f"before = {df[condition].shape[0]}명")

# df["출석일수"] = df["출석일수"].clip(lower=0, upper=20)  # .clip(0, 20) 으로 써도 무방
df["출석일수"] = df["출석일수"].clip(0, 20)

condition = (df["출석일수"] < 0) | (df["출석일수"] > 20)
print(f"after = {df[condition].shape[0]}명")
print("-"*70)

# 11. 필기점수와 실기점수가 0~100 범위를 벗어나지 않도록 제한하세요.
# df["필기점수"] = df["필기점수"].clip(lower=0, upper=100)
# df["실기점수"] = df["실기점수"].clip(lower=0, upper=100)
condition = (
    (df["필기점수"] < 0) | (df["필기점수"] > 100) |
    (df["실기점수"] < 0) | (df["실기점수"] > 100)
)
print(f"before = {df[condition].shape[0]}명")

df[["필기점수", "실기점수"]] = df[["필기점수", "실기점수"]].clip(0, 100)

condition = (
    (df["필기점수"] < 0) | (df["필기점수"] > 100) |
    (df["실기점수"] < 0) | (df["실기점수"] > 100)
)
print(f"before = {df[condition].shape[0]}명")

print("-"*70)

# 12. 실기점수가 필기점수보다 20점 이상 높은 학생의 정보를 출력하세요.
condition = df["실기점수"] - df["필기점수"] >= 20
# condition = df["실기점수"] >= df["필기점수"] + 20
print(df[condition])
print("-"*70)

# 13. 전체 교육일수가 20일일 때 '출석률'이라는 새로운 열을 생성하세요.
#     (80%라면 80이라는 숫자로 저장)
#     (ex) 10일 출석했으면 10 / 20 = 0.5 → * 100 = 50
#     즉, 출석률 = 출석일수 / 20 * 100
df["출석률"] = (df["출석일수"] / 20) * 100
df["출석률"] = df["출석률"].round().astype(int)
print("-"*70)

# 14. 필기점수 40%, 실기점수 60%를 반영하여 '최종점수'라는 새로운 열을 생성하세요.
# df["최종점수"] = 필기점수 * 40% + 실기점수 * 60%
df["최종점수"] = (df["필기점수"] * 0.4) + (df["실기점수"] * 0.6)
print("-"*70)

# 15. 최종점수의 소수점 이하를 버리고 정수형으로 변경하세요.
df["최종점수"] = df["최종점수"].astype(int)
print("-"*70)

# 16. 출석률이 100%인 학생의 비율을 출력하세요.
# 비율 = 100%인 학생 수 / 전체 학생 수 * 100
condition = df["출석률"] == 100
# count = condition.sum()
count = df[condition].shape[0]   # 추천
# count = len(df[condition])
# print((len(df[condition]) / len(df)) * 100)
print(f"100% 출석률 인원수 = {count}")
total = df.shape[0]
print(f"전체 인원수 = {total}")
ratio = count / total * 100
print("-"*70)

# 17. 최종점수가 가장 높은 학생의 모든 정보를 출력하세요.
#     (동점자가 있다면 모두 출력)
# condition = 최종점수 == 가장 높은 최종점수
condition = df["최종점수"] == df["최종점수"].max()
print(df[condition])
print("-"*70)

# 18. '평가결과'라는 열을 생성하고 모든 학생의 평가결과를 '불합격'으로 설정하세요.
df["평가결과"] = "불합격"
print(df)
print("-"*70)

# 19. 최종점수가 전체 학생의 평균 최종점수보다 높은 학생의 정보를 출력하세요.
# condition = 최종점수 > 평균 최종점수
condition = df["최종점수"] > df["최종점수"].mean()
print(df[condition])
print("-"*70)

# 20. 다음 조건을 모두 만족하는 학생의 평가결과를 '합격'으로 변경하세요.
#     - 최종점수 70점 이상
#     - 필기점수 40점 이상
#     - 실기점수 40점 이상
#     - 출석률 80% 이상
#     - 중도포기 상태가 아님
condition = (
        (df["최종점수"] >= 70) &
        (df["필기점수"] >= 40) &
        (df["실기점수"] >= 40) &
        (df["출석률"] >= 80) &
        (df["상태"] != "중도포기")
)
df.loc[condition, "평가결과"] = "합격"
print(df)
print("-"*70)

# 21. 중도포기 학생을 제외한 전체 학생 중 합격한 학생의 비율을 출력하세요.
condition = df["상태"] != "중도포기"
# pass_count = len(df[condition & (df["평가결과"] == "합격")]) / len(df[condition]) * 100
# print(pass_count)
survivor = df[condition]

condition = survivor["평가결과"] == "합격"
# count = condition.sum()
count = survivor[condition].shape[0]
total = survivor.shape[0]
ratio = count / total * 100
print(f"합격자 = {count}명, 수강생 = {total}명")
print(f"수강생 중 합격자 비율은 {ratio:.2f}% 입니다.")
print("-"*70)

# 22. 최종점수는 70점 이상이지만 평가결과가 '불합격'인 학생의 정보를 출력하세요.
condition = (df["최종점수"] >= 70) & (df["평가결과"] == "불합격")
print(df[condition])
print("-"*70)

# 23. S015 학생의 행 전체를 다음 정보로 변경하세요.
#     이름: 김철수
#     반: B
#     필기점수: 80
#     실기점수: 90
#     출석일수: 18
#     상태: 수강중
#     출석률: 90
#     최종점수: 86
#     평가결과: 합격
# → 추가 순서를 지켜서 넣을 것!
print(df.columns)
# df.loc["S015"] = "김철수", "B", 80, 90, 18, "수강중", 90, 86, "합격"
df.loc["S015"] = [
    "김철수", "B", 80, 90, 18,
    "수강중", 90, 86, "합격"
    ]                          # ------> 이렇게 줄 나눠서 입력 시 대괄호 필요
print(df.loc["S015"])
print("-"*70)

# 24. S010 학생의 필기점수와 실기점수를 각각 85점과 95점으로 동시에 변경하세요.
df.loc["S010", ["필기점수", "실기점수"]] = 85, 95
print(df.loc["S010"])
print("-"*70)

# 25. S061이라는 학번으로 새로운 학생을 추가하세요.
#     이름: 홍길동
#     반: A
#     필기점수: 90
#     실기점수: 80
#     출석일수: 20
#     상태: 수강중
#     출석률: 100
#     최종점수: 84
#     평가결과: 합격
df.loc["S061"] = "홍길동", "A", 90, 80, 20, "수강중", 100, 84, "합격"
print(df)
print("-"*70)

# 26. 변경된 데이터를 기준으로 최종점수, 출석률, 평가결과를 다시 계산하세요.
# 평가 기준과 자료형은 이전 문제와 동일하게 적용하세요.
# df["최종점수"] = 필기점수 * 40% + 실기점수 * 60%
# 출석률 = 출석일수 / 20 * 100
# df["평가결과"] = "불합격"
df["최종점수"] = (df["필기점수"] * 0.4) + (df["실기점수"] * 0.6)
df["최종점수"] = df["최종점수"].astype(int)

df["출석률"] = (df["출석일수"] / 20) * 100
df["출석률"] = df["출석률"].round.astype(int)

condition = (
        (df["최종점수"] >= 70) &
        (df["필기점수"] >= 40) &
        (df["실기점수"] >= 40) &
        (df["출석률"] >= 80) &
        (df["상태"] != "중도포기")
)                               # ---------> 줄 나눠서 입력할 땐 괄호 사용
df.loc[condition, "평가결과"] = "합격"
df.loc[~condition, "평가결과"] = "불합격"     # ~ : 아니면(not) 이라는 뜻
print(df)
print("-"*70)

# 27. 중도포기 학생을 모두 삭제하세요.
condition = df["상태"] == "중도포기"
df = df.drop(index=df.index[condition])
# df.index[condition] : 전체 학생의 학번을 가져온 후 조건이 True인 학번만 골라냄.
# df[condition].index : 중도포기 학생들의 행 전체를 가져온 후 거기에서 학번만 추출함.
#                                            ----------------> 순서는 차이 있지만 결과는 같다.
print(df)
print("-"*70)

# 28. 반별 합격자 수를 출력하세요.
condition = df["평가결과"] == "합격"
# print(df[condition].groupby("반")["평가결과"].count())
print(df[condition].groupby("반").size())
# print(condition.groupby(df["반"]).sum())
print("-"*70)

# 29. 반별 최종점수의 표준편차를 출력하세요.
# std_score = df.groupby("반")["최종점수"].std()
# print(std_score)
print(df.groupby("반")["최종점수"].std())
print("-"*70)

# 30. 반별 합격률을 출력하세요.
#     (합격자 수 / 해당 반의 전체 학생 수 * 100)
#     합격자가 없는 반은 0%로 출력하세요.
df.loc["S062"] = (
    "피카츄", "D", 30, 30, 20,
    "수강중", 100, 30, "불합격"
)                               # 풀이 중 학생 추가해서 예시연습

condition = df["평과결과"] == "합격"
# passed = df[condition].groupby("반").size()
# 선 필터링을 하고 그룹을 나누면 '없는 반'이 안 나온다.
# 논리 자체를 그룹으로 나눠서 합계를 구해야 한다.
# passed = condition.groupby("반").sum()
passed = condition.groupby(df["반"]).sum()

total = df.groupby("반").size()
print(passed)
print(total)
ratio = passed / total * 100
print(ratio)
print(ratio.round(2).astype(str) + "%")
#           → round(2) : 소수점 두자리까지
print("-"*70)

# 31. 현재 DataFrame에서 다음 열만 추출하여 result라는 새로운 DataFrame을 생성하세요.
#     - 이름
#     - 반
#     - 최종점수
#     - 출석률
#     - 평가결과
result = df[["이름", "반", "최종점수", "출석률", "평가결과"]]
# result = df[["이름", "반", "최종점수", "출석률", "평가결과"]].copy()
#                   ------> 기존 파일로 다음 작업도 할 예정이라면 .copy() 사용해서 복사본으로 만들어야 한다.
print(result)
print("-"*70)

# 32. result를 student_result.csv로 저장하세요.
#     단, 학번 정보가 유지되어야 합니다.
result.to_csv(
    "./data/student_result.csv",
    encoding="utf-8-sig",
    index_label="학번"
)
print("저장 완료")



