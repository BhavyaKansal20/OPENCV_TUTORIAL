import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

capture = cv2.VideoCapture(0)

while True:
    ret , frame = capture.read()
    gray=cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    detect = face_cascade.detectMultiScale(gray , 1.1 , 5)
    
    for (x , y , w , h) in detect:
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (0,255,0) , 2)
    
        roi_gray = gray[y:y+h , x:x+w]
        roi_color = frame[y:y+h , x:x+w]
    
    eye_detect = eye_cascade.detectMultiScale(roi_gray , 1.1 , 5)
    if len(eye_detect) > 0:
        cv2.putText(frame , "Eyes Detected" , (x , y-20) , cv2.FONT_HERSHEY_COMPLEX , 0.6 , (255,0,0) , 2)
    
    smile_detect = smile_cascade.detectMultiScale(roi_gray , 1.1 , 5)
    if len(smile_detect) > 0:
        cv2.putText(frame , "Smile Detected" , (x , y-10) , cv2.FONT_HERSHEY_COMPLEX , 0.6 , (255,0,0) , 2)
        
    
    cv2.imshow("Face , Eye and Smile Detection" , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
capture.release()
cv2.destroyAllWindows()