"""
실습 문제 : 컬러 노이즈 이미지 생성
파일명 : 25_컬러노이즈.py

사용자에게 폭과 높이를 입력받아 해당하는 크기만큼의 컬러 노이즈 이미지를 만들어 출력하세요
(결과를 color_noise.jpg)로 저장하세요
"""

import numpy as np
import cv2

w = int(input("폭 : "))
h = int(input("높이 : "))
color_noise = np.random.randint(0, 256, size=(h, w, 3), dtype=np.uint8)

cv2.imshow("color_noise", color_noise)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("./images/color_noise.jpg", color_noise)

