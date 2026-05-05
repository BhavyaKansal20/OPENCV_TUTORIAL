import cv2
image = cv2.imread("/Users/bhavyakansal/OpenCV/myimage.jpeg")

if image is None :
    print("Error loading image")
else :
    print("Image loaded successfully")
    text = "Long and Cool Hairsstyle"
    org = (100 , 100)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1.2
    color = (0 , 0, 255)
    thickness = 2
    cv2.putText(image , text , org , font , fontScale , color , thickness)
    cv2.imshow("text drawn" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()