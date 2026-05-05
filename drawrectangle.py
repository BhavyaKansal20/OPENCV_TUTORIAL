import cv2
image = cv2.imread("/Users/bhavyakansal/OpenCV/myimage.jpeg")

if image is None :
    print("Error loading image")
else :
    print("Image loaded successfully")
    pt1 = (600 , 50)
    pt2 = (1524 , 1375)
    color = (0 , 0 , 255)
    thickness = 5
    cv2.rectangle(image , pt1 , pt2 , color , thickness)
    cv2.imshow("rectangle drawn" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()