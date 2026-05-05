import cv2 
image = cv2.imread("/Users/bhavyakansal/OpenCV/myimage.jpeg")

if image is None:
    print("Error loading image")
else : 
    print("Image loaded successfully")
    
    resized = cv2.resize(image , (4000 , 4000))
    cv2.imshow("Original image" , image)
    cv2.imshow("Resized image" , resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()