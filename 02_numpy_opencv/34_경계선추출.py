"""
경계선 추출(Canny)

색상 또는 밝기가 급격하게 변화하는 지점
이진화 후에 사용하면 정확도가 올라감. (고려해야 할 변수가 적어짐.)
"""

import numpy as np
import cv2

# 이미지 읽기
image = cv2.imread("./images/strawberry.png")

# 일반적인 전처리 : grayscale → (blur) → binarize(otsu) → morphology
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary = cv2.threshold(
    blur, 0, 255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((21,21), dtype=np.uint8)
# (1) 팽창만 할 경우 - 결과가 부담스러움
# increase = cv2.dilate(binary, kernel)
# (2) 팽창+수축 같이 할 경우 - 외형은 유지되면서 끊어진 부분이 상당 부분 복구됨
increase = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# 경계선 추출(Canny)
# - cv2. Canny(이미지, 낮은 경계 임계값, 높은 경계 임계값)
# - 밝기 변화가 50 미만이면 경계가 아님. 50~150이면 조건부 경계, 150 이상이면 경계
# - 밝기가 아니라 밝기 변화량이라는 것을 주의해야 함.
edge = cv2.Canny(binary, 50, 150)

# 이미지 출력
cv2.imshow("increase", increase)
cv2.imshow("edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()



