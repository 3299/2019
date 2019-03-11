"""
Provides various helper functions.
"""

import wpilib
import math

class timeToggle(object):
    def __init__(self):
        self.period = 0
        self.timer = wpilib.Timer()
        self.running = False

    def start(self, reset, period):
        if (self.running == False and reset):
            self.period = period
            self.timer.start()
            self.running = True

    def get(self):

        if (not self.timer.hasPeriodPassed(self.period) and self.running == True): # will be true if timer still running
            return True
        else:
            self.timer.stop()
            self.running = False
            return False

def remap( x, oMin, oMax, nMin, nMax ): # thanks stackoverflow.com/a/15537393
    #range check
    if oMin == oMax:
        print("Warning: Zero input range")
        return None

    if nMin == nMax:
        print("Warning: Zero output range")
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result

'''
Given a value and power, this raises the value
to the power, then negates it if the value was
originally negative.
'''
def raiseKeepSign(value, power):

    newValue = value ** power

    if (value < 0 and newValue > 0):
        return newValue * -1
    else:
        return value ** power

'''
Given a Cartesian x,y position, this 'snaps'
it to the nearest angle, in degrees (the
number of snappable angles is determined by
`divisions`). Intended to be used with joystick
values.
'''

def snap(divisions, x, y):

    if (x == 0):
        return 0

    result = round(math.atan2(y, x) / (2 * math.pi / divisions) + divisions, 0) % divisions

    return result * (360 / divisions)

'''
Adds deadband to a joystick.
'''

def deadband(value, ignoreRange):
    if (abs(value) < ignoreRange and abs(value) > -ignoreRange):
        return 0
    else:
        return value
