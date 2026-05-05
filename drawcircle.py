import cv2
image = cv2.imread("/Users/bhavyakansal/OpenCV/myimage.jpeg")

if image is None :
    print("Error loading image")
else :
    print("Image loaded successfully")
    center = (1000 , 700)
    radius = 580
    color = (0 , 0 , 255)
    thickness = 5
    cv2.circle(image , center , radius , color , thickness)
    cv2.imshow("circle drawn" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()