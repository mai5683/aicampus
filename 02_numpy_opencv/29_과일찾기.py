"""
과일찾기

images/strawberry.png
images/banana.png
images/pear.png
images/grape.png
images/orange.png

에서 물체만 흰색 나머진 검정색!
"""

import cv2
import numpy as np

# 이미지 읽기
fruit = cv2.imread("./images/strawberry.png")
# fruit = cv2.imread("./images/banana.png")
# fruit = cv2.imread("./images/pear.png")
# fruit = cv2.imread("./images/grape.png")
# fruit = cv2.imread("./images/orange.png")

if fruit is None:
    print("이미지가 존재하지 않습니다")
    exit(1)

# 전처리
# (1) grayscale
gray = cv2.cvtColor(fruit, cv2.COLOR_BGR2GRAY)

# (2) gaussian blur
# blur = cv2.GaussianBlur(gray, (5, 5), 0)
blur = cv2.medianBlur(gray, 5)

# (3) binarize
# - 혹시... 평균밝기로는 안되겠니?
# - opencv야... 니가 좀 안되겠니? 적응형 이진화
avg = np.mean(blur)
# print(avg)
ret, binary = cv2.threshold(
    blur, avg, 255,
    cv2.THRESH_BINARY #기준값보다 큰걸 흰색으로
    # cv2.THRESH_BINARY_INV # 기준값보다 큰걸 검정색으로
)

# 리사이징
size = (300, 300)
# fruit_resize = cv2.resize(fruit, size)
gray_resize = cv2.resize(gray, size)
blur_resize = cv2.resize(blur, size)
binary_resize = cv2.resize(binary, size)

total = np.hstack((
    gray_resize, blur_resize, binary_resize
))

# 이미지 출력
cv2.imshow("total", total)
cv2.waitKey(0)
cv2.destroyAllWindows()





