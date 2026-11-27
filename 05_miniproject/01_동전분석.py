import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread("./images/coins/20261101_C_002.jpg")
if image is None:
    print("이미지를 읽을 수 없습니다.")
    exit(1)

# 원본 이미지
cv2.imshow("20261101_C_002.jpg", image)
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
kernel = np.ones((5,5), dtype=np.uint8)
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

# 동전 개수 및 전체 금액 초기화
coin_count = 0
total_price = 0
coin_counts = {10: 0, 50: 0, 100: 0, 500: 0}

# 동전별 특징 추출 및 금액 판별
for contour in contours:

    # 면적 계산 및 작은 노이즈 제외
    area = cv2.contourArea(contour)
    if area < 1000:
        continue
    coin_count += 1

    perimeter = cv2.arcLength(contour, True)
    x, y, w, h = cv2.boundingRect(contour)
    m = cv2.moments(contour)
    if m["m00"] != 0:
        cx = int(m["m10"] / m["m00"])
        cy = int(m["m01"] / m["m00"])
    else:
        cx = x + w // 2
        cy = y + h // 2

    mask = np.zeros(gray.shape, dtype=np.uint8)
    cv2.drawContours(mask, [contour], -1, 255, -1)
    condition = mask == 255
    coin_pixels = gray[condition]
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

    # 사각형 그리기
    cv2.rectangle(result, (x, y), (x + w, y + h), color, 2)

    # 금액 표시
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
    coin_counts[price] += 1

    # 동전 특징 출력
    print(f"동전번호 : {coin_count}")
    print("중심좌표 :", cx, cy)
    print(f"면적 : {area:.2f}")
    print(f"둘레 : {perimeter:.2f}")
    print(f"평균 밝기 : {brightness:.2f}")
    print(f"밝기의 표준편차 : {brightness_std:.2f}")
    print("-" * 30)

# 전체 동전 개수 및 금액 표시
cv2.putText(result, f"{coin_count}", (10, 30),
            font, font_scale, (0, 0, 0), thickness)
cv2.putText(result, f"{total_price:,} KRW", (10, 50),
            font, font_scale, (0, 0, 0), thickness)

# 전체 동전 개수 및 금액 출력
print(f"검출된 동전 개수 : {coin_count}개")
print(f"전체 동전 금액 : {total_price:,}원")

for key in coin_counts:
    print(f"{key}원 : {coin_count}개")

# 변환 이미지 출력
cv2.imshow("gray", gray)
cv2.imshow("blur", blur)
cv2.imshow("otsu", otsu)
cv2.imshow("morph", morph)
cv2.imshow("contours", result)


cv2.waitKey(0)
cv2.destroyAllWindows()

