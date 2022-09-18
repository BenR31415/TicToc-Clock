import gpio_controls
import time
from datetime import datetime
from picamera import PiCamera

flashObj = gpio_controls.flash()
flashObj.turnOn()

camera = PiCamera()
camera.rotation = 180

camera.start_preview()
count = 0
inputStr = ""
while True:
    if count % 10 == 0:
        inputStr = input()
        if inputStr == "quit":
            break
    filepath = f"/home/pi/Documents/trainingData/{inputStr}/{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
    camera.capture(filepath)
    count += 1
    time.sleep(0.1)


camera.stop_preview()