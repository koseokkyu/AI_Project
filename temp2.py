import time
from time import sleep
import picamera

#cam = picamera.PiCamera()
#time.sleep(2)

WAIT_TIME = 0.01
start = time.time()
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 20

    for filename in camera.capture_continuous("/home/pi/picture/img{timestamp:%H-%M-%S-%f}.jpg", use_video_port=True):
        if(time.time() - start) > 5:
            break;
            
