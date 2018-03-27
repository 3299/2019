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
        self.driveTrain = [wpilib.Spark(Mapping.frontLeftM),
                           wpilib.Spark(Mapping.frontRightM),
                           wpilib.Spark(Mapping.backLeftM),
                           wpilib.Spark(Mapping.backRightM)]

        self.driveTrain[0].setInverted(True)
        self.driveTrain[2].setInverted(True)

        # Init motors
        self.elevatorM = wpilib.Talon(Mapping.elevatorM)
        self.elevatorM.setInverted(True)
        self.winchM = wpilib.Talon(Mapping.winchM)
        self.intakeM = wpilib.Talon(Mapping.intakeM)
        self.jawsM = wpilib.Spark(Mapping.jawsM)

        # Soleniods
        self.jawsSol = wpilib.DoubleSolenoid(Mapping.jawsSol['out'], Mapping.jawsSol['in'])

        # Init sensors
        self.gyroS = wpilib.AnalogGyro(Mapping.gyroS)
        self.elevatorLimitS = wpilib.DigitalInput(Mapping.elevatorLimitS)
        self.jawsLimitS = wpilib.DigitalInput(Mapping.jawsLimitS)

        # Encoders
        self.elevatorEncoderS = wpilib.Encoder(7, 8, True)
        self.elevatorEncoderS.setDistancePerPulse(0.08078)

        self.driveYEncoderS = wpilib.Encoder(2, 3)
        self.driveYEncoderS.setDistancePerPulse(0.015708)

        self.jawsEncoderS = wpilib.Encoder(5, 6)
        self.jawsEncoderS.setDistancePerPulse(0.1769)
