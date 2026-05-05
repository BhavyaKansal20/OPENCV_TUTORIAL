import cv2
image = cv2.imread("/Users/bhavyakansal/OpenCV/myimage.jpeg")

if image is not None:
    cropped = image[1000:2000 , 500:1500]
    cv2.imshow("Original Image" , image) 
    cv2.imshow("Cropped Image" , cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error loading image")