import numpy as np
import cv2
from mss.darwin import MSS as mss
from PIL import Image
from threading import Thread
from imutils.video import FPS
import imutils

mon = {'top': 59, 'left': 0, 'width': 411, 'height': 712}

class MSSVideoStream:
    def __init__(self, mon, name="MSSVideoStream"):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = mss()
        self.mon = mon
        self.frame = self.stream.grab(self.mon)

        # initialize the thread name
        self.name = name

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        t = Thread(target=self.update, name=self.name, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                sct.close()
                return

            # otherwise, read the next frame from the stream
            self.frame = self.stream.grab(self.mon)

    def read(self):
        # return the frame most recently read
        return np.array(self.frame)

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

cap = MSSVideoStream(mon)
fps = FPS()
fps.start()
cap.start()

while 1:
    img = cap.read()
    fps.update()
    cv2.imshow('test', imutils.resize(np.array(img), width=200))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
fps.stop()
print(fps.fps())
