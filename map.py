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
