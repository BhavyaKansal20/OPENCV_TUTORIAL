import cv2 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True:
    ret , frame = capture.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    detect = face_cascade.detectMultiScale(gray , 1.1 , 5)
    
    for (x , y , w , h) in detect:
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (0,255,0) , 2)
        
    cv2.imshow("Face Detection" , frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.release()
cv2.destroyAllWindows()