#import sys
#from time import sleep
#from picamera import PiCamera
#from PIL import Image
#import os
#import RPi.GPIO as GPIO
#import time

#from datetime import datetime

#global arr

#global countdownSection
#global mainCanvas
#global thumbNail

#def renderBlock(target, camera, pos):
    #img = Image.open(target)
    #pad = getPaddedImage(target)
    #o = camera.add_overlay(pad.tobytes(),size= img.size,fullscreen=0, window=(pos[0],pos[1],img.size[0],img.size[1]))
    #o.alpha = 255
    #return o

#def renderCountdown(num):
    #target = 'content/countdown/' + str(num) + '.jpg'
    #pad = getPaddedImage(target)
    #global countdownSection
    #try:
        #countdownSection.update(pad.tobytes())
    #except NameError:
        #countdownSection = renderBlock(target,camera, (0,0))
        #countdownSection.layer = 2

#def getPaddedImage(imagePath):
    #img = Image.open(imagePath)
    #pad = Image.new('RGB', (
        #((img.size[0] + 31) // 32) * 32,
        #((img.size[1] + 15) // 16) * 16,
        #))
    #pad.paste(img, (0,0))
    #return pad



#def rendermainCanvas(bgType):
    #global mainCanvas
    #targetImage = 'content/Get-Ready-Background.jpg'
    #if (bgType == "instructions"):
        #targetImage = 'content/Instructions-Background.jpg'
    #if (bgType == "website"):
        #targetImage = 'content/Website-Background.jpg'

    #try:
        #mainCanvas.update(getPaddedImage(targetImage).tobytes())
    #except NameError:
        #mainCanvas = renderBlock(targetImage,camera, (0,0))
        #mainCanvas.layer = 2

#def runCountDown():
    #maxNumber = 4
    #for frame in range(0,maxNumber):
        #renderCountdown(frame)
        #sleep(1)
    #renderCountdown(maxNumber)

#size = 256,144
#def showThumb(location,picNum):
    #global thumbNail
    #thumb = Image.open(location)
    #saveLoc = 'content/thumb/new/thumb_' + str(picNum) + '.jpg'
    #os.remove(saveLoc)
    #thumb.thumbnail(size,Image.ANTIALIAS)
    #thumb.save(saveLoc,"JPEG")
    #try:
        #thumbNail.update(getPaddedImage(saveLoc).tobytes())
        #thumbNail.layer = 3
    #except NameError:
        #thumbNail = renderBlock(saveLoc,camera,(40,410))
        #thumbNail.layer = 3

#def hideThumb():
    #global thumbNail
    #thumbNail.layer = 0

#def runSequence():
    #rendermainCanvas("sequence")
    #prev = camera.start_preview(fullscreen=False, window=(405,218,1515,852 ))
    #sequencePrefix = datetime.now().strftime("%H.%M.%S.")
    #for counter in range(0,3):
        #runCountDown()
        #num = str(counter).zfill(3)
        #picLocation = "pics/" + sequencePrefix + num + '_pic.jpg'
        #camera.capture(picLocation)
        #os.system('mpg123 -q /home/pi/Projects/content/Click.mp3')
        #showThumb(picLocation,counter)
    #camera.stop_preview()
    #time.sleep(2)
    #hideThumb()
    #rendermainCanvas("website")



#camera = PiCamera()
#camera.resolution=(1515,852)
#camera.framerate=24
#try:
    #target = "instructions"
    #rendermainCanvas(target)
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    #lastCheck = datetime.now()
    #while True:
        #input_state = GPIO.input(18)
        #if input_state == False:
            #runSequence()
            #time.sleep(0.2)

        #if ((datetime.now() - lastCheck).seconds > 4):
            #if (target == "instructions"):
                #target = "website"
            #else:
                #target = "instructions"
            #rendermainCanvas(target)
            #lastCheck = datetime.now()

#except KeyboardInterrupt:
    #pass
    #print("keyboard press, shutting down")
#finally:
    #camera.close()
#sys.exit