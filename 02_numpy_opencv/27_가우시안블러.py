"""
블러(blur)

- 이미지에서의 블러는 이미지를 부드럽고 흐릿하게 만드는 작업을 처리
- 표 형태의 영역을 만들어서 이미지를 누르는 연산을 시도하며 이 영역을 커널(kernel)이라고 부른다.
- 하는 주된 이유는 노이즈(빛번짐 등) 제거, 이미지 평활화, 윤곽선 정리
- 평균 블러, 가우시안 블러, 미디언 블러 등이 존재
"""

import numpy as np
import cv2

# 이미지 읽기 (노이즈가 있는 이미지 선택)
noise = cv2.imread("./images/cat_noise1.jpg")

# 노이즈 제거 (가우시안 블러)
# X처리방침 :
# 가우시안 분포가 가로 방향으로 얼마나 퍼지는지 결정합니다.
# 0 : OpenCV가 커널 크기를 기준으로 자동 계산 (권장)
# 1 : 중심 픽셀 주변에 가중치가 집중
# 3 : 가중치가 더 넓게 퍼짐
# 5 : 더욱 넓게 퍼짐
# Y 처리방침 :
# 세로 방향으로 가우시안 분포가 퍼지는 정도입니다.
# 0 : sigmaX와 동일한 값 사용 (권장)
# 1 : 세로 표준편차 1
# 3 : 세로 표준편차 3
# gaussian = cv2.GaussianBlur(이미지, 커널크기, X처리방침, Y처리방침)
gaussian3x3 = cv2.GaussianBlur(noise, (3, 3), 0)
gaussian5x5 = cv2.GaussianBlur(noise, (5, 5), 0)    # 권장
gaussian7x7 = cv2.GaussianBlur(noise, (7, 7), 0)
gaussian9x9 = cv2.GaussianBlur(noise, (9, 9), 0)


# 결과 확인
cv2.imshow("noise", noise)
cv2.imshow("gaussian-3x3", gaussian3x3)
cv2.imshow("gaussian-5x5", gaussian5x5)
cv2.imshow("gaussian-7x7", gaussian7x7)
cv2.imshow("gaussian-9x9", gaussian9x9)

cv2.waitKey(0)
cv2.destroyAllWindows()


