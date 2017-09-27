# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:16:29 2017

@author: NipunaC
"""

# import the necessary packages
from threading import Thread
import cv2
import imutils
import numpy as np

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
vs2 = WebcamVideoStream(src=1).start()

frame_width = int(vs.stream.get(3))
frame_height = int(vs.stream.get(4))

output = np.zeros(( 450 , 600, 3), dtype="uint8")

out1 = cv2.VideoWriter('threadResult.avi',-1, 60, (600,450))

while(True):
    frame1 = vs.read()
    frame2 = vs2.read()
    frame1 = imutils.resize(frame1, width=300,height=225)
    frame2 = imutils.resize(frame2, width=300,height=225)

    
#    cv2.imshow("Frame", frame1)
#    cv2.imshow("Frame2", frame2)
    
    output[0:225 , 0:300] = frame1
    output[0:225 , 300:600 ] = frame2
    output[225:450 , 0:300] = frame1
    output[225:450 , 300:600] = frame2
    
    out1.write(output)
    cv2.imshow("Output",output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
vs.stop()
vs2.stop()
out1.release()