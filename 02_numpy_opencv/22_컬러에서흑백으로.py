"""
컬러에서 흑백으로 변환하는 방법

- 직접 : BGR의 가중평균을 계산
- 명령 : opencv에 있는 변환명령을 사용
"""

import numpy as np
import cv2

# 이미지 읽기
color = cv2.imread("./images/cat.jpg")

# 컬러를 흑백으로 변환
# 직접 : 0.299R + 0.587G + 0.114B
blue = color[:, :, 0]
green = color[:, :, 1]
red = color[:, :, 2]

gray = 0.299 * red + 0.587 * green + 0.114 * blue
gray = gray.round().astype(np.uint8)
# print(gray.dtype)

# opencv에서 제공하는 명령을 사용해서 처리
gray2 = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)

# 색상 반전 (color를 변경)
# reverse = 밝은 걸 어둡게, 어두운 걸 밝게
reverse = 255 - color

# 따뜻한 색감으로 변경 (color를 변경)
# warm = R채널 증가, B채널 감소 (255를 넘어갈 가능성이 있음)
warm = color.astype(int)
warm[:, :, 0] -= 50     # B채널 50 감소
warm[:, :, 2] += 50     # R채널 50 증가
warm = np.clip(warm, 0, 255).astype(np.uint8)

# 차가운 색감으로 변경 (color를 변경)
# cold = B채널 증가, R채널 감소
cold = color.astype(int)
cold[:, :, 1] += 50     # B채널 50 증가
cold[:, :, 2] -= 50     # R채널 50 감소
cold = np.clip(cold, 0, 255).astype(np.uint8)

# 이미지를 밝게
# bright = BGR 모두 증가
bright = color.astype(int)
bright += 50
bright = np.clip(bright,0,255).astype(np.uint8)

# 이미지를 어둡게
# dark = BGR 모두 감소
dark = color.astype(int)
dark -= 50
dark = np.clip(dark, 0,255).astype(np.uint8)

# 대비 조절
# 밝은 부분은 더 밝게, 어두운 부분은 더 어둡게
# contrast = 128을 기준으로 차이가 클 수록 더 늘리거나 감소시키기
# - 100은 128보다 작으니까 더 값을 줄인다
# - 200은 128보다 크니까 더 값을 키운다
contrast = color.astype(float)  # np.float32, np.float64
contrast -= 128
contrast *= 1.5
contrast += 128
contrast = np.clip(contrast, 0, 255).astype(np.uint8)
print(contrast)


# 이미지 출력
# cv2.imshow("color", color)
# cv2.imshow("gray", gray)
# cv2.imshow("gray2", gray2)
# cv2.imshow("reverse", reverse)
# cv2.imshow("warm", warm)
# cv2.imshow("cold", cold)
# cv2.imshow("bright", bright)
# cv2.imshow("dark", dark)
cv2.imshow("contrast", contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()

