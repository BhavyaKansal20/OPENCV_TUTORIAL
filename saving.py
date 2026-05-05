import cv2
image = cv2.imread("myimage.jpeg")

save = cv2.imwrite("output.jpeg" , image)

if save == True:
    print("image saved successfully")
else:
    print("error saving image")
