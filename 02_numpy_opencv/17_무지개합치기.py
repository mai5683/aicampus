"""
실습문제 : 무지개 합치기
17_무지개합치기.py에 병합 명령을 이용해서
각각의 색상 이미지를 합쳐서 무지개를 만들어보세요
"""

import numpy as np
import cv2

image = np.zeros((30, 500, 3), dtype=np.uint8)

# 이미지 생성
red = np.full((30, 500, 3), [49, 48, 214], dtype=np.uint8)
orange = np.full((30, 500, 3), [85, 112, 225], dtype=np.uint8)
yellow = np.full((30, 500, 3), [110, 203, 253], dtype=np.uint8)
green = np.full((30, 500, 3), [148, 184, 0], dtype=np.uint8)
blue = np.full((30, 500, 3), [255, 185, 116], dtype=np.uint8)
deepblue = np.full((30, 500, 3), [227, 132, 9], dtype=np.uint8)
purple = np.full((30, 500, 3), [231, 92, 108], dtype=np.uint8)

# vstack() 또는 concatenate(axis=)를 써서 수직 방향으로 병합
rainbow = np.vstack((red, orange, yellow, green, blue, deepblue, purple))
# rainbow = np.concatenate(
#     (red, orange, yellow, green, blue, deepblue, purple),
#     axis=0
# )

# 이미지 표시
cv2.imshow("rainbow", rainbow)
cv2.waitKey(0)
cv2.destroyAllWindows()




