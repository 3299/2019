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

        self.sd.putNumber('station', 1)

        self.elevatorCalibrated = False

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
        if (self.metabox.calibrateJawsSync()):
            pass

        if (self.elevatorCalibrated == False):
            if (self.metabox.calibrateAsync()):
                self.elevatorCalibrated = True
        else:
            self.metabox.goToHeight(15)

        ########
        # Move #
        ########
        if ((target == 'L' and self.sd.getNumber('station', 1) == 1) or
             target == 'R' and self.sd.getNumber('station', 1) == 3):
            # go forward and dump cube
            if (self.state == 0):
                if (self.drive.toDistance(8.5)):
                    self.state += 1
            if (self.state == 1):
                if (self.metabox.runOutAuto(2)):
                    self.state += 1
        elif (self.sd.getNumber('station', 1) == 2):
            if (self.state == 0):
                if (self.drive.toDistance(8.5)):
                    self.state += 1

        '''
        # Example for jaws
        # if (self.state == 0):
        #   if (self.metabox.runOutAuto(2)):
        #     self.state += 1
        if(self.target == "right"):
            if (self.state == 0):
                if (self.drive.toDistance(8.5)):
                    self.state += 1
            if (self.state == 1):
                if (self.metabox.runOutAuto(2)):
                    self.state += 1
        if(self.target == "left"):
            print(self.state)
            if (self.state == 0):
                if (self.drive.toDistance(14)):
                    self.state += 1

            if (self.state == 1):
                if (self.drive.toAngle(-90)):
                    self.state += 1

            if (self.state == 2):
                if (self.drive.toDistance(14)):
                    self.state += 1

            if (self.state == 3):
                if (self.drive.toAngle(180)):
                    self.state += 1
            if (self.state == 4):
                if (self.metabox.runOutAuto(2)):
                    self.state += 1
        if(self.target == "test"):
            if (self.state == 0):
                if (self.drive.toAngle(90)):
                    self.state += 1
        '''
