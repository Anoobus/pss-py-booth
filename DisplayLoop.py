# -*- coding: utf-8 -*-
import datetime
import BoothCam
import time


class DisplayLoop:
    def __init__(self):
        self.BoothCam = BoothCam.BoothCam()

    def runSequence(self):
        try:
            self.BoothCam.rendermainCanvas("sequence")
            self.BoothCam.showPreview()
            sequencePrefix = datetime.datetime.now().strftime("%H.%M.%S.")
            for counter in range(0,3):
                self.runCountDown()
                num = str(counter).zfill(3)
                picLocation = "pics/" + sequencePrefix + num + '_pic.jpg'
                self.BoothCam.takePic(picLocation,counter)
            self.BoothCam.hidePreview()
            time.sleep(2)
            self.BoothCam.rendermainCanvas("website")
        finally:
            self.BoothCam.shutdown()

    def runCountDown(self):
        maxNumber = 4
        for frame in range(0,maxNumber):
            self.BoothCam.renderCountdown(frame)
            time.sleep(1)
        self.BoothCam.renderCountdown(maxNumber)

