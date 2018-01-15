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

        self.climbM      = 7
        self.collectorM  = 5
        self.shooterM    = 9
        self.hopperM     = 8
        self.groundGearM = 4

        # Soleniods
        self.gearSol     = {'in': 3, 'out': 4}
        self.groundGearSol = {'in': 2, 'out': 0}

        # Sensors have suffix 'S'. Gyro uses SPI, everything else uses the DIO.
        self.gyroS       = 0
        self.allienceS   = 0
        self.shooterS    = 1
        self.hopperS     = 2

        # Relays
        self.bumpPopR    = 0
        self.greenLEDR   = 1
