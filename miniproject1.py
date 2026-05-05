# write a code in python and using opencv : 
# task have to load image , grayscale it , show it , save it 
# also take path of image from user along with option to save or show , 
# if save output save iamge name alog with output message.

import cv2

image = cv2.imread(input("Enter image path : "))
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

option = input("save or show : ")

if option == "save":
    save = cv2.imwrite(input("enter file name to save : ") , gray)
    print("Image saved successfully")
elif option == "show" :
    cv2.imshow("Grayscale Image" , gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Image shown Successfully")
else:
    print("Invalid Option")