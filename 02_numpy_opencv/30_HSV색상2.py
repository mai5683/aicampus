"""
HSV 색상을 사용
"""

import numpy as np
import cv2

# fruit = cv2.imread("./images/orange.png")
# fruit = cv2.imread("./images/strawberry.png")
# fruit = cv2.imread("./images/grape.png")
# fruit = cv2.imread("./images/pear.png")
fruit = cv2.imread("./images/banana.png")

if fruit is None:
    print("이미지가 존재하지 않습니다")
    exit(1)

# BGR → HSV 변환
hsv = cv2.cvtColor(fruit, cv2.COLOR_BGR2HSV)

# HSV 채널 분리
h = hsv[:, :, 0]    # 색상 (0 ~ 179), 모든 색상 종류를 표현
s = hsv[:, :, 1]    # 채도 (0 ~ 255), 색의 진하기를 표현
v = hsv[:, :, 2]    # 명도 (0 ~ 255), 색의 밝기를 표현

# 채도 채널에 OTSU이진화를 적용해서 0 <---> 255로 분리
# 채도가 0인 곳에는 검정을, 채도가 255인 곳에는 흰색을 설정
threshold, otsu = cv2.threshold(
    s, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("s의 임계값", threshold)

# mask = s > 40   # 진한 색상(과일) 찾기
mask = otsu == 255

result = fruit.copy()

result[mask] = (0, 0, 0)    # 대상은 검정
result[~mask] = (255, 255, 255)     # 나머지 흰색

# 리사이즈 후 병합
r1 = cv2.resize(fruit, (300, 300))
r2 = cv2.resize(result, (300, 300))
merge = np.hstack((r1, r2))

# 이미지 출력
cv2.imshow("merge", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()