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

# 붉은 색?
# 이미지를 분석해 보니
# B, G < 160
# R > 160
mask = (
    (image[:, :, 0] < 160) &    # B
    (image[:, :, 1] < 160) &    # G
    (image[:, :, 2] > 160)      # R
)
# print(len(image[mask]))

# 이진화(binarize)
# - 원하는 것과 원하지 않는 것을 반대색으로 배치하는 것
detect = image.copy()
detect[mask] = [255, 255, 255]
detect[~mask] = [0, 0, 0]

# gaussian blur 후 이진화
# blur = cv2.GaussianBlur(image, (9, 9), 0)
blur = cv2.medianBlur(image, 9)

mask_blur = (
    (blur[:, :, 0] < 160) &    # B
    (blur[:, :, 1] < 160) &    # G
    (blur[:, :, 2] > 160)      # R
)
detect_blur = blur.copy()
detect_blur[mask_blur] = [255, 255, 255]
detect_blur[~mask_blur] = [0, 0, 0]

# 진짜 블러 하고 나니까 찾은 게 늘어났나요?
# print(기존 탐지 픽셀 수 < 블러 후 탐지 픽셀 수)
print(len(detect[detect == [255, 255, 255]]))
print(len(detect_blur[detect_blur == [0, 0, 0]]))

# 이미지 표시
cv2.imshow("image", image)
cv2.imshow("detect", detect)
cv2.imshow("blur", blur)
cv2.imshow("detect_blur", detect_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()



