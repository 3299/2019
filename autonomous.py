"""
Runs the auto routine. Called once.
"""
import time
import wpilib
import hal

class Autonomous(object):
    def __init__(self, drive, driverStation):
        self.drive = drive
        self.driverStation = driverStation
        self.timer = wpilib.Timer()

    def run(self):
        if (hal.isSimulation() == False):
            print(self.driverStation.getGameSpecificMessage())

        self.drive.straight(5, -0.2)
