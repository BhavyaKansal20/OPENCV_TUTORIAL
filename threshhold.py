import cv2


image = cv2.imread("/Users/bhavyakansal/OpenCV/liongrayimage.png" , cv2.IMREAD_GRAYSCALE)

ret , thresh_img = cv2.threshold(image , 120 , 255 , cv2.THRESH_BINARY)
cv2.imshow("original image" , image)
cv2.imshow("thresholded image" , thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()