"""
목표 : pillow 이미지를 opencv로 변환해서 출력
"""

import cv2
import numpy as np
from PIL import Image

# pillow --> opencv
try:
    image_pil = Image.open("./images/cat.jpg")
except Exception:
    print("이미지가 없습니다")
    exit(1)

# pillow 이미지를 numpy 배열로 읽는다.
image_change = np.array(image_pil)        # np.array : 이미지 배열 생성 명령

# RGB → BGR
image_change = cv2.cvtColor(image_change, cv2.COLOR_RGB2BGR)

# 출력
cv2.imshow("change", image_change)
cv2.waitKey(0)
cv2.destroyAllWindows()

