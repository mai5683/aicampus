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

# 원본 이미지 정보
# print(image.shape)  # 5376x8064


# 이미지 크기 조정(resize) :
# - cv2.resize(이미지, (크기정보))
# - opencv는 일반적인 형식 (폭 x 높이)를 사용
# resize = cv2.resize(image, (500, 300))  # 500x300
# resize = cv2.resize(image, None, fx=0.5, fy=0.5)    # 폭과 높이를 50%씩 감소

# 폭을 300px로 정했을 때, 높이를 계산해서 설정하도록 구현
aspect_ratio = image.shape[1] / image.shape[0]    # 기존 이미지의 너비/높이
print("종횡비", aspect_ratio)
width = 300
# height = width / aspect_ratio
height = int(width / aspect_ratio)
resize = cv2.resize(image, (width, height))


# 이미지 표시
# cv2.imshow("image", image)
cv2.imshow("resize", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
