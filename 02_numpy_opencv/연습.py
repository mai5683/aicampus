import numpy as np
import cv2

image = cv2.imread("./images/plus1.jpg")

mosaic = image[0:10, 0:10]
average = np.mean(mosaic, axis=(0, 1))
print(average)

image[0:10, 0:10] = average

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
