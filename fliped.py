import cv2
image = cv2.imread("/Users/bhavyakansal/OpenCV/myimage.jpeg")

if image is None : 
    print("Error loading image")
else :
    flipped = cv2.flip(image , 0)
    cv2.imshow("original image" , image)
    cv2.imshow("Flipped image" , flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()