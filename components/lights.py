
"""
Facilitates communication between roboRIO and Arduino (for lights)
"""
class Lights(object):
    def __init__(self, arduinoC):
        self.arduinoC = arduinoC

    def rainbow(self):
        value = bytes([0x00, 0x00, 0xff, 0x00])
            
        try:
            print(value)
            self.arduinoC.transaction(value, 0)
        except:
            pass

    def stagger(self, value):
        try:
            print(value)
            self.arduinoC.transaction(value, 0)
        except:
            pass

    def flash(self, value):
        try:
            print(value)
            self.arduinoC.transaction(value, 0)
        except:
            pass
