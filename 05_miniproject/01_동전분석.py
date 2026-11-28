
import cv2
import coin_core as cc


# ------------------------------------------------
# 프로그램 실행
# ------------------------------------------------

# 이미지 불러오기
filename = "20261107_B_004.jpg"
image = cv2.imread(f"./images/coins/{filename}")
if image is None:
    print("이미지를 읽을 수 없습니다.")
    exit(1)

# 원본 이미지
cv2.imshow(filename, image)

# 이미지 분석 함수 호출
result, coin_list = cc.analyze_image(image)
coin_count = len(coin_list)

# 전체 금액 및 금액별 동전 개수 집계
total_price = 0
coin_counts = {10: 0, 50: 0, 100: 0, 500: 0}

for coin in coin_list:
    price = coin["price"]
    total_price += price
    coin_counts[price] += 1

# 동전별 특징 데이터 출력
for coin in coin_list:
    print(coin)
print("〓" * 70)

# 전체 동전 개수 및 금액 출력
print(f"검사 파일 : {filename}")
print(f"검출된 동전 개수 : {coin_count}개")
print(f"전체 동전 금액 : {total_price:,}원")

# 금액별 동전 개수 출력
for key in coin_counts:
    print(f"{key}원 : {coin_counts[key]}개")

# 최종 분석 결과 이미지 출력
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()


