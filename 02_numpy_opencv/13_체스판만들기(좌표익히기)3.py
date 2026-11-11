"""
체스판 만들기

체스판 규격 : 8줄 8칸

크기를 400x400으로 설정하고 한 칸을 50px로 한 뒤 구현
"""


import numpy as np
import cv2

image = np.zeros((400, 400), dtype=np.uint8)

# 체스판 그리기
# range(시작, 종료, 간격)
# range(0, 300, 50) -> 0, 50, 100, 150, 200, 250, 300

for y in range(0, 301, 100):    # y: 0, 100, 200, 300
    for x in range(0, 301, 100):    # x: 0, 100, 200, 300
        image[y:y+50, x:x+50] = 255
        image[y+50:y+100, x+50:x+100] = 255    # 오른쪽 아래칸

# 이미지 표시
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


