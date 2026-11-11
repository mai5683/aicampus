"""
실습 문제 : 이미지 합치기
파일명 : 19_이미지합성.py

인터넷에서 이미지 2장을 다운받아 가로, 세로로 합쳐보세요

가로로 합칠 때에는 두 이미지의 높이를 모두 400px로 맞추시기 바랍니다.
세로로 합칠 때에는 두 이미지의 폭을 모두 300px로 맞추시기 바랍니다.
"""


import numpy as np
import cv2

# 이미지 읽기
# (Tip) 경로에서 .은 현재를 의미하고 ..은 상위 경로를 의미
# image1 = cv2.imread("images/plus1.jpg")
image1 = cv2.imread("./images/plus1.jpg")   # .은 현재 위치를 의미
image2 = cv2.imread("images/plus2.jpg")

if image1 is None or image2 is None:
    print("이미지가 존재하지 않습니다")
    exit(1)

# 이미지를 합성
# print(image1.shape, image2.shape)
# width1 = image1.shape[1]
# height1 = image1.shape[0]
h1, w1 = image1.shape[:2]
h2, w2 = image2.shape[:2]
print(w1, h1, w1/h1)
print(w2, h2, w2/h2)

new_w1 = 300
new_h1 = round(new_w1 / (w1/h1))

new_w2 = 300
new_h2 = round(new_w2 / (w2/h2))

resize1 = cv2.resize(image1, (new_w1, new_h1))
resize2 = cv2.resize(image2, (new_w1, new_h1))
print(resize1.shape, resize2.shape)

# 합성
# plus = np.hstack((resize1, resize2))
plus = np.concatenate((resize1, resize2), axis=1)


# 합성된 결과를 출력
# cv2.imshow("image1", resize1)
# cv2.imshow("image2", resize2)
cv2.imshow("plus", plus)
cv2.waitKey(0)
cv2.destroyAllWindows()


