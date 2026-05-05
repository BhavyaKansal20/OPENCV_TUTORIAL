import cv2
import numpy as np

image = cv2.imread("/Users/bhavyakansal/OpenCV/flower.png" , cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image , 50 , 150)
cv2.imshow("original image" , image)
cv2.imshow("edges detected" , edges)
cv2.waitKey(0)
cv2.destroyAllWindows()