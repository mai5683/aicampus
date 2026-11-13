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
cv2.rectangle(image, (100,100), (300,300), 255, -1)

# 원 그리기
# cv2.circle(이미지, 중심점, 반지름, 색상, 두께)
cv2.circle(image, (50,50), 10, 255, -1)
cv2.circle(image, (450,250), 30, 255, 1)
cv2.circle(image, (200,430), 20, 255, -1)

# 침식(erode) 연산을 수행
# - 커널이 필요 (클 수록 효과가 강해짐)
# - 커널의 자리값이 1이면 계산에 참여, 0이면 참여 안 함)
kernel = np.ones((9, 9), dtype=np.uint8)    # shape 자리에는 무조건 홀수가 들어가야 한다.
result = cv2.erode(image, kernel)
# result = cv2.erode(result, kernel)
# result = cv2.erode(result, kernel)

# 팽창(dilate)
result2 = cv2.dilate(result, kernel)

# 이미지 표시
cv2.imshow("image", image)
cv2.imshow("result", result)
cv2.imshow("result2", result2)
cv2.waitKey(0)
cv2.destroyAllWindows()