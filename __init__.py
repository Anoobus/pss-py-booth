# -*- coding: utf-8 -*-
#import BoothCam
import DisplayLoop
from time import sleep

print('here we go')

print('now loop')
try:
    loopy = DisplayLoop.DisplayLoop()
    loopy.runSequence()
finally:
    camera.close()

sleep(3)
print('im done')
