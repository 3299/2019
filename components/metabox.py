"""
Controls intake wheels, the elevator, and the metabox.
"""

import wpilib
from networktables import NetworkTables

class MetaBox(object):
    def __init__(self, encoderS, limitS, elevatorM):
        self.encoder = encoderS
        self.limit = limitS
        self.elevatorM = elevatorM
        self.elevatorTravel = 26.25
        self.floorOffset = 11.25

        self.pid = wpilib.PIDController(1, 0.2, 0.2, lambda: self.getEncoder(), self.elevatorM)
        self.pid.setAbsoluteTolerance(0.1)

        self.sd = NetworkTables.getTable('SmartDashboard')
        self.sd.putNumber('p', 0.8)
        self.sd.putNumber('i', 0.2)
        self.sd.putNumber('d', 0.5)

    def getEncoder(self):
        return self.encoder.getDistance() + self.elevatorTravel

    def set(self, height, continuous=False):
        self.pid.setP(self.sd.getNumber('p', 1))
        self.pid.setI(self.sd.getNumber('i', 0.2))
        self.pid.setD(self.sd.getNumber('d', 0.2))

        if (height - self.floorOffset < 0 or height > self.floorOffset + self.elevatorTravel):
            return False
        else:
            self.pid.setContinuous(continuous)
            self.pid.enable()
            self.pid.setSetpoint(height - self.floorOffset)

        if (self.pid.onTarget() and continuous == False):
            self.pid.disable()

    def calibrateAsync(self):
        if (self.limit.get() == False):
            self.elevatorM.set(0.4)
            return False
        else:
            self.elevatorM.set(0)
            self.encoder.reset()
            return True
