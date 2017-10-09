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
import time
import datetime

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
    
    def getFrameRate(self):
        
        # Number of frames to capture
        num_frames = 120;
         
         
        print "Capturing {0} frames".format(num_frames)
         
        # Start time
        start = time.time()
         
        # Grab a few frames
        for i in xrange(0, num_frames) :
            ret, frame = self.stream.read()
         
         
        # End time
        end = time.time()
         
        # Time elapsed
        seconds = end - start
        print "Time taken : {0} seconds".format(seconds)
         
        # Calculate frames per second
        fps  = num_frames / seconds;
        print "Estimated frames per second : {0}".format(fps);
        
        self.stream.release()
      

vs = WebcamVideoStream(src=0).start()
#vs2 = WebcamVideoStream(src=1).start()

frame_width = int(vs.stream.get(3))
frame_height = int(vs.stream.get(4))



output = np.zeros(( 450 , 600, 3), dtype="uint8")

out1 = cv2.VideoWriter('threadResult.avi',-1, 30, (600,450))

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')



while(True):
    frame1 = vs.read()
#    frame2 = vs2.read()
    frame1 = imutils.resize(frame1, width=300)
#    frame2 = imutils.resize(frame2, width=300,height=225)
    frame_size = frame1.shape
    
#    cv2.imshow("Frame", frame1)
#    cv2.imshow("Frame2", frame2)
    
    output[0:225 , 0:300] = frame1
    output[0:225 , 300:600 ] = frame1
    output[225:450 , 0:300] = frame1
    output[225:450 , 300:600] = frame1
    
    out1.write(output)
    cv2.imshow("Output",output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
vs.stop()

out1.release()