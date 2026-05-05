import cv2
img = cv2.imread("/Users/bhavyakansal/OpenCV/myimage.jpeg")

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

_ , thresh = cv2.threshold(gray , 100 , 200 , cv2.THRESH_BINARY)

#Find COUNTORS
contours , hierarchy = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img , contours , -1 , (0,255,0) , 3)

for contours in contours:
    approx = cv2.approxPolyDP(contours, 0.01 * cv2.arcLength(contours, True), True)
    
    corners = len(approx)
    if corners == 3 :
        shape_name="Triangle"
    
    elif corners == 4 :
        shape_name="Rectangle"
    
    
    elif corners == 5 :
        shape_name="Pentagon"
    
    
    elif corners > 5 :
        shape_name="Circle"
        
    else :
        shape_name="Unknown"
        
        
    cv2.drawContours(img , [approx] , -1 , (0,255,0) , 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(img , shape_name , (x,y) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (255,0,0) , 2)

     
    
cv2.imshow("Image" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()