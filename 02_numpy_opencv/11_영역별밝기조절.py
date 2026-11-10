import numpy as np
import cv2

# 회색 500x500 이미지 생성 (type=np.uint8이어야 함)
image = np.full((500,500), 150, dtype=np.uint8)

# 폭의 중앙(cx)과 높이의 중앙(cy)을 계산해 보자.
# image.shape는 tuple이고 각 데이터는 int인 걸 확인했다.
# print(image.shape[0], image.shape[1])
cx = image.shape[1] // 2
cy = image.shape[0] // 2

# 기본 이미지는 그대로 두고 편집본을 따로 생성해야 before/after 비교가 가능 → copy()
edit_image = image.copy()
edit_image[:cy, :cx] = 220
edit_image[:cy, cx:] = 150
edit_image[cy:, :cx] = 150
edit_image[cy:, cx:] = 100

# before/after 이미지들의 평균 밝기를 구하여 출력
print("편집 전 밝기", np.mean(image))
print("편집 후 밝기", np.mean(edit_image))

# 이미지 표시
cv2.imshow("image", image)
cv2.imshow("edit_image", edit_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
