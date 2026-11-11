"""
컬러 이미지

컬러 이미지는 흑백이미지와 다르게 한 픽셀에 값이 3개가 들어간다.

- 흑백 이미지 300x300 → (300, 300)
- 컬러 이미지 300x300 → (300, 300, 3)
"""

import numpy as np
import cv2

# 이미지 배열 생성
# image = np.zeros((300, 300), dtype=np.uint8)    # 흑백
image = np.zeros((300, 300, 3), dtype=np.uint8) # 컬러

# 색상 변경
# image[:,:] = 200    # 흑백
# image[:,:] = [255, 0, 0]    # Blue=255
# image[:,:] = [0, 255, 0]    # Green=255
# image[:,:] = [0, 0, 255]    # Red=255
# image[:,:] = [160, 102, 55]   # 적당히 혼합된 색상

# image[:, :, 0] = 255    # Blue채널만 변경
# image[:, :, 1] = 255    # Green채널만 변경
# image[:, :, 2] = 255    # Red채널만 변경

# 이미지 표시
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()