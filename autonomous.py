'''
Runs the auto routine. Called once.
'''
import wpilib

class Autonomous(object):
    def __init__(self, drive, encoder, gyro, metabox, driverStation):
        self.drive = drive
        self.encoder = encoder
        self.gyro = gyro
        self.metabox = metabox
        self.driverStation = driverStation

        self.state = 0

    def run(self):
        """
        self.driverStation.getGameSpecificMessage()
        if(self.driveStation.getGameSpecificMessage() == "")
            return False
        else
        target == self.driveStation.getGameSpecificMessage()
        # Square driving example
        """
        '''
        if (self.state == 0):
            if (self.drive.toDistance(4)):
                self.state += 1
        if (self.state == 1):
            if (self.drive.toAngle(90)):
                self.state += 1

        if (self.state == 2):
            if (self.drive.toDistance(4)):
                self.state += 1
        if (self.state == 3):
            if (self.drive.toAngle(180)):
                self.state += 1

        if (self.state == 4):
            if (self.drive.toDistance(4)):
                self.state += 1
        if (self.state == 5):
            if (self.drive.toAngle(270)):
                self.state += 1

        if (self.state == 6):
            if (self.drive.toDistance(4)):
                self.state += 1
        if (self.state == 7):
            if (self.drive.toAngle(360)):
                self.state += 1
        '''

        # Example for jaws
        # if (self.state == 0):
        #   if (self.metabox.runOutAuto(2)):
        #     self.state += 1

        if (self.state == 0):
            if (self.drive.toDistance(8.5)):
                self.state += 1
        if (self.state == 1):
            if (self.metabox.runOutAuto(2)):
                self.state += 1

        """
        if (self.state == 1):
            if (self.drive.toAngle(45)):
                self.state += 1
        if (self.state == 2):
            if (self.drive.toDistance(10)):
                self.state += 1
        if (self.state == 3):
            if (self.drive.toAngle(0)):
                self.state += 1
        if (self.state == 4):
            if (self.drive.toDistance(6)):
                self.state += 1
        if (self.state == 5):
            if (self.drive.toAngle(-90)):
                self.state += 1
        if (self.state == 6):
            if (self.drive.toDistance(10)):
                self.state += 1
        if (self.state == 7):
            if (self.drive.toAngle(-180)):
                self.state += 1
        """
