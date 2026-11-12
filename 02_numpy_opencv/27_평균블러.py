"""
블러(blur)

- 이미지에서의 블러는 이미지를 부드럽고 흐릿하게 만드는 작업을 처리
- 표 형태의 영역을 만들어서 이미지를 누르는 연산을 시도하며 이 영역을 커널(kernel)이라고 부른다.
- 하는 주된 이유는 노이즈(빛번짐 등) 제거, 이미지 평활화, 윤곽선 정리
- 평균 블러, 가우시안 블러, 미디언 블러 등이 존재
"""

import numpy as np
import cv2

# 이미지 읽기 (노이즈가 있는 이미지 선택)
noise = cv2.imread("./images/cat_noise1.jpg")

# 노이즈 제거 (평균 블러)



# 결과 확인
cv2.imshow("noise", noise)
cv2.waitKey(0)
cv2.destroyAllWindows()


