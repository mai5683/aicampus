import cv2
import numpy as np
from pathlib import Path
import pandas as pd


# ------------------------------------------------
# 이미지 분석 함수
# ------------------------------------------------
def analyze_image(image):
    # 이미지 전처리
    # - 그레이스케일
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # - 블러
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # - OTSU 이진화
    threshold, otsu = cv2.threshold(
        blur, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # - 모폴로지
    kernel = np.ones((5, 5), dtype=np.uint8)
    morph = cv2.morphologyEx(otsu, cv2.MORPH_CLOSE, kernel)

    # 윤곽선 검출
    contours, hierarchy = cv2.findContours(
        morph, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # 사본 생성
    result = image.copy()

    # 글자 설정
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    thickness = 2

    # 동전 집계 및 분석 데이터 초기화
    coin_count = 0
    total_price = 0
    coin_list = []

    # 동전별 특징 추출 및 금액 판별
    for contour in contours:

        # 면적 계산 및 작은 노이즈 제외
        area = cv2.contourArea(contour)
        if area < 1000:
            continue
        coin_count += 1

        # 동전 둘레 및 크기 계산
        perimeter = cv2.arcLength(contour, True)
        x, y, w, h = cv2.boundingRect(contour)

        # 동전의 중심 좌표 계산
        m = cv2.moments(contour)
        if m["m00"] != 0:
            cx = int(m["m10"] / m["m00"])
            cy = int(m["m01"] / m["m00"])
        else:
            cx = x + w // 2
            cy = y + h // 2

        # 동전 영역 추출
        mask = np.zeros(gray.shape, dtype=np.uint8)
        cv2.drawContours(mask, [contour], -1, 255, -1)
        condition = mask == 255
        coin_pixels = gray[condition]

        # 동전 영역의 평균 밝기 및 표준편차 계산
        brightness = np.mean(coin_pixels)
        brightness_std = np.std(coin_pixels)

        # 동전 금액 및 사각형 색상 판별
        if area < 9500:
            price = 10
            color = (0, 0, 255)
        elif area < 13000:
            price = 50
            color = (255, 0, 0)
        elif area < 16500:
            price = 100
            color = (0, 255, 0)
        else:
            price = 500
            color = (0, 255, 255)

        # 동전 검출 영역 표시
        cv2.rectangle(result, (x, y), (x + w, y + h), color, 2)

        # 동전별 금액 표시
        text = f"{price}"

        (tw, th), baseline = cv2.getTextSize(
            text, font, font_scale, thickness
        )
        tx = x + (w // 2) - (tw // 2)
        ty = y - 10
        cv2.putText(result, text, (tx, ty),
                    font, font_scale, (0, 0, 0), thickness)

        # 전체 금액 누적
        total_price += price

        # 동전별 특징 데이터
        coin_info = {
            "coin_id": coin_count,
            "center_x": cx, "center_y": cy,
            "width": w, "height": h,
            "area": round(area, 2),
            "perimeter": round(perimeter, 2),
            "brightness": round(float(brightness), 2),
            "brightness_std": round(float(brightness_std), 2),
            "price": price
        }
        # 전체 동전 리스트에 추가
        coin_list.append(coin_info)

    # 전체 동전 개수 및 금액 표시
    cv2.putText(result, f"{coin_count}", (10, 30),
                font, font_scale, (0, 0, 0), thickness)
    cv2.putText(result, f"{total_price:,} KRW", (10, 50),
                font, font_scale, (0, 0, 0), thickness)

    return result, coin_list


# ------------------------------------------------
# 이미지 파일 목록 조회 함수
# ------------------------------------------------
def load_files(folder):
    # 이미지 파일 리스트 초기화
    file_list = []

    # JPG 파일 선별
    for item in folder.iterdir():
        if item.is_file() and item.suffix.lower() == ".jpg":
            file_list.append(item)

    # 파일명 오름차순 정렬
    file_list.sort()

    return file_list


# ------------------------------------------------
# 이미지 일괄 분석 함수
# ------------------------------------------------
def analyze_all_images(file_list, result_folder):
    # 분석 결과 저장 폴더 생성
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
        result, coin_list = analyze_image(image)

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

        # 분석 결과 이미지 저장
        save_path = result_folder / file.name
        cv2.imwrite(str(save_path), result)

    return all_coins


# ------------------------------------------------
# 동전 상세 데이터 생성 및 CSV 저장 함수
# ------------------------------------------------
def save_csv(all_coins, csv_path):
    df = pd.DataFrame(all_coins)

    df = df[["filename", "date", "machine", "coin_id",
             "center_x", "center_y", "width", "height",
             "area", "perimeter", "brightness",
             "brightness_std", "price"]]

    df.to_csv(csv_path, index=False, encoding="utf-8-sig")

    return df


# ------------------------------------------------
# Pandas 정산 통계 분석 함수
# ------------------------------------------------
def analyze_statistics(df):
    # 1. 전체 동전 개수
    total_count = len(df)

    # 2. 전체 정산 금액
    total_price = df["price"].sum()

    # 3. 동전 종류별 개수
    coin_counts = df.groupby("price")["coin_id"].count()

    # 4. 동전 종류별 합계 금액
    coin_prices = df.groupby("price")["price"].sum()

    # 5. 날짜별 동전 개수와 합계 금액
    date_counts = df.groupby("date")["coin_id"].count()
    date_prices = df.groupby("date")["price"].sum()

    # 6. 정산기별 동전 개수와 합계 금액
    machine_counts = df.groupby("machine")["coin_id"].count()
    machine_prices = df.groupby("machine")["price"].sum()

    # 7. 날짜 및 정산기별 동전 개수와 합계 금액
    date_machine_counts = df.groupby(["date", "machine"])["coin_id"].count()
    date_machine_prices = df.groupby(["date", "machine"])["price"].sum()

    # 8. 정산 금액이 가장 높은 날짜
    condition = date_prices == date_prices.max()
    max_date = date_prices[condition]

    # 9. 정산 금액이 가장 높은 정산기
    condition = machine_prices == machine_prices.max()
    max_machine = machine_prices[condition]

    # 10. 가장 많이 투입된 동전의 종류
    condition = coin_counts == coin_counts.max()
    max_coin = coin_counts[condition]

    # 11. 동전 종류별 평균 면적
    coin_area_mean = df.groupby("price")["area"].mean()

    # 12. 동전 종류별 면적의 표준편차
    coin_area_std = df.groupby("price")["area"].std()

    # 13. 정산기별 금액 비율
    machine_ratio = machine_prices / total_price * 100

    # 14. 이미지별 정산 금액 내림차순 정렬
    image_prices = df.groupby("filename")["price"].sum()
    image_prices = image_prices.sort_values(ascending=False)

    # 15. 금액이 100원 이상인 동전 정보 추출
    condition = df["price"] >= 100
    coins_100up = df[condition]

    # 통계 분석 결과를 딕셔너리로 정리
    statistics = {
        "total_count": total_count,
        "total_price": total_price,
        "coin_counts": coin_counts,
        "coin_prices": coin_prices,
        "date_counts": date_counts,
        "date_prices": date_prices,
        "machine_counts": machine_counts,
        "machine_prices": machine_prices,
        "date_machine_counts": date_machine_counts,
        "date_machine_prices": date_machine_prices,
        "max_date": max_date,
        "max_machine": max_machine,
        "max_coin": max_coin,
        "coin_area_mean": coin_area_mean,
        "coin_area_std": coin_area_std,
        "machine_ratio": machine_ratio,
        "image_prices": image_prices,
        "coins_100up": coins_100up
    }
    return statistics


# ------------------------------------------------
# 엑셀 보고서 저장 함수
# ------------------------------------------------
def save_report(statistics, excel_path):
    # 전체현황 데이터 생성
    summary = pd.DataFrame({
        "전체 동전 개수": [statistics["total_count"]],
        "전체 정산 금액": [statistics["total_price"]]
    })

    # 종류별현황 데이터 생성
    coin_summary = pd.DataFrame({
        "동전 개수": statistics["coin_counts"],
        "합계 금액": statistics["coin_prices"]
    })

    # 날짜별현황 데이터 생성
    date_summary = pd.DataFrame({
        "동전 개수": statistics["date_counts"],
        "합계 금액": statistics["date_prices"]
    })

    # 정산기별현황 데이터 생성
    machine_summary = pd.DataFrame({
        "동전 개수": statistics["machine_counts"],
        "합계 금액": statistics["machine_prices"],
        "금액 비율(%)": statistics["machine_ratio"].round(2)
    })

    # 날짜정산기별현황 데이터 생성
    date_machine_summary = pd.DataFrame({
        "동전 개수": statistics["date_machine_counts"],
        "합계 금액": statistics["date_machine_prices"]
    })

    # 동전특징 데이터 생성
    coin_features = pd.DataFrame({
        "평균 면적": statistics["coin_area_mean"].round(2),
        "면적 표준편차": statistics["coin_area_std"].round(2)
    })

    # 이미지별현황 데이터 생성
    image_summary = pd.DataFrame({
        "합계 금액": statistics["image_prices"]
    })

    # 고액동전 데이터
    coins_100up = statistics["coins_100up"]

    # 엑셀 파일 저장
    with pd.ExcelWriter(
            excel_path,
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