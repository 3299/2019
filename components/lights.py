import json
import wpilib
import hal

"""
Facilitates communication between roboRIO and Arduino (for lights).
Handled entirely in the main loop. Do not pass in an instance to
components.
"""
class Lights(object):
    def __init__(self):
        # Init I2C for communication with Arduino
        if (hal.isSimulation()):
            # import stub for simulation
            from components.i2cstub import I2CStub
            self.arduinoC = wpilib.I2C(wpilib.I2C.Port.kOnboard, 4, I2CStub())
        else:
            self.arduinoC = wpilib.I2C(wpilib.I2C.Port.kOnboard, 4)

        self.allianceColor = 'red'

    def setColor(self, color):
        self.allianceColor = color

    def run(self, options):
        if (options['effect'] != 'rainbow'):
            # default to alliance color
            options.setdefault('color', self.allianceColor)

            if (options['color'] == 'blue' or options['color'] == wpilib.DriverStation.Alliance.Blue):
                commandC = 'b'
            else:
                commandC = 'r'


            options.setdefault('fade', False)
            if (options['fade'] == True):
                commandF = 't'
            else:
                commandF = 'f'

            options.setdefault('speed', '')
            commandS = str(options['speed'])

            if (options['effect'] == 'stagger'):
                commandByte = 's'
            elif (options['effect'] == 'flash'):
                commandByte = 'f'

            value = commandByte + commandC + commandF + commandS

        elif (options['effect'] == 'rainbow'):
            value = 'r'

        self.send(value)

    def send(self, data):
        try:
            self.arduinoC.writeBulk(bytes(data + '\n', encoding="ASCII"))
        except:
            pass
