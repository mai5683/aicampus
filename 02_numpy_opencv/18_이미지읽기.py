"""
실제 이미지를 읽어서 표시하기
"""

import cv2

# 이미지 읽기 - cv2.imread("경로"
image = cv2.imread("images/flowers.jpg")
# print(image)
# print(type(image))    # numpy.ndarray

# 이미지가 없는 경우를 제거
if image is None:
    print("이미지가 존재하지 않습니다")
    exit(1)

# 이미지 표시
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
