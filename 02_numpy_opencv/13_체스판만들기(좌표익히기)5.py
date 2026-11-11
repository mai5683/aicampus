"""
체스판 만들기

체스판 규격 : 8줄 8칸

크기를 400x400으로 설정하고 한 칸을 50px로 한 뒤 구현
"""

import numpy as np
import cv2

# 새로운 시도 : 8줄 8칸으로 만들고 확장(repeat)
image = np.zeros((8, 8), dtype=np.uint8)

# image[짝수줄, 짝수칸] = 255
# image[시작무관:종료무관:2줄씩, 시작무관:종료무관:2칸씩] = 255
image[::2, ::2] = 255
# image[홀수줄, 홀수칸] = 255
# image[시작1:종료무관:2줄씩, 시작1:종료무관:2칸씩] = 255
image[1::2, 1::2] = 255

# (+추가) 배열의 크기를 현재 패턴에서 확장 (x50배)
# repeat(배율, 축방향)
# 축방향을 지정하지 않으면 1차원으로 간주되므로 반드시 축방향을 지정해야 한다.
# image = image.repeat(배율, 축방향)
# image = image.repeat(50, axis=0)
# image = image.repeat(50, axis=1)
image = image.repeat(50, axis=0).repeat(50, axis=1)

# 이미지 표시
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

