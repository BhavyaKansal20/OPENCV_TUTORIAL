import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("recorded_video.mp4" , codec , 30 , (frame_width , frame_height))

while True :
    success , image = camera.read()
    
    if not success:
        print("error capturing video")
        break 
    
    recorder.write(image)
    cv2.imshow("video captured" , image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quitting...")
        break  
    
camera.release()
recorder.release()
cv2.destroyAllWindows()
    