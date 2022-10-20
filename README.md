# ANPR-With-OCR
Description:
License plate recognition are used in toll plaza, surveillance cameras, intelligent car parking, etc,. This paper proposes three modules for number plate recognition: Image acquisition, License plate detection and Character recognition. Firstly a pytorch library OpenCV is used for retrieving  the data. Then we use YOLOv5, a family of You Only Look Once(YOLO) models for detecting the number plate. Finally OCR methods i.e. Tesseract OCR and EasyOCR  are used for recognising and extracting the characters from the number plates. We used a dataset from github to train our model.On training and testing the model. The result shows EasyOCR with more than 95% accuracy on predicting the number plate than Tesseract OCR which shows 90% .Hence, EasyOCR outperforms Tesseract OCR as it uses deep learning approach for object recognition and it is efficient in real time prediction

YOlOV5: https://github.com/ultralytics/yolov5
