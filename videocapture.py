import cv2 

capture = cv2.VideoCapture(0)

while True :
    ret , frame = capture.read()
    
    if not ret :
        print("Error captureing video")
        break

    cv2.imshow("video captured" , frame)
    
    if cv2.waitKey(1) & 0xFF == ord('b') :
        print("quitting....")
        break


capture.release()
cv2.destroyAllWindows()

