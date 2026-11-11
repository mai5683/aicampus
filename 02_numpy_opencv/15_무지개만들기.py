"""
실습문제 : 무지개 만들기
15_무지개만들기.py에 500x210 크기의 이미지를 만들고 무지개를 그려보세요
"""

import numpy as np
import cv2

image = np.zeros((210, 500, 3), dtype=np.uint8)

# image[줄, 칸무관]
image[:30,:,2] = 255                # 칸은 무관하니 :으로
image[30:60,:] = [0, 94, 255]
image[60:90,:] = [0, 228, 255]
image[90:120,:] = [22, 219, 29]
image[120:150,:,0] = 255
image[150:180,:,0] = 117
image[180:,:] = [153, 0, 63]

cv2.imshow("rainbow", image)
cv2.waitKey(0)
cv2.destroyAllWindows()