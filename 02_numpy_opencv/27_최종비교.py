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

# 노이즈 제거 (평균 블러)
gaussian = cv2.GaussianBlur(noise, (5, 5), 0)
median = cv2.medianBlur(noise, 5)
average = cv2.blur(noise, (5, 5))

# 밝은 픽셀의 개수를 카운트 (종류별로)
# 밝다 = BGR이 200 이상 (200,200,200)
# print(noise >= 200)     # 각 채널까지 모두 검사
# print(noise[:,:,0] >= 200)  # B채널
# print(noise[:,:,1] >= 200)  # G채널
# print(noise[:,:,2] >= 200)  # R채널
mask_noise = (
    (noise[:,:,0] >= 200) &     # 블루채널 200 이상
    (noise[:,:,1] >= 200) &     # 그린채널 200 이상
    (noise[:,:,2] >= 200)       # 레드채널 200 이상
)
mask_gaussian = (
    (gaussian[:,:,0] >= 200) &     # 블루채널 200 이상
    (gaussian[:,:,1] >= 200) &     # 그린채널 200 이상
    (gaussian[:,:,2] >= 200)       # 레드채널 200 이상
)
mask_median = (
    (median[:,:,0] >= 200) &     # 블루채널 200 이상
    (median[:,:,1] >= 200) &     # 그린채널 200 이상
    (median[:,:,2] >= 200)       # 레드채널 200 이상
)
mask_average = (
    (average[:,:,0] >= 200) &     # 블루채널 200 이상
    (average[:,:,1] >= 200) &     # 그린채널 200 이상
    (average[:,:,2] >= 200)       # 레드채널 200 이상
)
# print(noise[mask].size)    # RGB까지 카운트
print("noise", len(noise[mask_noise]))    # 채널 빼고 픽셀만 카운트
print("gaussian", len(gaussian[mask_gaussian]))
print("median", len(median[mask_median]))
print("average", len(average[mask_average])) 

# 크기 조절 후 병합
r1 = cv2.resize(noise, (300, 300))
r2 = cv2.resize(gaussian, (300, 300))
r3 = cv2.resize(median, (300, 300))
r4 = cv2.resize(average, (300, 300))
result = np.hstack((r1, r2, r3, r4))

# 결과 확인
# cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


