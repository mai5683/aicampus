"""
샤프닝 (Sharpening)

블러(Blur)와 반대되는 작업
- blur : 현재 픽셀의 값을 무디게 하는 작업 (주변과 유사해지게)
- sharpening : 현재 픽셀의 값을 강조하는 작업 (주변과 차이나게)

블러에도 커널(kernel)이 필요했던 것처럼
샤프닝에도 커널(kernel)이 필요하다.

하지만 형태가 조금 다르다.
"""

import cv2
import numpy as np

image = cv2.imread("../03_tkinter/images/tilted.png")
if image is None:
    print("이미지 없음")
    exit(1)

image = cv2.resize(image, (800, 600))

# blur
blur = cv2.GaussianBlur(image, (5, 5), 0)

# sharpening
# (1) 십자 커널 (3x3)   - 보통 십자 커널을 사용
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.float32)
# (2) 전체 커널 (3x3)   - 비추천
# kernel = np.array([
#     [-1, -1, -1],
#     [-1, 9, -1],
#     [-1, -1, -1]
# ], dtype=np.float32)
sharp = cv2.filter2D(image, -1, kernel)  # -1은 원본과 같은 깊이를 유지하라는 의미
# sharp = cv2.filter2D(image, cv2.CV_8U, kernel)  # = np.uint8
# sharp = cv2.filter2D(image, cv.CV_16S, kernel)  # = np.uint16
# sharp = cv2.filter2D(image, cv.CV_32F, kernel)  # = np.float32
# sharp = cv2.filter2D(image, cv.CV_64F, kernel)  # = np.float64

# 이미지 표시
cv2.imshow("image", image)
cv2.imshow("blur", blur)
cv2.imshow("sharp", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()


