import cv2
import numpy as np
import datetime
from PIL import ImageGrab

from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

timeStamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

fourChar = cv2.VideoWriter_fourcc('m' , 'p' , '4', 'v')

captured_video = cv2.VideoWriter(timeStamp + '.avi', fourChar, 10.0, (width, height))


while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height ))
    img_np = np.array(img)
    color_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow(' Not Medal', color_img)
    captured_video.write(color_img)

    if cv2.waitKey(10) == ord('q'):
        break