"""
Controls intake wheels, the elevator, and the metabox.
"""

import wpilib
import helpers
from networktables import NetworkTables

class MetaBox(object):
    def __init__(self, encoderS, limitS, elevatorM, intakeM, jawsSol, pusherSol):
        self.encoder = encoderS
        self.limit = limitS
        self.elevatorM = elevatorM
        self.intakeM = intakeM
        self.jawsSol = jawsSol
        self.pusherSol = pusherSol
        self.elevatorTravel = 26.25
        self.floorOffset = 11.25
        self.sd = NetworkTables.getTable('SmartDashboard')

        self.pidDefault = {'p': 0.8, 'i': 0.2, 'd': 0.5}
        self.pid = wpilib.PIDController(self.pidDefault['p'], self.pidDefault['i'], self.pidDefault['d'], lambda: self.getEncoder(), self.set)
        self.pid.setAbsoluteTolerance(0.1)
        self.sd.putNumber('elevatorP', self.pidDefault['p'])
        self.sd.putNumber('elevatorI', self.pidDefault['i'])
        self.sd.putNumber('elevatorD', self.pidDefault['d'])

        # Toggles for mechanisms
        self.runInT = helpers.timeToggle()
        self.pushOut1T = helpers.timeToggle()
        self.pushOut2T = helpers.timeToggle()
        self.pushOut3T = helpers.timeToggle()

    def run(self, heightRate, runIn, pushOut1, pushOut2, pushOut3):
        '''
        Intended to be called with a periodic loop
        and with button toggles.
        '''
        # set elevator
        self.set(heightRate)

        if (runIn or self.runInT.get()):
            # intake cube
            self.jawsSol.set(self.jawsSol.Value.kForward)
            self.intakeM.set(1)

            self.runInT.start(runIn, 2)

        elif (pushOut1 or self.pushOut1T.get()):
            # open jaws
            self.jawsSol.set(self.jawsSol.Value.kForward)

            self.pushOut1T.start(pushOut1, 2)

        elif (pushOut2 or self.pushOut2T.get()):
            # run wheels
            self.running = 'pushOut2'
            self.intakeM.set(-1)

            self.pushOut2T.start(pushOut2, 2)

        elif (pushOut3 or self.pushOut3T.get()):
            # use pusher
            self.pusherSol.set(self.pusherSol.Value.kForward)

            #self.pushOut3T.(pushOut3, 3)

            self.pusherT = helpers.timeToggle()
            self.wheelsT = helpers.timeToggle()
            self.jawsT = helpers.timeToggle()

            if (self.pusherT.get()):
                # run wheels
                self.intakeM.set(-1)
                wheelsTimer = wpilib.Timer()

                if (self.wheelsT.get()):
                    # open jaws
                    self.jawsSol.set(self.jawsSol.Value.kForward)
                    jawsTimer = wpilib.timer()

                    if (self.jawsT.get()):
                        self.running = ''

        else:
            # close jaws and stop intake
            self.jawsSol.set(self.jawsSol.Value.kReverse)
            self.pusherSol.set(self.pusherSol.Value.kReverse)
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
