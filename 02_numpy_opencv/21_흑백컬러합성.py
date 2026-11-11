"""
실습문제 : 흑백과 컬러 이미지 합치기
파일명 : 21_흑백컬러합성.py

이미지를 읽는 명령에 옵션을 주면 흑백 이미지를 읽을 수 있습니다.
image = cv2.imread("파일명", cv2.IMREAD_GRAYSCALE)

기존에 합성했던 이미지 두개를 하나는 컬러, 하나는 흑백으로 읽은 뒤 합성해보세요.
"""

import numpy as np
import cv2

image1 = cv2.imread("./images/plus1.jpg")   # 컬러
# image1 = cv2.imread("./images/plus1.jpg", cv2.IMREAD_COLOR_BGR)    # BGR 방식
# image1 = cv2.imread("./images/plus1.jpg", cv2.IMREAD_UNCHANGED)    # 이미지 세팅
image2 = cv2.imread("./images/plus2.jpg", cv2.IMREAD_GRAYSCALE)      # grayscale

# 이미지 합성
h1, w1 = (image1.shape[0], image1.shape[1])     # image1.shape[:2] 로 간추릴 수 있다.
h2, w2 = (image2.shape[0], image2.shape[1])
ratio1 = w1 / h1
ratio2 = w2 / h2

new_h1 = 400
new_w1 = round(new_h1 * ratio1)
new_h2 = 400
new_w2 = round(new_h2 * ratio2)

resize1 = cv2.resize(image1, (new_w1, new_h1))
resize2 = cv2.resize(image2, (new_w2, new_h2))

# resize2는 흑백이니까 컬러채널로 확장
resize2_color = np.stack((resize2, resize2, resize2), axis=2)

merge = np.hstack((resize1, resize2_color))

# cv2.imshow("image1", image1)
# cv2.imshow("image2", image2)
cv2.imshow("merge", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()