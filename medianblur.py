import cv2

image = cv2.imread("/Users/bhavyakansal/OpenCV/noisy_img.png")

blurred = cv2.medianBlur(image , 3)
cv2.imshow("original image" , image)
cv2.imshow("blurred image" , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()