"""numpy + opencv 실습문제
파일명 : 08_이미지밝기조정.py
다음 요구사항에 맞게 프로그램을 구현하세요

- 밝기가 120인 300x300 크기의 이미지 배열을 image라는 이름으로 생성하세요
- 밝기를 50만큼 증가시킨 데이터를 bright라는 이름으로 저장하세요
- 밝기를 50만큼 감소시킨 데이터를 dark라는 이름으로 저장하세요

세 개의 이미지를 각각 opencv로 출력하여 비교하세요
"""


import numpy as np
import cv2

# 밝기가 120인 300x300 크기의 이미지 배열을 image라는 이름으로 생성하세요
image = np.full((300,300), 120, dtype=int)

bright = np.clip(image + 50, 0, 255).astype(dtype=np.uint8)
dark = np.clip(image - 50, 0, 255).astype(dtype=np.uint8)

# 이미지를 uint8로 변경 (안 배운 명령)
image = np.clip(image, 0, 255).astype(dtype=np.uint8)

# 이미지 출력
cv2.imshow("original", image)
cv2.imshow("bright", bright)
cv2.imshow("dark", dark)
cv2.waitKey(0)
cv2.destroyAllWindows()

