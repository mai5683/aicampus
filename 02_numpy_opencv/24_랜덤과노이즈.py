"""
랜덤과 노이즈 만들기

파이썬에 random 모듈이 있지만... 배열 사용에 최적화된 다음 방법을 사용한다.
1. np.random.randint()      - 기존 방식
2. np.random.default_rng()  - 신규 권장되는 방식

두 방법의 비교
- np.random.randint()는 NumPy 내부의 공유 난수 생성기를 이용, default_rng는 독립 생성
- 나머지 특징은 동일

난수 생성 명령
- 정수 : np.random.randint()  /  rng.integers()
- 실수(0~1) : random() 으로 동일
- 균등분포 : uniform() 으로 동일
- 정규분포 : normal() 로 동일
- 시드 고정 : np.random.seed(42)  /  np.random.default_rng(42)  → 생성 시 ()안에 고정값 설정
"""

import numpy as np
import cv2

#-----------------------------------------------
# 1번 방법
#-----------------------------------------------
# high에 적은 값은 포함 안 됨 (미만)
# np.random.randint(최소값, 상한값(미포함), 생성크기, 생성형태)
image1 = np.random.randint(0, 256, size=(500,500), dtype=np.uint8)

#-----------------------------------------------
# 2번 방법 (권장)
#-----------------------------------------------
# rng라는 도구를 생성한 뒤
# rng.integers(최소값, 상한값(미포함), 생성크기, 생성형태)
rng = np.random.default_rng()   # rng = Random Number Generator(난수 생성기)의 줄임말
image2 = rng.integers(0, 256, size=(500,500), dtype=np.uint8)

# 이미지 출력
cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()




