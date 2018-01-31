import json
import wpilib
from components.i2cstub import I2CStub

"""
Facilitates communication between roboRIO and Arduino (for lights)
"""
class Lights(object):
    def __init__(self):
        # Init I2C for communication with Arduino
        self.arduinoC = wpilib.I2C(wpilib.I2C.Port.kOnboard, 4, I2CStub())

    def rainbow(self):
        self.arduinoC.set(0)
    def stagger(self, color, fade, speed):
        #data = {'effect': 'stagger', 'color': color, 'fade': fade, 'speed': speed}
        #try:
        #self.arduinoC.transaction(json.dumps(data).encode('ASCII'), 0)
        self.arduinoC.transaction(b'sbt255\n', 0)
        #except:
        #    pass

    def flash(self, color):
        self.arduinoC.set(1)
