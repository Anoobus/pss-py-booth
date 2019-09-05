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
        #self.camera.resolution = (1640, 922)
        self.camera.resolution = (1515, 852)
        self.camera.framerate = 24
        self.previewOn = False
        print('setting up mainCanvas')
        self.mainCanvas = self.__renderBlock(READY_PATH, (0, 0))
        self.mainCanvas.layer = 2
        print('setting up countdown')
        self.countdownSection = self.__renderBlock('content/countdown/Blank.jpg', (0,0))
        self.countdownSection.layer = 0
        print('setting up thumbNail')
        self.thumbNailSection = self.__renderBlock('content/thumb/new/thumb_0.jpg',(40,410))
        self.thumbNailSection.layer = 0

    def __getPaddedImage(self, imagePath):
        img = Image.open(imagePath)
        pad = Image.new('RGB', (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
            ))
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
        #self.camera.resolution = (1640,922)
        self.camera.capture(imgName)
        #self.camera.resolution = (1515, 852)
        #os.system('mpg123 -q /home/pi/Projects/content/Click.mp3')
        #self.showPreview()
        self.showThumb(imgName,picNum)

    def showThumb(self, location,picNum):
        size = 256,144
        thumb = Image.open(location)
        saveLoc = 'content/thumb/new/thumb_' + str(picNum) + '.jpg'
        os.remove(saveLoc)
        thumb.thumbnail(size,Image.ANTIALIAS)
        thumb.save(saveLoc,"JPEG")
        self.thumbNailSection.update(self.__getPaddedImage(saveLoc).tobytes())
        self.thumbNailSection.layer = 3

    def hideThumb(self):
        self.thumbNailSection.layer = 0

    def hidePreview(self):
        self.camera.stop_preview()

    def showPreview(self):
        self.camera.start_preview(fullscreen=False,
            window=(405,218,1515,852 ))

    def shutdown(self):
        self.camera.close()