import cv2 

image = cv2.imread(input("Enter the image path : "))


options = input("Draw a Line"  
           "Write Text on Image"
           "Draw a Circle" 
           "Draw a Rec : ")

if options == "Draw a Line":
    pt1 = (input("Enter the x and y coordinates of the starting point : "))
    pt2 = (input("Enter the x and y coordinates of the ending point : "))
    color = (input("Enter the color of the line in BGR format : "))
    thickness = input("Enter the thickness of the line : ")
    cv2.line(image , pt1 , pt2 , color , thickness)
    
    option = ("1. show" , "2. save")
    option = input("Select an option from the following : " + option)
    if option == "1. show":
        cv2.imshow("line drawn " , image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif option == "2. save":
        save_path = input("Enter the path to save the image : ")
        cv2.imwrite(save_path , image)  
    else : 
        print("Invalid option selected")
        

elif options == "Write Text on Image":
    text = input("Enter the text to be written on the image : ")
    org = (input("Enter the x and y coordinates of the bottom-left corner of the text : "))
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = input("Enter the font scale factor : ")
    color = (input("Enter the color of the text in BGR format : "))
    thickness = input("Enter the thickness of the text : ")
    cv2.putText(image , text , org , font , fontScale , color , thickness)
    
    option = ("1. show" , "2. save")
    option = input("Select an option from the following : " + option)
    if option == "1. show":
        cv2.imshow("line drawn " , image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif option == "2. save":
        save_path = input("Enter the path to save the image : ")
        cv2.imwrite(save_path , image)  
    else : 
        print("Invalid option selected")
    
    cv2.imshow("text drawn" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
elif options == "Draw a Circle":
    center = (input("Enter the x and y coordinates of the center of the circle : "))
    radius = input("Enter the radius of the circle : ")
    color = (input("Enter the color of the circle in BGR format : "))
    thickness = input("Enter the thickness of the circle : ")
    cv2.circle(image , center , radius , color , thickness)
    
    option = ("1. show" , "2. save")
    option = input("Select an option from the following : " + option)
    if option == "1. show":
        cv2.imshow("line drawn " , image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif option == "2. save":
        save_path = input("Enter the path to save the image : ")
        cv2.imwrite(save_path , image)  
    else : 
        print("Invalid option selected")
    
    cv2.imshow("circle drawn" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


elif options == "Draw a Rec":
    pt1 = tuple(map(int, input("Top-left: ").strip("() ").split(',')))
    pt2 = tuple(map(int, input("Bottom-right: ").strip("() ").split(',')))
    color = tuple(map(int, input("Color: ").strip("() ").split(',')))
    thickness = int(input("Enter the thickness of the rectangle : "))
    cv2.rectangle(image , pt1 , pt2 , color , thickness)
    
    option = input("save or show : ")
    if option == "show":
        cv2.imshow("line drawn " , image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif option == "save":
        save_path = input("Enter the path to save the image : ")
        cv2.imwrite(save_path , image)  
    else : 
        print("Invalid option selected")
    
    cv2.imshow("rectangle drawn" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()