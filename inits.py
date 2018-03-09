"""
Inits wpilib objects
"""

import wpilib
from map import Map

class Component(object):
    def __init__(self):
        # Mapping object stores port numbers for all connected motors, sensors, and joysticks. See map.py.
        Mapping = Map()

        # Init drivetrain
        self.driveTrain = {'frontLeft': wpilib.Spark(Mapping.frontLeftM), 'backLeft': wpilib.Spark(Mapping.backLeftM), 'frontRight': wpilib.Spark(Mapping.frontRightM), 'backRight': wpilib.Spark(Mapping.backRightM)}

        # Init motors
        self.elevatorM = wpilib.Spark(Mapping.elevatorM)

        # Init sensors
        self.gyroS = wpilib.AnalogGyro(Mapping.gyroS)
        self.elevatorLimitS = wpilib.DigitalInput(0)

        # Encoders
        self.elevatorEncoderS = wpilib.Encoder(7, 8)
        self.elevatorEncoderS.setDistancePerPulse(0.064)

        self.driveYEncoderS = wpilib.Encoder(2, 3)
        self.driveYEncoderS.setDistancePerPulse(0.06)
