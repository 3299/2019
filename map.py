"""
Defines port numbers for motors and sensors.
"""

class Map(object):
    def __init__(self):
        # Motors have suffix 'M'. All motors use PWM.
        self.frontLeftM  = 0
        self.frontRightM = 3
        self.backLeftM   = 1
        self.backRightM  = 5
        self.elevatorM   = 2
        self.intakeM     = 6
        self.jawsM       = 10
        #self.winchM      = 7
        self.frontLift   = 4
        self.backLift    = 7
        self.backWheel = 11

        self.gyroS = 0
        self.arduino = 9

        # DIO
        self.elevatorLimitS = 0
        self.jawsLimitS = 1
        self.metaboxLimitS = 6

        # Soleniods
        self.jawsSol = {'out': 2, 'in': 3}
        self.pusherSol = {'out': 0, 'in': 1}
