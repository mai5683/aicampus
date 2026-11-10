import numpy as np
import cv2

# 이미지 배경 생성
image = np.zeros((500, 500), dtype=np.uint8)

# 그림 그리기
# - 높이(100~400), 폭(100~400) 사이 영역에 밝기를 120으로 설정해라.
image[100:400, 100:400] = 120

# 눈 그리기
image[150:200, 150:200] = 0
image[150:200, 300:350] = 0

# 입 그리기
image[300:350, 150:350] = 0

# 이미지 출력
# cv2.imshow("창이름", 이미지)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

