"""
Wrapper for wpilib.PowerDistributionPanel().
"""
import wpilib

class Power(object):
    def __init__(self):
        self.board = wpilib.PowerDistributionPanel()

    def getAverageCurrent(self, slots):
        totalCurrent = 0

        for slot in slots:
            totalCurrent += self.board.getCurrent(slot)

        return totalCurrent / len(slots)
