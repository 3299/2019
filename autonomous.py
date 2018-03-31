'''
Runs the auto routine. Called once.
'''
import wpilib
from networktables import NetworkTables

class Autonomous(object):
    def __init__(self, drive, encoder, gyro, metabox, driverStation):
        self.drive = drive
        self.encoder = encoder
        self.gyro = gyro
        self.metabox = metabox
        self.driverStation = driverStation
        self.sd = NetworkTables.getTable('SmartDashboard')
        self.state = 0

        self.jawsCalibrated = False

    def run(self):
        ##############
        # Get target #
        ##############
        if (self.driverStation.getGameSpecificMessage() == ''):
            return False
        else:
            target = self.driverStation.getGameSpecificMessage()[0]

        #############
        # Calibrate #
        #############
        # Move elevator to top
        if (self.metabox.isCalibrated == False):
            self.metabox.calibrateSync()
        else:
            # Move jaws to bottom
            if (self.jawsCalibrated == False):
                if (self.metabox.calibrateJawsSync() == True):
                    self.jawsCalibrated = True
            else:
                self.metabox.jawsM.set(0)

        ########
        # Move #
        ########
        print(target)
        if ((target == 'L' and self.sd.getNumber('station', 1) == 1) or
             (target == 'R' and self.sd.getNumber('station', 1) == 3)):
            # go forward and dump cube
            if (self.state == 0):
                if (self.drive.toTime(6, 0.3)):
                    self.state += 1
            if (self.state == 1):
                if (self.metabox.openAuto(2)):
                    self.state += 1
        else:
            if (self.state == 0):
                if (self.drive.toTime(6, 0.3)):
                    self.state += 1
