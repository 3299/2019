import serial

"""
Facilitates communication between roboRIO and Arduino (for lights)
"""
class Lights(object):
    def __init__(self, arduinoC):
        self.arduinoC = arduinoC
    def rainbow(self):
        self.arduinoC.set(0)
    def stagger(self, color, fade, fast):
        if(color == 'red' and fade == False and fast == False):
            self.arduinoC.set(-0.1)
        elif(color == 'red' and fade == False and fast == True):
            self.arduinoC.set(-0.2)
        elif(color == 'red' and fade == True and fast == True):
            self.arduinoC.set(-0.3)
        elif(color == 'red' and fade == True and fast == False):
            self.arduinoC.set(-0.4)
        elif(color == 'blue' and fade == False and fast == False:)
            self.arduinoC.set(-0.5)
        elif(color == 'blue' and fade == False and fast == True):
            self.arduinoC.set(-0.6)
        elif(color == 'blue' and fade == True and fast == True):
            self.arduinoC.set(-0.7)
        elif(color == 'blue' and fade == True and fast == False):
            self.arduinoC.set(-0.8)

    def flash(self, color):
        self.arduinoC.set(1)
