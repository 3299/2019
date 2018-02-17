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
        self.elevatorS = wpilib.Encoder(7, 8)
        self.elevatorS.setDistancePerPulse(0.064)
