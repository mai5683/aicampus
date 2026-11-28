

import pandas as pd
from pathlib import Path

# 경로 계산
folder = Path(__file__).resolve().parent / "data"

# 엑셀 파일 읽기
df = pd.read_excel(
    folder / "inspection.xlsx",
    sheet_name="검사기록",
    engine="openpyxl"
)

print("<불러온 데이터>")
print(df, "\n")

# 정상 제품만 선별해서 data/inspection_good.xlsx에 저장
condition = df["검사결과"] == "정상"
df_good = df[condition]
df_defect = df[~condition]

df_good.to_excel(
    folder / "inspection_good.xlsx",
    index=False,
    engine="openpyxl"
)

# 기존 파일에 합치기
# - 덮어쓰기가 되며 합치고 싶으면 별도의 ExcelWriter를 모드 "a"로 생성해야 합니다
df_good.to_excel(
    folder / "inspection.xlsx",
    index=False,
    sheet_name="정상제품",
    engine="openpyxl"
)

print("저장 완료")


# (추가) ExcelWriter를 사용하여 기존파일에 추가하기
with pd.ExcelWriter(
                folder / "inspection.xlsx",
                mode="a",
                engine="openpyxl",
                if_sheet_exists="replace") as writer:
    df.to_excel(writer, sheet_name="분석결과", index=False)


