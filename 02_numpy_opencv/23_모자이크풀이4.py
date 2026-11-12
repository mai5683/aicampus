"""
# 실습 과제 : 모자이크 구현하기

원하는 이미지에 모자이크를 구현한 뒤 `images/mosaic.jpg`에 저장하시기 바랍니다.
```python
# 이미지 저장 명령
cv2.imwrite("저장위치", 이미지)
```

모자이크의 구현 방법은 다음과 같습니다.

- 모자이크는 일정 크기의 픽셀을 하나로 합쳐서 표시하는 기법입니다.
- 일정 크기를 `10`이라고 가정하고 문제를 풉니다 (나중에 조절 가능합니다)
- 이미지를 `10x10`씩 잘라서 각각의 평균을 구합니다.
- 해당 영역에 구해진 평균값을 대입합니다.

우선 한 곳에만 적용해보시고 필요하다면 반복 등을 사용하셔도 좋습니다
"""

import numpy as np
import cv2

# 이미지 읽기
origin = cv2.imread("./images/sample.jpg")

# 이미지 분리
mosaic = origin.copy()

# 모자이크 처리
block = 10 # 모자이크 처리할 규격 (색이 뭉개질 범위, 클수록 모자이크가 심해짐)
# x = 0~이미지의폭까지 block만큼 증가 # 모자이크 처리 시작지점 X
# y = 0~이미지의높이까지 block만큼 증가 # 모자이크 처리 시자지점 Y
# origin_width = mosaic.shape[1]
height, width = mosaic.shape[:2]
# 모든 줄에 모자이크 처리
for y in range(0, height, block):
    for x in range(0, width, block):
        # print("x", x)
        area = mosaic[y:y+block, x:x+block] # 구역 슬라이싱
        # print(area)
        # print(area.shape)
        # print(np.mean(area, axis=(0,1)))
        avg = np.mean(area, axis=(0,1)).astype(np.uint8)
        # print(avg.dtype)
        mosaic[y:y+block, x:x+block] = avg

# 이미지 표시
cv2.imshow("origin", origin)
cv2.imshow("mosaic", mosaic)
cv2.waitKey(0)
cv2.destroyAllWindows()




