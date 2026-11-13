"""
모폴로지(Morphology) 연산

- 이미지를 전처리 과정에서 이진화까지 하고 나면 잡음이나 끊어짐이 생긴다.
- 잡음(noise)은 없애고, 끊어진 건 연결해 줘야 한다.
- 기본적으로 흰색을 물체로 생각하고, 검정색을 배경이라고 생각한다.
"""

import numpy as np
import cv2

# 이미지를 읽지 말고 생성
image = np.zeros((500, 500), dtype=np.uint8)

# 테스트를 위한 그림 그리기
# opencv의 그림 그리기 명령을 이용해서 도형을 그려 보자.

# 사각형 그리기
# cv2.rectangle(이미지, 시작점, 끝점, 색상, 두께)
# 두께가 -1이면 내부가 채워진다.
cv2.rectangle(image, (100,100), (150,250), 255, -1)
cv2.rectangle(image, (155,100), (205,250), 255, -1)


# 작은 노이즈를 없애기 위해서는 침식 → 팽창이 필요
# 직접 하지 않고 이를 수행하는 명령을 사용
kernel = np.ones((9,9), dtype=np.uint8)
# cv2.morphologyEx(이미지, 작업종류, 커널)
# cv2.MORPH_OPEN : 선 침식 후 팽창
# cv2.MORPH_CLOSE : 선 팽창 후 침식
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# 이미지 표시
cv2.imshow("image", image)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()