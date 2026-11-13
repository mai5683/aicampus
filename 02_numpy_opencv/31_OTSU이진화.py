"""
오츠(OTSU) 이진화

- 1979년 일본 오츠 노부유키라는 사람이 발표한 이진화 기법
- 이미지의 밝기 분포를 분석하여 임계값(Threshold)을 자동으로 결정하는 방법
- 특정 채널(R, G, B, H, S, V)에도 적용이 가능.. 분포를 분석해서 양극화시키는 알고리즘
"""

import cv2
import numpy as np

# 이미지 읽기
# image = cv2.imread("./images/screws.jpg")
image = cv2.imread("./images/strawberry.png")
if image is None:
    print("이미지 없음")
    exit(1)

# grayscale        → 이진화가 들어가려면 grayscale이 선행되어야 한다.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blur         → grayscale 후엔 blur처리 : 이진화를 위한 통상적인 순서
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# OTSU binarize : 임계값에 0을 적어야 한다. (자동 조정이 됨)
threshold, otsu = cv2.threshold(
    blur, 0, 255,
    # cv2.THRESH_BINARY_INV     # thresh보다 큰 걸 흰색(255)으로 만들고 나머지 버림 (수동)
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU     # OTSU 이진화 적용 (자동)
)

# 반환되는 threshold는 결정된 임계값, otsu는 결과이미지
print("오츠 이진화의 임계값", threshold)

# 이미지 표시
cv2.imshow("image", image)
cv2.imshow("otsu", otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()



