# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:31:59 2017

@author: NipunaC
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:06:24 2017

@author: NipunaC
"""

import numpy as np
import cv2

frame_size = 300


cap0 = cv2.VideoCapture(0)
cap0.set(3,frame_size)
cap0.set(4,frame_size)

cap1 = cv2.VideoCapture(1)
cap1.set(3,frame_size)
cap1.set(4,frame_size)

#cap2 = cv2.VideoCapture(2)
#cap2.set(3,frame_size)
#cap2.set(4,frame_size)

#cap3 = cv2.VideoCapture(3)
#cap3.set(3,frame_size)
#cap3.set(4,frame_size)

frame_width = int(cap0.get(3))
frame_height = int(cap0.get(4))

frame_width2 = int(cap1.get(3))
frame_height2 = int(cap1.get(4))

#frame_width3 = int(cap2.get(3))
#frame_height3 = int(cap2.get(4))

#frame_width4 = int(cap3.get(3))
#frame_height4 = int(cap3.get(4))

output = np.zeros(( frame_height *2 , frame_width * 2, 3), dtype="uint8")
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.


out1 = cv2.VideoWriter('outpy.avi',-1, 10, (frame_width*2,frame_height*2))

#out1 = cv2.VideoWriter('outpy.avi',cv2.cv.CV_FOURCC('M','R','L','E'), 10, (frame_width,frame_height))
#out1 = cv2.VideoWriter('outpy.avi',cv2.cv.CV_FOURCC('F','L','V','1'), 10, (frame_width,frame_height))
#out2 = cv2.VideoWriter('outpy2.avi',cv2.cv.CV_FOURCC('M','R','L','E'), 10, (frame_width2,frame_height2))
#out2 = cv2.VideoWriter('outpy2.avi',-1, 10, (frame_width2,frame_height2))


while(True):
    # Capture frame-by-frame
    ret1, frame1 = cap0.read()
    ret2, frame2 = cap1.read()
#    ret3, frame3 = cap2.read()
#    ret4, frame4 = cap3.read()
   
    if ret1==True and ret2==True    :
        
        # write the  frame1
#        out1.write(frame1)
#        cv2.imshow('frame',frame1)
        
#        out2.write(frame2)
#        cv2.imshow('frame2',frame2)
        
        output[0:frame_height , 0:frame_width] = frame1
        output[0:frame_height , frame_width:frame_width*2 ] = frame2
        output[frame_height:frame_height*2 , 0:frame_width] = frame1
        output[frame_height:frame_height*2  , frame_width:frame_width*2 ] = frame2
        
        
        out1.write(output)
        cv2.imshow('output',output)
        
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap0.release()
cap1.release()
#cap2.release()
#cap3.release()

#qout2.release()
cv2.destroyAllWindows()