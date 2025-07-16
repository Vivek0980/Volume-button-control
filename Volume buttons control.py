import cv2
import mediapipe as mp
import time
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import hands_tracking_project_module as htpm
wcam=640
hcam=480

detector=htpm.HandDetector()


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = cast(interface, POINTER(IAudioEndpointVolume))

#volume.GetMute()
#volume.GetMasterVolumeLevel()
volume_range=volume.GetVolumeRange()
min_volume_range=volume_range[0]
max_volume_range=volume_range[1]




cam=cv2.VideoCapture(0)
cam.set(3,wcam)
cam.set(4,hcam)
volbar=400
while True:
    ret,frame=cam.read()
    if not ret:
        break
    
    img=detector.find_hands(frame)

    lmlist=detector.find_position(img,draw=False)
    if len(lmlist)!=0:
        x1=lmlist[4][1]
        y1=lmlist[4][2]
        x2=lmlist[8][1]
        y2=lmlist[8][2]
        cx=(x1+x2)//2
        cy=(y1+y2)//2
        #print(x1,x2,cx)q
        #print(y1,y2,cy)
        cv2.circle(img,(x1,y1),radius=4,color=(0,255,0),thickness=3)
        cv2.circle(img,(x2,y2),radius=4,color=(0,255,0),thickness=3)
        cv2.line(img,(x1,y1),(x2,y2),color=(0,255,0),thickness=3)
        cv2.circle(img,(cx,cy),radius=4,color=(255,0,0),thickness=3)
        length=math.hypot(x2-x1,y2-y1)
        min_length=10
        max_length=180
        if length<24:
            cv2.circle(img,(cx,cy),radius=4,color=(255,0,255),thickness=3)
        vol=np.interp(length,[24,180],[min_volume_range,max_volume_range])
        vol_bar=np.interp(length,[24,180],[400,150])
        print(vol)
        volume.SetMasterVolumeLevel(vol, None)
        #print(volume.GetMasterVolumeLevel())
        cv2.rectangle(img,(50,150),(85,400),color=(0,255,255),thickness=3)
        cv2.rectangle(img,(50,int(vol_bar)),(85,400),color=(0,255,255),thickness=cv2.FILLED)
        #volume.SetMute(1,None)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break