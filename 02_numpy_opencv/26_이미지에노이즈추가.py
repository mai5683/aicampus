"""
이미지에 노이즈 추가하기
학습을 위해 인위적으로 어떤 이미지에 노이즈를 추가해보려고 합니다.
(ex : 뜬금없는 흰픽셀, 검정픽셀, 주변과 어울리지 않는 픽셀 등)

1. 원하는 이미지를 불러온다
2. 노이즈를 생성한다
  - -30 ~ 30의 범위를 가지는 무작위 정수로 생성  → noise1
  - 평균이 0, 표준편차가 30인 무작위 실수를 생성 → noise2
  - 명령은 공식문서를 찾아보세요
3. 각각의 노이즈를 이미지에 합성한다
4. 합성된 결과를 출력 및 저장한다
5. 만약 파일명이 sample.jpg라면 합성결과는 sample_with_noise1.jpg여야 한다
"""

import numpy as np
import cv2

# 이미지 읽기
origin = cv2.imread("./images/cat.jpg")

# 노이즈 생성
print(origin.shape)     # (1024, 1024, 3)
height, width, channel = origin.shape
print(height, width, channel)

rng = np.random.default_rng()
# noise1 = rng.integers(-30, 30, size=(height, width, channel), dtype=int)
noise1 = rng.integers(-30, 30, size=origin.shape, dtype=int, endpoint=True)
noise2 = rng.normal(0, 30, size=origin.shape)
# print(noise2)
# print(noise2.dtype)

# 노이즈 합성
result1 = origin.copy() + noise1
result1 = np.clip(result1, 0, 255).astype(np.uint8)

result2 = origin.copy() + noise2
result2 = np.clip(result2, 0, 255).astype(np.uint8)

# 저장 및 출력
cv2.imwrite("./images/cat_noise1.jpg", result1)
cv2.imwrite("./images/cat_noise2.jpg", result2)

cv2.imshow("origin", origin)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)
cv2.waitKey(0)
cv2.destroyAllWindows()


