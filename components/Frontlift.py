import helpers
import wpilib
import math
from inits import Component
from networktables import NetworkTables

class Frontlift(object):
    def __init__(self, frontLift, backLift, backWheel):
        self.frontLift = frontLift
        self.backLift = backLift
        self.backWheel = backWheel

    def run(self, frontLiftUp, frontLiftDown, backLiftUp, backLiftDown, backWheel):
        if (frontLiftUp):
            self.frontLift.set(1)
        elif (frontLiftDown):
            self.frontLift.set(-1)
        else:
            self.frontLift.set(0)
        if (backLiftUp):
            self.backLift.set(1)
        elif (backLiftDown):
            self.backLift.set(-1)
        else:
            self.backLift.set(0)
        if (backWheel):
            self.backWheel.set(0.5)
        else:
            self.backWheel.set(0)
    '''
    def frontLiftUp(self, liftValue):
        if (self.frontLift.get() == True or liftValue < 0):
            self.frontLift.set(liftValue)
        else:
            self.frontLift.set(0)
            return False
    def backLiftUp(self, liftValue):
        if (self.frontLift.get() == True or liftValue < 0):
            self.frontLift.set(liftValue)
        else:
            self.frontLift.set(0)
            return False
    def backWheel(self, liftValue):
        if (self.frontLift.get() == True or liftValue < 0):
            self.frontLift.set(liftValue)
        else:
            self.frontLift.set(0)
            return False
    def frontLiftDown(self, liftValue):
        if (self.frontLift.get() == True or liftValue < 0):
            self.frontLift.set(-liftValue)
        else:
            self.frontLift.set(0)
            return False
    def backLiftDown(self, liftValue):
        if (self.frontLift.get() == True or liftValue < 0):
            self.frontLift.set(-liftValue)
        else:
            self.frontLift.set(0)
            return False
    '''
