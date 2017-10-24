# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 08:57:12 2017

@author: NipunaC
"""

# import the necessary packages
from threading import Thread
import cv2
import imutils
import numpy as np
import time
import datetime

class VideoWriter:
    
    def __init__(self):

#        fourcc = cv2.cv.CV_FOURCC(*'XVID')
        self.out1 = cv2.VideoWriter('threadResult.avi',-1, 80, (600,450))
        self.writerStopped = False
        self.output = np.zeros(( 450 , 600, 3), dtype="uint8")

      
    def start(self):
        Thread(target=self.update, args=()).start()
        return self 
    
    def update(self):
        
        while True:
            if self.writerStopped :   
                return

            
            # otherwise, read the next frame from the stream
            if(np.any(self.output)):
                self.out1.write(self.output)
    
    def stop(self):
		# indicate that the thread should be stopped
        self.writerStopped = True
        self.out1.release()
        

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
    
    def check(self):
        return self.grabbed
        
    
    def read(self):
		# return the frame most recently read
		return self.frame
    
    def stop(self):
		# indicate that the thread should be stopped
        self.stopped = True
        self.stream.release() 
    
    def getFrameRate(self):
        
        # Number of frames to capture
        num_frames = 30;
         
         
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
        return fps
      

vs = WebcamVideoStream(src=0).start()
#vs2 = WebcamVideoStream(src=1).start()

videoWriter = VideoWriter().start()



frame_width = int(vs.stream.get(3))
frame_height = int(vs.stream.get(4))

# Capturing frame rate
rate = int(vs.getFrameRate())

#output = np.zeros(( 450 , 600, 3), dtype="uint8")

fourcc = cv2.cv.CV_FOURCC(*'H264')
#fourcc = -1
#out1 = cv2.VideoWriter('threadResult.avi',-1, rate, (600,450))

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')



while(True):
    grabbed1 = vs.check()
    
    if grabbed1==True:
    
        frame1 = vs.read()
    #    frame2 = vs2.read()
        frame1 = imutils.resize(frame1, width=300)
    #    frame2 = imutils.resize(frame2, width=300,height=225)
        frame_size = frame1.shape
        
        
    #    cv2.imshow("Frame", frame1)
    #    cv2.imshow("Frame2", frame2)
        
        videoWriter.output[0:225 , 0:300] = frame1
        videoWriter.output[0:225 , 300:600 ] = frame1
        videoWriter.output[225:450 , 0:300] = frame1
        videoWriter.output[225:450 , 300:600] = frame1
        
#        out1.write(output)
#        videoWriter.update()    
            
        cv2.imshow("Output",videoWriter.output)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    else:
        break

cv2.destroyAllWindows()
vs.stop()
videoWriter.stop()

#out1.release()