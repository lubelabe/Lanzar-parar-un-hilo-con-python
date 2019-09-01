import threading
import PruebaOne
import time

c = threading.Thread(target = PruebaOne.DetectionFace)
c.start()

for i in xrange(10,0,-1):
    time.sleep(1)
    print i
    if i <= 1:
        PruebaOne.run = False
