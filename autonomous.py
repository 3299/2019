"""
Runs the auto routine. Called once.
"""
import time
import wpilib
import hal
class Autonomous(object):
    def __init__(self, drive):
        self.drive = drive
        self.DriverStation = wpilib.DriverStation.getInstance()

    def run(self):
        print('Autonomous has run')
        if (hal.isSimulation == False):
            print(self.DriverStation.getGameSpecificMessage())

        #self.drive.straight(2, 0.3)
        #self.drive.driveToAngle(0.3, 90, False)
