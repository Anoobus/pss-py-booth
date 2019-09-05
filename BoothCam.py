# -*- coding: utf-8 -*-
from picamera import PiCamera
from PIL import Image
import os

READY_PATH = 'content/Get-Ready-Background.jpg'
INSTRUCTION_PATH = 'content/Instructions-Background.jpg'
WEBSITE_PATH = 'content/Website-Background.jpg'


class UsingBoothCam:
    def __init__(self):
        self.cam = BoothCam()
        print('ctor hit')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('shutting down')
        self.cam.shutdown()

    def __enter__(self):
        print('returning cam ref')
        return self.cam

class BoothCam:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (2592, 1944)
        self.camera.framerate = 24
        self.previewOn = False
        print('setting up mainCanvas')
        self.mainCanvas = self.__renderBlock(READY_PATH, (0, 0))
        self.mainCanvas.layer = 2
        print('setting up countdown')
        self.countdownSection = self.__renderBlock('content/countdown/Blank.jpg', (0, 0))
        self.countdownSection.layer = 0
        print('setting up thumbNail')
        self.thumbNailSection = self.__renderBlock('content/thumb/new/thumb_0.jpg', (40, 410))
        self.thumbNailSection.layer = 0

    def __getPaddedImage(self, imagePath):
        img = Image.open(imagePath)
        pad = Image.new('RGB', (self.safeResolution(img.size[0], img.size[1])))
        pad.paste(img, (0, 0))
        return pad

    def rendermainCanvas(self, bgType):
        targetImage = READY_PATH
        if (bgType == "instructions"):
            targetImage = INSTRUCTION_PATH
        if (bgType == "website"):
            targetImage = WEBSITE_PATH
        print('setting mainCanvas to ' + targetImage)
        self.mainCanvas.update(self.__getPaddedImage(targetImage).tobytes())
        print('hide thumbnail layer')
        self.thumbNailSection.layer = 0

    def __renderBlock(self, target, pos):
        img = Image.open(target)
        pad = self.__getPaddedImage(target)
        o = self.camera.add_overlay(pad.tobytes(),
            size=img.size,
            fullscreen=0,
            window=(pos[0], pos[1], img.size[0], img.size[1]))
        o.alpha = 255
        return o

    def renderCountdown(self, num):
        target = 'content/countdown/' + str(num) + '.jpg'
        pad = self.__getPaddedImage(target)
        self.countdownSection.update(pad.tobytes())

    def takePic(self, imgName, picNum):
        self.camera.capture(imgName)
        #os.system('mpg123 -q /home/pi/Projects/content/Click.mp3')
        self.showThumb(imgName, picNum)

    def showThumb(self, location, picNum):
        size = (self.safeResolution(256, 341))
        thumb = Image.open(location)
        thumb.thumbnail(size, Image.ANTIALIAS)
        self.thumbNailSection.update(thumb.tobytes())
        self.thumbNailSection.layer = 3

    def hideThumb(self):
        self.thumbNailSection.layer = 0

    def hidePreview(self):
        self.camera.stop_preview()

    def showPreview(self):
        self.camera.start_preview(fullscreen=False,
            window=(405, 218, self.safeResolution(800, 600)))

    def shutdown(self):
        self.camera.close()

    def safeResolution(self, x, y):
        # // = Floor division - division that results into whole number
        #      adjusted to the left in the number line
        return ((x + 31) // 32 * 32, (y + 15) // 16 * 16)