import cv2

image = cv2.imread("/Users/bhavyakansal/OpenCV/myimage.jpeg")

blurred = cv2.GaussianBlur(image , (21,21) , 3)
cv2.imshow("original image" , image)
cv2.imshow("blurred image" , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()