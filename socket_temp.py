import time
import picamera
import socket


HOST = 'server-ip'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

cam = picamera.PiCamera()
time.sleep(2)

# Capture the images
for frame in range(FRAMES):
    # Note the time before the capture
    # with picamera.PiCamera() as cam:
    msg = cam.capture('/home/pi/picture/frame%03d.jpg' % frame)
    # Wait for the next capture. Note that we take into
    # account the length of time it took to capture the
    # image when calculating the delay
    s.send(msg.encode(encoding='utf_8', errors='strict'))
    data = s.recv(1024)
    print ('result: ' + data.decode())

s.close()
cam.close()