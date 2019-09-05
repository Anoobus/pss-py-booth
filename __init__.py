# -*- coding: utf-8 -*-
import DisplayLoop
from time import sleep

print('here we go')

print('now loop')

loopy = DisplayLoop.DisplayLoop()
loopy.runSequence()


sleep(3)
print('im done')

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
