
import cv2
import numpy as np
import pandas as pd
from pathlib import Path
import coin_core as cc


# Pandas 출력 설정
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.float_format", "{:,.2f}".format)

# 이미지 폴더 경로 지정
folder = Path("./images/coins")
file_list = cc.load_files(folder)

# 분석 결과 저장 폴더 경로 지정
result_folder = Path("./images/results")

# 이미지 일괄 분석 함수 호출
all_coins = cc.analyze_all_images(file_list, result_folder)

# 동전 상세 데이터 생성 및 CSV 저장
df = cc.save_csv(all_coins, "coins.csv")

print("〓" * 70)

# 데이터 검사
df = pd.read_csv("coins.csv", encoding="utf-8-sig")

print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isna().sum())

# 중복 데이터 검사
condition = df.duplicated(subset=["filename", "coin_id"])
print(f"중복 데이터 개수: {condition.sum()}개")
print(df[condition])

# 동전 금액 정상 여부 검사
condition = (
        (df["price"] != 10) & (df["price"] != 50) &
        (df["price"] != 100) & (df["price"] != 500)
)
print(f"비정상 동전 금액 개수: {condition.sum()}개")
print(df[condition])

# 정산기 번호 정상 여부 검사
condition = (df["machine"] != "A") & (df["machine"] != "B") & (df["machine"] != "C")
print(f"비정상 정산기 번호 개수: {condition.sum()}개")
print(df[condition])

# 크기, 면적, 둘레 정상 여부 검사
condition = (
        (df["width"] <= 0) | (df["height"] <= 0) |
        (df["area"] <= 0) | (df["perimeter"] <= 0)
)
print(f"비정상 크기 및 면적, 둘레 데이터 개수: {condition.sum()}개")
print(df[condition])

# 평균 밝기 범위 검사
condition = (df["brightness"] < 0) | (df["brightness"] > 255)
print(f"비정상 평균 밝기 데이터 개수: {condition.sum()}개")
print(df[condition])

# 밝기 표준편차 정상 여부 검사
condition = df["brightness_std"] < 0
print(f"비정상 밝기 표준편차 데이터 개수: {condition.sum()}개")
print(df[condition])

# 전체 이미지 및 동전 개수 출력
print(f"전체 이미지 개수 : {len(file_list)}개")
print(f"검출한 전체 동전 개수 : {len(all_coins)}개")

print("〓" * 70)


# ------------------------------------------------
# Pandas 정산 통계 분석
# ------------------------------------------------
statistics = cc.analyze_statistics(df)

# 전체 동전 개수 및 정산 금액 출력
print(f"전체 동전 개수: {statistics['total_count']}개")
print(f"전체 정산 금액: {statistics['total_price']:,}원")

# ------------------------------------------------
# 엑셀 보고서 생성
# ------------------------------------------------
cc.save_report(statistics, "report.xlsx")


