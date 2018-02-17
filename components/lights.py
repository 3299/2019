import json
import wpilib
import hal

"""
Facilitates communication between roboRIO and Arduino (for lights)
"""
class Lights(object):
    def __init__(self):
        # Init I2C for communication with Arduino
        if (hal.isSimulation()):
            # imports stub for simulation
            from components.i2cstub import I2CStub
            self.arduinoC = wpilib.I2C(wpilib.I2C.Port.kOnboard, 4, I2CStub())
        else:
            self.arduinoC = wpilib.I2C(wpilib.I2C.Port.kOnboard, 4)

    def rainbow(self):
        self.send('r')

    def stagger(self, color, fade, speed):
        commandByte = 's'

        if (color == 'blue'):
            commandC = 'b'
        else:
            commandC = 'r'
        if (fade == True):
            commandF = 't'
        else:
            commandF = 'f'

        commandS = str(speed)

        value = commandByte + commandC + commandF + commandS
        self.send(value)

    def flash(self, color, fade, speed):
        commandByte = 'f'

        if (color == 'blue'):
            commandC = 'b'
        else:
            commandC = 'r'
        if (fade == True):
            commandF = 't'
        else:
            commandF = 'f'

        commandS = str(speed)

        value = commandByte + commandC + commandF + commandS
        self.send(value)

    def send(self, data):
        print(data)
        try:
            self.arduinoC.writeBulk(bytes(data + '\n', encoding="ASCII"))
        except:
            pass
