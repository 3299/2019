import helpers
import wpilib
import math
from networktables import NetworkTables

class Frontlift(object):
    def __init__(self):
        self.frontLift = frontLift
        self.backLift = backLift
        self.backWheel = backWheel

    def run(self):
        if (self.leftJ.getRawButton(6) or self.leftJ.getRawButton(7)
            if (self.leftJ.getRawButton(6))
                self.frontLift.set(0.5)
            if (self.leftJ.getRawButton(7))
                self.frontLift.set(-0.5)
        else:
            self.frontLift.set(0)

        if (self.leftJ.getRawButton(10) or self.leftJ.getRawButton(11)
            if (self.leftJ.getRawButton(10))
                self.backLift.set(0.5)
            if (self.leftJ.getRawButton(11))
                self.backLift.set(-0.5)
        else:
            self.backLift.set(0)

        if (self.leftJ.getRawButton(8))
            self.backWheel.set(1)
        else:
            self.backWheel.set(0)
