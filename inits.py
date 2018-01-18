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
        self.driveTrain['frontLeft'].setInverted(True)
        self.driveTrain['backLeft'].setInverted(True)

        # Init sensors
        self.gyroS = wpilib.ADXRS450_Gyro(Mapping.gyroS)


        # Init I2C for communication with Arduino
        self.arduino = wpilib.I2C(wpilib.I2C.Port.kOnboard, 4)
