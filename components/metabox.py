"""
Controls intake wheels, the elevator, and the metabox.
"""

import wpilib
import helpers
from networktables import NetworkTables

class MetaBox(object):
    def __init__(self, elevatorEncoder, jawsEncoder, elevatorLimitS, jawsLimitS, jawsM, elevatorM, intakeM, jawsSol):
        self.elevatorEncoder = elevatorEncoder
        self.jawsEncoder = jawsEncoder
        self.elevatorLimit = elevatorLimitS
        self.jawsLimitS = jawsLimitS
        self.jawsM = jawsM
        self.elevatorM = elevatorM
        self.intakeM = intakeM
        self.jawsSol = jawsSol

        self.elevatorTravel = 26.25
        self.isCalibrated = False

        self.sd = NetworkTables.getTable('SmartDashboard')

        self.pidDefault = {'p': 0.8, 'i': 0.2, 'd': 0.5}
        self.pid = wpilib.PIDController(self.pidDefault['p'], self.pidDefault['i'], self.pidDefault['d'], lambda: self.getEncoder(), self.setElevator)
        self.pid.setAbsoluteTolerance(0.1)
        self.sd.putNumber('elevatorP', self.pidDefault['p'])
        self.sd.putNumber('elevatorI', self.pidDefault['i'])
        self.sd.putNumber('elevatorD', self.pidDefault['d'])

        self.timer = wpilib.Timer()
        self.autoActionStarted = False

    def run(self, heightRate, runIn, open, runOut, bottom, angle, timed=False):
        '''
        Intended to be called with a periodic loop
        and with button toggles.
        '''

        if (runIn and self.jawsLimitS.get() == False):
            self.intakeM.set(1)
        elif (runOut):
            self.intakeM.set(-1)
        else:
            self.intakeM.set(0)

        if (open):
            self.jawsSol.set(self.jawsSol.Value.kForward)
        else:
            self.jawsSol.set(self.jawsSol.Value.kReverse)

        if (bottom):
            self.goToHeight(0)
        else:
            self.setElevator(heightRate)

        self.jawsM.set(helpers.deadband(angle, 0.1))

    def runOutAuto(self, time):
        if (self.autoActionStarted == False):
            self.timer.start()
            self.autoActionStarted = True

        if (self.timer.hasPeriodPassed(time)):
            self.autoActionStarted = False
            self.intakeM.set(0)
            return True
        else:
            self.intakeM.set(-1)
            return False


    ''' Functions that want to move the elevator should call this instead of elevatorM.set() directly. '''
    def setElevator(self, value):
        if ((self.elevatorLimit.get() == False or (self.elevatorLimit.get() == True and value < 0)) and self.getEncoder() > 0):
            self.elevatorM.set(value)
        else:
            self.elevatorM.set(0)
            return False

    ''' Functions that want to move the jaws should call this instead of jawsM.set() directly. '''
    def setJaws(self, value):
        if (self.jawsEncoder.getDistance() >= 0):
            self.jawsM.set(value)
        else:
            self.jawsM.set(0)
            return False

    def getEncoder(self):
        return self.elevatorEncoder.getDistance() + self.elevatorTravel

    def goToHeight(self, height, continuous=False):
        self.pid.setP(self.sd.getNumber('elevatorP', self.pidDefault['p']))
        self.pid.setI(self.sd.getNumber('elevatorI', self.pidDefault['i']))
        self.pid.setD(self.sd.getNumber('elevatorD', self.pidDefault['d']))

        if (self.isCalibrated != True):
            return False

        if (height < 0 or height > self.elevatorTravel):
            return False
        elif (self.elevatorLimit.get() == True):
            self.pid.disable()
        else:
            self.pid.setContinuous(continuous)
            self.pid.enable()
            self.pid.setSetpoint(height)

        if (self.pid.onTarget() and continuous == False):
            self.pid.disable()

    def calibrateAsync(self):
        if (self.elevatorLimit.get() == False):
            self.elevatorM.set(0.4)
            return False
        else:
            self.isCalibrated = True
            self.elevatorM.set(0)
            self.elevatorEncoder.reset()
            return True
