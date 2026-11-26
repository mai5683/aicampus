import cv2

image = cv2.imread("./images/coins/20261101_C_003.jpg")

if image is None:
    print("이미지를 읽을 수 없습니다.")
    exit(1)

cv2.imshow("20261101_A_001", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
