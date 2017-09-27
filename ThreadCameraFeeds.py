# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:16:29 2017

@author: NipunaC
"""

# import the necessary packages
from threading import Thread
import cv2
import imutils

class WebcamVideoStream:

    def __init__(self, src=0):
		# initialize the video camera stream and read the first frame
		# from the stream
        self.frameSize = 300; 
        self.stream = cv2.VideoCapture(src)

        (self.grabbed, self.frame) = self.stream.read()


		# initialize the variable used to indicate if the thread should
		# be stopped
        self.stopped = False
    
    def start(self):
		# start the thread to read frames from the video stream
		Thread(target=self.update, args=()).start()
		return self
    
    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:   
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()
            
    
    def read(self):
		# return the frame most recently read
		return self.frame
    
    def stop(self):
		# indicate that the thread should be stopped
        self.stopped = True
        self.stream.release() 
       

vs = WebcamVideoStream(src=0).start()
#vs2 = WebcamVideoStream(src=1).start()

while(True):
    frame = vs.read()
#    frame2 = vs2.read()
    frame = imutils.resize(frame, width=400)
    cv2.imshow("Frame", frame)
    
#    cv2.imshow("Frame2", frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
vs.stop()
#vs2.stop()