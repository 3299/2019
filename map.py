"""
Defines port numbers for motors and sensors.
"""

class Map(object):
    def __init__(self):
        # Motors have suffix 'M'. All motors use PWM.
        self.frontLeftM  = 2
        self.frontRightM = 3
        self.backLeftM   = 0
        self.backRightM  = 1

        # Sensors have suffix 'S'. Gyro uses SPI, everything else uses the DIO.
        self.gyroS = 0
        self.arduino = 9
