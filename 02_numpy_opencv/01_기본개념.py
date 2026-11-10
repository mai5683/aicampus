"""
NumPy와 OpenCV는 파이썬이 제공하지 않기 때문에 설치 필요

python에는 pip라는 패키지 설치 도구가 있으므로 이를 사용

pip install numpy
pip install opencv-python

한 번에 하면

pip install numpy opencv-python

"""

import numpy as np
import cv2

print("numpy 버전", np.__version__)
print("opencv 버전", cv2.__version__)

# 최초의 코드
# numpy를 이용해서 이미지를 생성
image = np.zeros((300, 200), dtype=np.uint8)

# 흰 사각형 그리기
image[50:150, 50:150] = 255

# opencv를 이용해서 이미지를 출력
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
