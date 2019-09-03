# -*- coding: utf-8 -*-
import sys
from time import sleep
from picamera import PiCamera
from PIL import Image
import numpy

global o
global arr

arrayList = []
def renderBlock(target, camera, pos, isSpecial):
    img = Image.open(target)
    ##pad = Image.new('RGB', (
    ##    ((img.size[0] + 31) // 32) * 32,
    ##    ((img.size[1] + 15) // 16) * 16,
    ##    ))
    ##pad.paste(img, (0,0))
    ##o = camera.add_overlay(pad.tostring(), img.size, fullscreen=0, window=(pos[0],pos[1],img.size[0],img.size[1]))
    o = camera.add_overlay(pad.tostring(), img.size, fullscreen=0, window=(pos[0],pos[1],img.size[0],img.size[1]))
    o.alpha = 155
    o.layer = 3
    ##if isSpecial != True:
    ##    arrayList.append(o)

def render1():
    renderBlock('content/Layout-clean.jpg',camera, (40,10),False)


##def render2():
##    renderBlock('horz-block.jpg',camera, (10,10),False)
##    renderBlock('vert-half-block.jpg',camera, (100,10),False)
##    renderBlock('horz-block.jpg',camera, (10,55),False)
##    renderBlock('vert-half-block.jpg',camera, (10,55),False)
##    renderBlock('horz-block.jpg',camera, (10,100),False)
##
##def render3():
##    renderBlock('vert-block.jpg',camera, (80,10),False)
##    renderBlock('horz-half-block.jpg',camera, (30,10),False)
##    renderBlock('horz-half-block.jpg',camera, (30,55),False)
##    renderBlock('horz-half-block.jpg',camera, (30,100),False)
##
##def clearRender():
##    for alphaCount in range(0,254):
##        for x in arrayList:
##            if alphaCount > 60:
##                x.alpha = 255 - alphaCount + 60
##
##        sleep(0.001)
##    for x in arrayList:
##        x.layer = 0
##    del arrayList[:]


##numpy.zeros((5,2))
##numpy[0,2] = True
##numpy[1,2] = True

def timedSnapShot(fileName,picNum):
    ##render1()
    ##clearRender()

    ##render2()
    ##clearRender()

    ##render3()
    ##clearRender()

    ##camera.capture(fileName, resize=(320,180))
    camera.capture("pics/" + fileName)
    ##renderBlock(fileName,camera, (10,110 + (picNum * 320) + (picNum * 2)), True)




camera = PiCamera()
camera.resolution=(1920,1080)
camera.framerate=24
try:
    camera.start_preview()
    counter = 0
    Max = 10
    KeepRunning = True
    render1()
    while (KeepRunning):
        counter = counter + 1
        KeepRunning = counter < 5
        num = str(counter).zfill(3)
        timedSnapShot(num + '_pic.jpg',0)
        print("loop " + num)
        sleep(5)
except KeyboardInterrupt:
    pass
    print("keyboard press, shutting down")
finally:
    camera.close()
sys.exit
