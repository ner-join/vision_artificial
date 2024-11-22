import log_report
import cv2
import threading

class RunCamera():
    def __init__(self,src=0,nameThread= "CameraThread"):
        try:
            self.logReport = log_report.ReportLog()
            self.src = src
            self.nameThread = nameThread
            self.capture = None
            self.grabbed = None
            self.frame = None
            self.flagStop = False
            self.logReport.logger.info("Init constructor run camera")
        except Exception as e:
            self.logReport.logger.info(f"Error constructor run camera {e}")
    
    def start(self):
        try:
            self.flagStop = False
            self.capture = cv2.VideoCapture(self.src)
            self.grabbed, self.frame = self.capture.read()
            
            if self.capture.isOpened():
                self.cameraThread = threading.Thread(target=self.get,name=self.nameThread, daemon=True)
                self.cameraThread.start()

                self.logReport.logger.info("Init start run camera")
            else:
                self.logReport.logger.warning("Capture not opened")
        except Exception as e:
            self.logReport.logger.info(f"Error constructor run camera {e}")
    
    def get(self):
        try:
            while self.capture.isOpened() and self.grabbed and not self.flagStop:
                self.grabbed, self.frame = self.capture.read()
                if not self.grabbed:
                    break
        except Exception as e:
            self.logReport.logger.error(f"Error in get:{e}")
    
    def stop(self):
        self.flagStop = True
        self.capture.release()
