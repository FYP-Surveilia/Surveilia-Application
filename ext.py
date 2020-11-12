# import cv2
#
# #print("Before URL")
# cap = cv2.VideoCapture('rtsp://admin:123456@192.168.1.216/H264?ch=1&subtype=0')
# #print("After URL")
#
# while True:
#
#     #print('About to start the Read command')
#     ret, frame = cap.read()
#     #print('About to show frame of Video.')pip
#     cv2.imshow("Capturing",frame)
#     #print('Running..')
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
import urllib.request
import cv2
import numpy as np

url = "http://192.168.0.103:8080/shot.jpg?rnd=693379"
while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)

    cv2.imshow('test', img)
    cv2.waitKey(10)
