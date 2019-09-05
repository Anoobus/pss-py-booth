# -*- coding: utf-8 -*-
import datetime
import BoothCam
import time


class DisplayLoop:
#    def __init__(self):
#        self.BoothCam

    def runSequence(self):
        with BoothCam.UsingBoothCam() as cam:
            print('set canvas to sequence')
            cam.rendermainCanvas("sequence")
            print('show preview')
            cam.showPreview()
            sequencePrefix = datetime.datetime.now().strftime("%H.%M.%S.")
            for counter in range(0,3):
                print('run countdown')
                self.runCountDown(cam)
                num = str(counter).zfill(3)
                picLocation = "pics/" + sequencePrefix + num + '_pic.jpg'
                print('take pic')
                cam.takePic(picLocation,counter)
            print('turn off preview')
            cam.hidePreview()
            time.sleep(2)
            print('render website canvas')
            cam.rendermainCanvas("website")
            print('wait 2')
            time.sleep(2)


    def runCountDown(self, cam):
        maxNumber = 4
        for frame in range(0,maxNumber):
            print('render countdown frame %s',frame)
            cam.renderCountdown(frame)
            time.sleep(1)
        print('render countdown frame %s',maxNumber)
        cam.renderCountdown(maxNumber)

