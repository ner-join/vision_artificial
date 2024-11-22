# from PIL import Font
import log_report
from tkinter import ttk, font
import tkinter as tk 
import numpy as np
import cv2
# from PIL import ImageFont as font
from PIL import ImageDraw, Image, ImageTk

import run_camera

class App(ttk.Frame):
    def __init__(self,master = None):
        try:
            super().__init__(master)
            self.loggerReport = log_report.ReportLog()

            self.runCamera = run_camera.RunCamera(src=0,nameThread="CamPc1")

            self.master = master
            self.flagStop = False
            self.width = 640
            self.height = 480
            self.master.geometry("%dx%d" % (self.width,self.height))
            self.loggerReport.logger.info('GuiCreated')

            self.createWidgets()
            self.createWindowBlack()
            self.createPhotoBlack()
            self.master.mainloop()
        except Exception as e:
            self.loggerReport.logger(f"GUI Not Created:{e}")
        
    def createWindowBlack(self):
        frame = np.zeros([320,480,3],dtype=np.uint8)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imgArray = Image.fromarray(frame)
        imgTk = ImageTk.PhotoImage(image = imgArray)
        self.labelCamera1.configure(image=imgTk)
    
    def createPhotoBlack(self):
        frame = np.zeros([80,120,3],dtype=np.uint8)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imgArray = Image.fromarray(frame)
        imgTk = ImageTk.PhotoImage(image = imgArray)
        self.labelPhoto.configure(image=imgTk)

    def createWidgets(self):
        #Button Start
        self.btnStartCamera = tk.Button(self.master, text="Start",bg='#0EEA1F'
                                         ,fg="#FFFFFF",width=12,command=self.cameraStart)
        self.btnStartCamera.place(x=120,y=440)

        #Button Photo
        self.btnPhoto = tk.Button(self.master, text="Foto",bg='#0000FF'
                                         ,fg="#FFFFFF",width=12,command=self.takePhoto)
        self.btnPhoto.place(x=220,y=440)

        #Button Stop
        self.btnStopCamera = tk.Button(self.master, text="Stop",bg='#FF00BB'
                                         ,fg="#FFFFFF",width=12,command=self.cameraStop)
        self.btnStopCamera.place(x=320,y=440)
        
        #TextCameraName
        self.fontText = font.Font(family='Helvetica',size=8,weight='bold')
        self.labelCameraName = tk.Label(self.master,text=f"Camera 1",fg="#000000",)
        self.labelCameraName['font'] = self.fontText
        self.labelCameraName.place(x=20,y=5)

        #Label as Window
        self.labelCamera1 = tk.Label(self.master,borderwidth=2,relief='solid')
        self.labelCamera1.place(x=20,y=20)

        #PhotoName
        self.fontText = font.Font(family='Helvetica',size=8,weight='bold')
        self.labelCameraName = tk.Label(self.master,text=f"Photo",fg="#000000",)
        self.labelCameraName['font'] = self.fontText
        self.labelCameraName.place(x=510,y=5)
        #Photo windows
        self.labelPhoto = tk.Label(self.master,borderwidth=2,relief='solid')
        self.labelPhoto.place(x=510,y=20)

    def cameraStart(self):
        print('StartCamera')
        self.flagStop = False
        self.runCamera.start()
        self.showFrameInLabel()
    
    def cameraStop(self):
        print('StopCamera')
        self.flagStop = True
    
    def takePhoto(self):
        print('Take photo')
        try:
            if(self.runCamera.grabbed and not self.flagStop):
                frameCamera = self.runCamera.frame
                frameCamera = cv2.resize(frameCamera,(120,80))
                frame = cv2.cvtColor(frameCamera, cv2.COLOR_BGR2RGB)
                imgArray = Image.fromarray(frame)
                imgTk = ImageTk.PhotoImage(image = imgArray)
                self.labelPhoto.configure(image=imgTk)
                self.labelPhoto.image = imgTk
        except Exception as e:
            self.loggerReport.logger.error(f"Error {e}")


    def showFrameInLabel(self):
        try:
            if(self.runCamera.grabbed and not self.flagStop):
                frameCamera = self.runCamera.frame
                frameCamera = cv2.resize(frameCamera,(480,320))
                frame = cv2.cvtColor(frameCamera, cv2.COLOR_BGR2RGB)
                imgArray = Image.fromarray(frame)
                imgTk = ImageTk.PhotoImage(image = imgArray)
                self.labelCamera1.configure(image=imgTk)
                self.labelCamera1.image = imgTk
                self.labelCamera1.after(30,self.showFrameInLabel)
        except Exception as e:
            self.loggerReport.logger.error(f"Error {e}")


def main():
     print("Hola")
     root = tk.Tk()
     root.title("MyFirstGUI")
     appRunCamera = App(master=root)
