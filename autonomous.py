'''
Runs the auto routine. Called once.
'''
import time
import wpilib
import hal

class Autonomous(object):
    def __init__(self, drive, driverStation):
        self.drive = drive
        self.driverStation = driverStation
        self.timer = wpilib.Timer()

    def run(self):
        """
        targetScale = True
        targetSwitch = True
        position = 'Left'
        switch = 'Left'
        scale = 'Left'

        # Example:
        @state(first=True)
        def driveToAngle(self):
            self.drive.driveToAngle(60)

        if (self.driveToAngle(60) == True)

        """


        """
        if (targetScale == True):
            if (targetSwitch == True):
                if (position == 'Left'):
                    if (switch == 'Left'):
                        if (scale == 'Left'):
                            self.drive.driveToPosition(5)
                            '''
                            Magic cube drop
                            Also magic cube pickup
                            '''
                            self.drive.driveToPosition(5)
                            '''
                            magic Scale drop
                            '''
                        if (scale == 'Right'):
                            self.drive.driveToPosition(5)
                            '''
                            Magic cube drop
                            Also magic cube pickup
                            '''
                            self.driveToAngle(0.2,60)
                            self.drive.driveToPosition(5)
                            '''
                            magic Scale drop
                            '''
                    if (switch == 'Right'):
                        if (scale == 'Left'):
                            self.drive.driveToPosition(5)
                            self.driveToAngle(0.2,90)
                            self.drive.driveToPosition(7)
                            '''
                            Magic cube drop thingy
                            Magic cube pickup thingy
                            '''
                            self.driveToAngle(0.2,-90)
                            self.drive.driveToPosition(7)
                            self.driveToAngle(0.2,90)
                            self.drive.driveToPosition(2)
                            '''
                            Magic scale drop
                            '''
                        if (scale == 'Right'):
                            self.drive.driveToPosition(5)
                            self.driveToAngle(0.2,90)
                            self.drive.driveToPosition(7)
                            '''
                            Magic cube drop thingy
                            Magic cube pickup thingy
                            '''
                            self.driveToAngle(0.2,180)
                            self.drive.driveToPosition(7)
                            self.driveToAngle(0.2,90)
                            self.drive.driveToPosition(5)
                            '''
                            Magic scale drop
                            '''
                if (position == 'Center'):
                    if (switch == 'Left'):
                        if (scale == 'Left'):
                            self.drive.driveToPosition(2)
                            self.driveToAngle(0.2,-60)
                            self.drive.driveToPosition(5)
                            '''
                            magic cube drop thingy
                            '''
                            self.driveToAngle(0.2,60)
                            self.drive.driveToPosition(7)
                            '''
                            scale drop thingy
                            '''
                        if (scale == 'Right'):
                            self.drive.driveToPosition(2)
                            self.driveToAngle(0.2,60)
                            self.drive.driveToPosition(5)
                            '''
                            magic cube drop thingy
                            '''
                            self.driveToAngle(0.2,-150)
                            self.drive.driveToPosition(7)
                            self.driveToAngle(0.2,90)
                            '''
                            scale drop thingy
                            '''
                    if (switch == 'Right'):
                        if (scale == 'Left'):
                            self.drive.driveToPosition(2)
                            self.driveToAngle(0.2,-60)
                            self.drive.driveToPosition(5)
                            '''
                            magic cube drop thingy
                            '''
                            self.driveToAngle(0.2,60)
                            self.drive.driveToPosition(2)
                            self.driveToAngle(0.2,-90)
                            self.drive.driveToPosition(7)
                            '''
                            scale drop thingy
                            '''
                        if (scale == 'Right'):
                            self.drive.driveToPosition(2)
                            self.driveToAngle(0.2,60)
                            self.drive.driveToPosition(5)
                            '''
                            magic cube drop thingy
                            '''
                            self.driveToAngle(0.2,-60)
                            self.drive.driveToPosition(7)
                            '''
                            scale drop thingy
                            '''
                if (position == 'Right'):
                    if (switch == 'Left'):
                        if (scale == 'Left'):
                            self.drive.driveToPosition(5)
                            self.driveToAngle(0.2,-90)
                            self.drive.driveToPosition(7)
                            '''
                            Magic cube drop thingy
                            Magic cube pickup thingy
                            '''
                            self.driveToAngle(0.2,-180)
                            self.drive.driveToPosition(7)
                            self.driveToAngle(0.2,-90)
                            self.drive.driveToPosition(5)
                            '''
                            Magic scale drop
                            '''
                        if (scale == 'Right'):
                            self.drive.driveToPosition(5)
                            self.driveToAngle(0.2,-90)
                            self.drive.driveToPosition(7)
                            '''
                            Magic cube drop thingy
                            Magic cube pickup thingy
                            '''
                            self.driveToAngle(0.2,90)
                            self.drive.driveToPosition(7)
                            self.driveToAngle(0.2,-90)
                            self.drive.driveToPosition(2)
                            '''
                            Magic scale drop
                            '''
                    if (switch == 'Right'):
                        if (scale == 'Left'):
                            self.drive.driveToPosition(5)
                            '''
                            Magic cube drop
                            Also magic cube pickup
                            '''
                            self.driveToAngle(0.2,-60)
                            self.drive.driveToPosition(7)
                            '''
                            magic Scale drop
                            '''
                        if (scale == 'Right'):
                            self.drive.driveToPosition(5)
                            '''
                            Magic cube drop
                            Also magic cube pickup
                            '''
                            self.drive.driveToPosition(5)
                            '''
                            magic Scale drop
                            '''
            else:
                if (position == 'Left'):
                    if (scale == 'Left'):
                        self.drive.driveToPosition(10)
                        '''
                        Magic tall cube drop
                        '''
                    if (scale == 'Right'):
                        self.drive.driveToPosition(10)
                        self.driveToAngle(0.2,90)
                        self.drive.driveToPosition(5)
                        '''
                        Magic tall cube drop
                        '''
                if (position == 'Center'):
                    if (scale == 'Left'):
                        self.drive.driveToPosition(1)
                        self.driveToAngle(0.2,-60)
                        self.drive.driveToPosition(3)
                        self.driveToAngle(0.2,60)
                        self.drive.driveToPosition(10)
                        '''
                        Magic tall cube drop
                        '''
                    if (scale == 'Right'):
                        self.drive.driveToPosition(1)
                        self.driveToAngle(0.2,60)
                        self.drive.driveToPosition(3)
                        self.driveToAngle(0.2,-60)
                        self.drive.driveToPosition(10)
                        '''
                        Magic tall cube drop
                        '''
                if (position == 'Right'):
                    if (scale == 'Left'):
                        self.drive.driveToPosition(10)
                        self.driveToAngle(0.2,90)
                        self.drive.driveToPosition(5)
                        '''
                        Magic tall cube drop
                        '''
                    if (scale == 'Right'):
                        self.drive.driveToPosition(10)
                        '''
                        Magic tall cube drop
                        '''
        else:
            if (targetSwitch == True):
                if (position == 'Left'):
                    if (switch == 'Right'):
                        self.drive.driveToPosition(1)
                        self.driveToAngle(0.2, 60)
                        self.drive.driveToPosition(4)
                        '''
                        Drop the cube
                        '''
                    if (switch == 'Left'):
                        self.drive.driveToPosition(5)
                        '''
                        Drop the cube
                        '''
                if (position == 'Center'):
                    if (switch == 'Right'):
                        self.drive.driveToPosition(1)
                        self.driveToAngle(0.2, 60)
                        self.drive.driveToPosition(3)
                        '''
                        Drop the cube
                        '''
                    if (switch == 'Left'):
                        self.drive.driveToPosition(1)
                        self.driveToAngle(0.2, -60)
                        self.drive.driveToPosition(3)
                        '''
                        Drop the cube
                        '''
                if (position == 'Right'):
                    if (switch == 'Right'):
                        self.drive.driveToPosition(5)
                        '''
                        Drop the cube
                        '''
                    if (switch == 'Left'):
                        self.drive.driveToPosition(1)
                        self.driveToAngle(0.2, -60)
                        self.drive.driveToPosition(4)
                        '''
                        Drop the cube
                        '''
            else:
                self.drive.driveToPosition(5)
            """
