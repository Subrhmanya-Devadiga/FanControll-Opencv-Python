import cv2
import os


class Human:
    def __init__(self):
        self.trained_facedata = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.webcam = cv2.VideoCapture(0)
        self.fan1 = False
        self.fan2 = False
        self.allfans = False
        while True:
            self.successfull_frame_read, self.frame = self.webcam.read()
            self.grayscale_image = cv2.cvtColor(self.frame,cv2.COLOR_BGR2GRAY)
            self.face_cordinates = self.trained_facedata.detectMultiScale(self.grayscale_image)
            try:
                if self.face_cordinates.any():
                    for (x,y,h,w) in self.face_cordinates:
                        try:
                            if x <= 300 and y>0:
                                if not self.fan1:
                                    print("Fan1 on")
                                    self.fan1 = True
                                    
                                    #print(self.face_cordinates)
                            else:
                                try:
                                    if self.fan1:
                                        self.fan1 = False
                                        print("Fan1 off")
                                        
                                except:
                                    pass
                        except:
                            pass
                        try:
                            if x > 300 and y>0:
                                if not self.fan2:
                                    print("Fan2 on")
                                    self.fan2 = True
                                    
                                    #print(self.face_cordinates)
                            else:
                                if self.fan2 :
                                    self.fan2 = False
                                    print("Fan2 off")
                                    
                        except:
                            pass
            except:
                self.fan2 = False
                self.fan1 = False
                print("Fan1 off")
                print("Fan2 off")
            for (x,y,w,h) in self.face_cordinates:
                cv2.rectangle(self.frame,(x,y),(x+w,y+h),(0,256,0),2)
                cv2.imshow('detected_images',self.frame)
            self.key = cv2.waitKey(1)
        
            if self.key == 113:
                break
humandetect = Human()