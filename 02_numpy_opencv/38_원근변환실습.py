"""
다음 이미지를 원근변환 기법을 사용해서 정면에서 바라보는 형태가 되도록 변환하세요.
"""

import numpy as np
import cv2

image = cv2.imread("./images/tilted2.png")
if image is None:
    print("이미지 없음")
    exit(1)

before = np.array([
    [140, 222],
    [1117, 128],
    [1383, 778],
    [220, 942]
], dtype=np.float32)

# numpy니까 h 먼저
# width = 1000
# height = 700
h, w = image.shape[:2]

# opencv니까 w 먼저
after = np.array([
    [0, 0],
    [width-1, 0],
    [width-1, height-1],
    [0, height-1],
], dtype=np.float32)

# 변환 정보 획득
# - 일반적으로 before 대신 scr(source), after 대신 dst(destination)을 사용한다.
matrix = cv2.getPerspectiveTransform(before, after)
result = cv2.warpPerspective(image, matrix, (width, height))

# 이미지 출력
cv2.imshow("image", image)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
