from PIL.Image import ImageTransformHandler
import cv2
import numpy as np
import pytesseract

#location of the pytesseract
pytesseract.pytesseract.tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract.exe"

cascade= cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_russian_plate_number.xml") #detection algorithm
# dictionary, till it matches it will iterate
states={"AN":"Andaman and Nicobar",
    "AP":"Andhra Pradesh","AR":"Arunachal Pradesh",
    "AS":"Assam","BR":"Bihar","CH":"Chandigarh",
    "DN":"Dadra and Nagar Haveli","DD":"Daman and Diu",
    "DL":"Delhi","GA":"Goa","GJ":"Gujarat",
    "HR":"Haryana","HP":"Himachal Pradesh",
    "JK":"Jammu and Kashmir","KA":"Karnataka","KL":"Kerala",
    "LD":"Lakshadweep","MP":"Madhya Pradesh","MH":"Maharashtra","MN":"Manipur",
    "ML":"Meghalaya","MZ":"Mizoram","NL":"Nagaland","OD":"Odissa",
    "PY":"Pondicherry","PN":"Punjab","RJ":"Rajasthan","SK":"Sikkim","TN":"TamilNadu",
    "TR":"Tripura","UP":"Uttar Pradesh", "WB":"West Bengal","CG":"Chhattisgarh",
    "TS":"Telangana","JH":"Jharkhand","UK":"Uttarakhand"}

def extract_num(img_filename):
    img=cv2.imread(img_filename) # reading the image
    #Img To Gray
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting the image to grey for processing
    nplate=cascade.detectMultiScale(gray,1.1,4) 
    #crop portion
    for (x,y,w,h) in nplate: #indirectly its a bounding boxes splitted into this variable
        wT,hT,cT=img.shape  #channel, is nothing but the image shape
        a,b=(int(0.02*wT),int(0.02*hT)) #tuple, getting the float value imag shape and converting into integer
        plate=img[y+a:y+h-a,x+b:x+w-b,:] #cropping the plate , finally representing the detected contours by drawing rectangles around the edges
      
        #make the img more darker to identify LPR
        kernel=np.ones((1,1),np.uint8) # kernal nothing but a blank window size 1,1
        plate=cv2.dilate(plate,kernel,iterations=1) #Dilation is a technique where we expand the image. It adds the number of pixels to the boundaries of objects in an image
        plate=cv2.erode(plate,kernel,iterations=1) #shrinking th image ,  If any of the pixels in a kernel is 0, then all the pixels in the kernel are set to 0
        plate_gray=cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
        (thresh,plate)=cv2.threshold(plate_gray,127,255,cv2.THRESH_BINARY) #Thresholding is a method of image segmentation, in general it is used to create binary images
        #read the text on the plate
        read=pytesseract.image_to_string(plate)
        read=''.join(e for e in read if e.isalnum())
        stat=read[0:2]
        print(stat)
        print(read)
       # cv2.rectangle(img,(x,y),(x+w,y+h),(51,51,255),2) #numericals are color
       # cv2.rectangle(img,(x-1,y-40),(x+w+1,y),(51,51,255),-1) #to draw rectangle over number plate to highlight
       # cv2.putText(img,read,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,255,255),2) # show the number on the rectangle


        cv2.imshow("plate",plate)
        
    cv2.imwrite("Result.jpeg",img)
    cv2.imshow("Result",img) #showing th image
    if cv2.waitKey(0)==113: # using image so zero / video means 1
        exit()               #if we r pressing 'q' it will exit
    cv2.destroyAllWindows() #close rest of the function 

extract_num("testing1.jpeg") #calling the function