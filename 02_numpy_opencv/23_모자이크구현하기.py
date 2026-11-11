"""
실습 과제 : 모자이크 구현하기
원하는 이미지에 모자이크를 구현한 뒤 images/mosaic.jpg에 저장하시기 바랍니다.
# 이미지 저장 명령
cv2.imwrite("저장위치", 이미지)


모자이크의 구현 방법은 다음과 같습니다.

모자이크는 일정 크기의 픽셀을 하나로 합쳐서 표시하는 기법입니다.
일정 크기를 10이라고 가정하고 문제를 풉니다 (나중에 조절 가능합니다)
이미지를 10x10씩 잘라서 각각의 평균을 구합니다.
해당 영역에 구해진 평균값을 대입합니다.

우선 한 곳에만 적용해보시고 필요하다면 반복 등을 사용하셔도 좋습니다.
"""

import numpy as np
import cv2

image = cv2.imread("./images/plus1.jpg")



for y in range(0, 800, 10):
    for x in range(0, 800, 10):
        mosaic = image[y:y+10, x:x+10]
        average = np.mean(mosaic, axis=(0, 1))
        image[y:y + 10, x:x + 10] = average

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("./images/mosaic.jpg", image)

