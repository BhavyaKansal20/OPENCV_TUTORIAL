import cv2
image = cv2.imread("/Users/bhavyakansal/OpenCV/myimage.jpeg")

if image is None:
    print("error loading image")
else : 
    print("image loaded successfully")
    pt1 = (0,1024)
    pt2 = (2048 , 1024)
    cv2.line(image , pt1 , pt2 , (0,0,255) , 5)
    cv2.imshow("line drawn " , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()