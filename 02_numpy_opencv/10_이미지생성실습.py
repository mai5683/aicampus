import numpy as np
import cv2

image = np.full((500,500), 0, dtype=int)
image = np.clip(image, 0, 255).astype(dtype=np.uint8)

image[150:350, 150:350] = 200
image[200:240, 190:230] = 0
image[200:240, 270:310] = 0
image[280:300, 200:300] = 0


cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()