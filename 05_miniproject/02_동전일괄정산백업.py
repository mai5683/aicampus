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

# 분석 결과 저장 폴더 생성
result_folder = Path("./images/results")
result_folder.mkdir(exist_ok=True)

# 전체 동전 정보 리스트 초기화
all_coins = []

# 이미지 일괄 분석
for file in file_list:
    image = cv2.imread(str(file))

    if image is None:
        print("이미지를 읽을 수 없습니다.")
        continue

    # 이미지 분석 함수 호출
    result, coin_list = cc.analyze_image(image)

    # 검출된 동전 개수 계산
    coin_count = len(coin_list)

    # 파일명 및 동전 개수 출력
    print(f"{file.name} : {coin_count}개")

    # 파일명에서 정산 정보 추출
    parts = file.stem.split("_")
    date = parts[0]
    machine = parts[1]
    print(f"날짜: {date}, 정산기: {machine}")

    # 동전별 정산 정보 추가
    for coin in coin_list:
        coin["filename"] = file.name
        coin["date"] = date
        coin["machine"] = machine

        all_coins.append(coin)

    save_path = result_folder / file.name
    cv2.imwrite(str(save_path), result)

# 동전 상세 데이터 생성 및 csv 저장
df = pd.DataFrame(all_coins)

df = df[["filename", "date", "machine", "coin_id",
         "center_x", "center_y", "width", "height",
         "area", "perimeter", "brightness",
         "brightness_std", "price"]]

df.to_csv("coins.csv", index=False, encoding="utf-8-sig")

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

# 1. 전체 동전의 개수를 구하시오.
total_count = len(df)
print(f"전체 동전 개수: {total_count}개", "\n")

# 2. 전체 정산 금액을 구하시오.
total_price = df["price"].sum()
print(f"전체 정산 금액: {total_price:,}원", "\n")

# 3. 동전 종류별 개수를 구하시오.
coin_counts = df.groupby("price")["coin_id"].count()
print(f"동전 종류별 개수: \n{coin_counts}", "\n")

# 4. 동전 종류별 합계 금액을 구하시오.
coin_prices = df.groupby("price")["price"].sum()
print(f"동전 종류별 합계 금액: \n{coin_prices}", "\n")

# 5. 날짜별 동전 개수와 합계 금액을 구하시오.
date_counts = df.groupby("date")["coin_id"].count()
date_prices = df.groupby("date")["price"].sum()
print(f"날짜별 동전 개수: \n{date_counts}")
print(f"날짜별 동전 합계 금액: \n{date_prices}", "\n")

# 6. 정산기별 동전 개수와 합계 금액을 구하시오.
machine_counts = df.groupby("machine")["coin_id"].count()
machine_prices = df.groupby("machine")["price"].sum()
print(f"정산기별 동전 개수: \n{machine_counts}")
print(f"정산기별 동전 합계 금액: \n{machine_prices}", "\n")

# 7. 날짜와 정산기를 함께 그룹화하여 동전 개수와 합계 금액을 구하시오.
date_machine_counts = df.groupby(["date", "machine"])["coin_id"].count()
date_machine_prices = df.groupby(["date", "machine"])["price"].sum()
print(f"날짜 및 정산기별 동전 개수: \n{date_machine_counts}")
print(f"날짜 및 정산기별 동전 합계 금액: \n{date_machine_prices}", "\n")

# 8. 정산 금액이 가장 높은 날짜를 구하시오.
condition = date_prices == date_prices.max()
max_date = date_prices[condition]
print(f"정산 금액이 가장 높은 날짜: \n{max_date}", "\n")

# 9. 정산 금액이 가장 높은 정산기를 구하시오.
condition = machine_prices == machine_prices.max()
max_machine = machine_prices[condition]
print(f"정산 금액이 가장 높은 정산기: \n{max_machine}", "\n")

# 10. 가장 많이 투입된 동전의 종류를 구하시오.
condition = coin_counts == coin_counts.max()
max_coin = coin_counts[condition]
print(f"가장 많이 투입된 동전의 종류 : \n{max_coin}", "\n")

# 11. 동전 종류별 평균 면적을 구하시오.
coin_area_mean = df.groupby("price")["area"].mean()
print(f"동전 종류별 평균 면적: \n{coin_area_mean.round(2)}", "\n")

# 12. 동전 종류별 면적의 표준편차를 구하시오.
coin_area_std = df.groupby("price")["area"].std()
print(f"동전 종류별 면적의 표준편차: \n{coin_area_std.round(2)}", "\n")

# 13. 정산기별 금액이 전체 정산 금액에서 차지하는 비율을 구하시오.
machine_ratio = machine_prices / total_price * 100
print(f"정산기별 금액 비율(%): \n{machine_ratio.round(2)}", "\n")

# 14. 이미지별 정산 금액을 구하고 내림차순으로 정렬하시오.
image_prices = df.groupby("filename")["price"].sum()
image_prices = image_prices.sort_values(ascending=False)
print("<이미지별 정산 금액 내림차순>")
print(image_prices, "\n")

# 15. 금액이 100원 이상인 동전의 정보를 추출하시오.
condition = df["price"] >= 100
coins_100up = df[condition]
print(coins_100up)



# ------------------------------------------------
# 엑셀 보고서 생성
# ------------------------------------------------

# 전체현황 데이터 생성
summary = pd.DataFrame({
    "전체 동전 개수": [total_count],
    "전체 정산 금액": [total_price]
})

# 종류별현황 데이터 생성
coin_summary = pd.DataFrame({
    "동전 개수": coin_counts,
    "합계 금액": coin_prices
})

# 날짜별현황 데이터 생성
date_summary = pd.DataFrame({
    "동전 개수": date_counts,
    "합계 금액": date_prices
})

# 정산기별현황 데이터 생성
machine_summary = pd.DataFrame({
    "동전 개수": machine_counts,
    "합계 금액": machine_prices,
    "금액 비율(%)": machine_ratio.round(2)
})

# 날짜정산기별현황 데이터 생성
date_machine_summary = pd.DataFrame({
    "동전 개수": date_machine_counts,
    "합계 금액": date_machine_prices
})

# 동전특징 데이터 생성
coin_features = pd.DataFrame({
    "평균 면적": coin_area_mean.round(2),
    "면적 표준편차": coin_area_std.round(2)
})

# 이미지별현황 데이터 생성
image_summary = pd.DataFrame({
    "합계 금액": image_prices
})

# 엑셀 파일 저장
with pd.ExcelWriter(
        "report.xlsx",
        mode="w",
        engine="openpyxl") as writer:
    summary.to_excel(writer, sheet_name="전체현황", index=False)
    coin_summary.to_excel(writer, sheet_name="종류별현황", index=True)
    date_summary.to_excel(writer, sheet_name="날짜별현황", index=True)
    machine_summary.to_excel(writer, sheet_name="정산기별현황", index=True)
    date_machine_summary.to_excel(writer, sheet_name="날짜정산기별현황", index=True)
    coin_features.to_excel(writer, sheet_name="동전특징", index=True)
    image_summary.to_excel(writer, sheet_name="이미지별현황", index=True)
    coins_100up.to_excel(writer, sheet_name="고액동전", index=False)

print("엑셀 보고서 저장 완료")


