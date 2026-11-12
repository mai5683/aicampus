"""
실습 문제 : 컬러 노이즈 이미지 생성
파일명 : 25_컬러노이즈.py

사용자에게 폭과 높이를 입력받아 해당하는 크기만큼의 컬러 노이즈 이미지를 만들어 출력하세요
(결과를 color_noise.jpg)로 저장하세요
"""

import numpy as np
import cv2

width = 500
height = 400

# 노이즈 이미지를 생성
# noise = np.random.randint(0, 256, size=(height, width), dtype=np.uint8)
rng = np.random.default_rng()
# noise = rng.integers(0, 256, size=(height, width), dtype=np.uint8)
noise = rng.integers(0, 255,
                     size=(height, width, 3), dtype=np.uint8, endpoint=True)

# 이미지 표시
cv2.imshow("noise", noise)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 저장
cv2.imwrite("./images/color_noise1.jpg", noise)

