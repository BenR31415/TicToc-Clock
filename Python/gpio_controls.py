import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class flash():
    def __init__(self) -> None:
        self.ledPin = 2
        GPIO.setup(self.ledPin, GPIO.OUT)
        self.turnOff()
    
    def turnOn(self) -> None:
        GPIO.output(self.ledPin, GPIO.HIGH)
    
    def turnOff(self) -> None:
        GPIO.output(self.ledPin, GPIO.LOW)

class Switch():
    def __init__(self) -> None:
        self.switchPin = 3
        GPIO.setup(self.switchPin, GPIO.IN)
    
    def checkSwitchIsPressed(self) -> bool:
        return not GPIO.input(self.switchPin)