"""
이미지 전처리 실습
다운로드 받은 D:/image_sample 내부의 폴더 중 다음 제시된 폴더 내의 이미지를 전처리해보세요

wrench
soccer_ball
umbrella
strawberry
scissors
yin_yang
"""

import numpy as np
import cv2

image = cv2.imread("D:/image_sample/umbrella/image_0004.jpg")
if image is None:
    print("이미지 없음")

# 오츠이진화
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
threshold, otsu = cv2.threshold(
    blur, 0, 255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((9, 9), dtype=np.uint8)    # shape 자리에는 무조건 홀수가 들어가야 한다.
result1 = cv2.erode(image, kernel)
result2 = cv2.dilate(result1, kernel)

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)


cv2.imshow("image", image)
cv2.imshow("otsu", otsu)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()