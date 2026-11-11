"""
흑백에서 컬러로

총천연색 컬러가 아니라 컬러와 동일안 채널을 갖게 하는 것
(ex : 컬러프린트로 뽑는 검정색)
"""

import numpy as np
import cv2

# 흑백 김을 준비
# gray = np.zeros((200,300), dtype=np.uint8)
gray = np.full((200,300), 120, dtype=np.uint8)

# 컬러로 변환 :
# - 채널을 맞추겠다는 뜻
# - 밝기가 100이었다면 BGR은 얼마일까요? [100,100,100]
# - 원래 없던 채널을 생성해야 한다. (축 확장이라고 봐도 될까요?)
# - (20,,300) → (200,300,3)
color = np.stack((gray, gray, gray), axis=2)

# gray += 50      # color와 gray는 다른 개체

# 이미지 표시
cv2.imshow("gray", gray)
cv2.imshow("color", color)
cv2.waitKey(0)
cv2.destroyAllWindows()



