"""
Controls intake wheels, the elevator, and the metabox.
"""

import wpilib
from networktables import NetworkTables

class MetaBox(object):
    def __init__(self, encoderS, limitS, elevatorM, intakeM):
        self.encoder = encoderS
        self.limit = limitS
        self.elevatorM = elevatorM
        self.intakeM = intakeM
        self.elevatorTravel = 26.25
        self.floorOffset = 11.25
        self.sd = NetworkTables.getTable('SmartDashboard')

        self.pidDefault = {'p': 0.8, 'i': 0.2, 'd': 0.5}
        self.pid = wpilib.PIDController(self.pidDefault['p'], self.pidDefault['i'], self.pidDefault['d'], lambda: self.getEncoder(), self.set)
        self.pid.setAbsoluteTolerance(0.1)
        self.sd.putNumber('elevatorP', self.pidDefault['p'])
        self.sd.putNumber('elevatorI', self.pidDefault['i'])
        self.sd.putNumber('elevatorD', self.pidDefault['d'])

    def run(self, heightRate, runIn, runOut):
        self.set(heightRate)

        if (runIn):
            self.intakeM.set(1)
        elif (runOut):
            self.intakeM.set(-1)
        else:
            self.intakeM.set(0)

    ''' Functions that want to move the elevator should call this instead of elevatorM.set() directly. '''
    def set(self, value):
        if ((self.limit.get() == False or (self.limit.get() == True and value < 0)) and self.getEncoder() > 0):
            self.elevatorM.set(value)
        else:
            self.elevatorM.set(0)
            return False

    def getEncoder(self):
        return self.encoder.getDistance() + self.elevatorTravel

    def goToHeight(self, height, continuous=False):
        self.pid.setP(self.sd.getNumber('elevatorP', self.pidDefault['p']))
        self.pid.setI(self.sd.getNumber('elevatorI', self.pidDefault['i']))
        self.pid.setD(self.sd.getNumber('elevatorD', self.pidDefault['d']))

        if (height - self.floorOffset < 0 or height > self.floorOffset + self.elevatorTravel):
            return False
        elif (self.limit.get() == True):
            self.pid.disable()
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
