"""
사과 이미지(apple.png)에서 사과를 찾아 봅시다.

기본 컨셉은 붉은 계열의 픽셀을 찾는 것
필요하다면 블러를 사용하는 것 (가우시안 블러)
"""

import numpy as np
import cv2

image = cv2.imread("./images/apple.png")
if image is None:
    print("이미지가 존재하지 않습니다")
    exit(1)

# grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# binarize
ret, binary = cv2.threshold(gray, 70, 255,
                            cv2.THRESH_BINARY)  # thresh보다 큰 걸 흰색(255)으로 만들고 나머지는 버림


# 이미지 표시
cv2.imshow("image", image)
cv2.imshow("gray", gray)
cv2.imshow("binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()