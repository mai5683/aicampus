"""
원근 변환(Perspective Transform)

- 비스듬하게 촬영한 문서나 물체를 정면에서 바라본 것처럼 변환하는 기법
- 변환 전, 후의 좌표를 알아야 함.

명령 :
- cv2.getPerpectiveTransform(before, after)
- cv2.warpPerspective(이미지, 변환행렬, (폭,높이))
"""

import numpy as np
import cv2

# 이미지 입력
image = cv2.imread("../03_tkinter/images/tilted.png")
if image is None:
    print("이미지 없음")
    exit(1)

# 이미지 연산
# 1. 현재 이미지의 모서리 좌표를 딴다.
# (Tip) np.float32()로 생성하면 dtype 지정을 생략할 수 있다.
before = np.array([
    [140, 68],    # [왼쪽 위],
    [1128, 217],  # [오른쪽 위]
    [1418, 974],  # [오른쪽 아래]
    [52, 1073]    # [왼쪽 아래]
], dtype=np.float32)

# 2. 펼쳐졌을 때의 크기
width = 1000
height = 700

# 3. 꼭짓점이 옮겨질 위치 (원보노가 동일하게 11시부터 시계방향 순서로 배치)
after = np.array([
    [0, 0],                # 좌상단(11시)
    [width-1, 0],          # 우상단(1시)
    [width-1, height-1],   # 우하단(5시)
    [0, height-1],         # 좌하단(7시)
], dtype=np.float32)

# 4. before와 after를 주고 어떻게 이동시켜야 하는지 과정이 담긴 변환행렬 구하기.
matrix = cv2.getPerspectiveTransform(before, after)
# print(matrix)

# 5. 이미지 변환 처리
result = cv2.warpPerspective(image, matrix, (width, height))

# 이미지 출력
cv2.imshow("image", image)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

