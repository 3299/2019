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
        if (targetScale == True):
            if (targetSwitch == True):
                if (position == "Left"):
                    if (switch == "Left"):
                        if (scale == "Left"):
                            self.driveToPosition(5,0.2)
                            """
                            Magic cube drop
                            Also magic cube pickup
                            """
                            self.driveToPosition(5,0.2)
                            """
                            magic Scale drop
                            """
                        if (scale == "Right"):
                            self.driveToPosition(5,0.2)
                            """
                            Magic cube drop
                            Also magic cube pickup
                            """
                            self.driveToAngle(0.2,60)
                            self.driveToPosition(5,0.2)
                            """
                            magic Scale drop
                            """
                    if (switch == "Right"):
                        if (scale == "Left"):
                            self.driveToPosition(5,0.2)
                            self.driveToAngle(0.2,90)
                            self.driveToPosition(7,0.2)
                            """
                            Magic cube drop thingy
                            Magic cube pickup thingy
                            """
                            self.driveToAngle(0.2,-90)
                            self.driveToPosition(7,0.2)
                            self.driveToAngle(0.2,90)
                            self.driveToPosition(2,0.2)
                            """
                            Magic scale drop
                            """
                        if (scale == "Right"):
                            self.driveToPosition(5,0.2)
                            self.driveToAngle(0.2,90)
                            self.driveToPosition(7,0.2)
                            """
                            Magic cube drop thingy
                            Magic cube pickup thingy
                            """
                            self.driveToAngle(0.2,180)
                            self.driveToPosition(7,0.2)
                            self.driveToAngle(0.2,90)
                            self.driveToPosition(5,0.2)
                            """
                            Magic scale drop
                            """
                if (position == "Center"):
                    if (switch == "Left"):
                        if (scale == "Left"):
                            self.driveToPosition(2,0.2)
                            self.driveToAngle(0.2,-60)
                            self.driveToPosition(5,0.2)
                            """
                            magic cube drop thingy
                            """
                            self.driveToAngle(0.2,60)
                            self.driveToPosition(7,0.2)
                            """
                            scale drop thingy
                            """
                        if (scale == "Right"):
                            self.driveToPosition(2,0.2)
                            self.driveToAngle(0.2,60)
                            self.driveToPosition(5,0.2)
                            """
                            magic cube drop thingy
                            """
                            self.driveToAngle(0.2,-150)
                            self.driveToPosition(7,0.2)
                            self.driveToAngle(0.2,90)
                            """
                            scale drop thingy
                            """
                    if (switch == "Right"):
                        if (scale == "Left"):
                            self.driveToPosition(2,0.2)
                            self.driveToAngle(0.2,-60)
                            self.driveToPosition(5,0.2)
                            """
                            magic cube drop thingy
                            """
                            self.driveToAngle(0.2,60)
                            self.driveToPosition(2,0.2)
                            self.driveToAngle(0.2,-90)
                            self.driveToPosition(7,0.2)
                            """
                            scale drop thingy
                            """
                        if (scale == "Right"):
                            self.driveToPosition(2,0.2)
                            self.driveToAngle(0.2,60)
                            self.driveToPosition(5,0.2)
                            """
                            magic cube drop thingy
                            """
                            self.driveToAngle(0.2,-60)
                            self.driveToPosition(7,0.2)
                            """
                            scale drop thingy
                            """
                if (position == "Right"):
                    if (switch == "Left"):
                        if (scale == "Left"):
                            self.driveToPosition(5,0.2)
                            self.driveToAngle(0.2,-90)
                            self.driveToPosition(7,0.2)
                            """
                            Magic cube drop thingy
                            Magic cube pickup thingy
                            """
                            self.driveToAngle(0.2,-180)
                            self.driveToPosition(7,0.2)
                            self.driveToAngle(0.2,-90)
                            self.driveToPosition(5,0.2)
                            """
                            Magic scale drop
                            """
                        if (scale == "Right"):
                            self.driveToPosition(5,0.2)
                            self.driveToAngle(0.2,-90)
                            self.driveToPosition(7,0.2)
                            """
                            Magic cube drop thingy
                            Magic cube pickup thingy
                            """
                            self.driveToAngle(0.2,90)
                            self.driveToPosition(7,0.2)
                            self.driveToAngle(0.2,-90)
                            self.driveToPosition(2,0.2)
                            """
                            Magic scale drop
                            """
                    if (switch == "Right"):
                        if (scale == "Left"):
                            self.driveToPosition(5,0.2)
                            """
                            Magic cube drop
                            Also magic cube pickup
                            """
                            self.driveToAngle(0.2,-60)
                            self.driveToPosition(7,0.2)
                            """
                            magic Scale drop
                            """
                        if (scale == "Right"):
                            self.driveToPosition(5,0.2)
                            """
                            Magic cube drop
                            Also magic cube pickup
                            """
                            self.driveToPosition(5,0.2)
                            """
                            magic Scale drop
                            """
            else
                if (position == "Left"):
                    if (scale == "Left"):
                        self.driveToPosition(10,0.2)
                        """
                        Magic tall cube drop
                        """
                    if (scale == "Right"):
                        self.driveToPosition(10,0.2)
                        self.driveToAngle(0.2,90)
                        self.driveToPosition(5,0.2)
                        """
                        Magic tall cube drop
                        """
                if (position == "Center"):
                    if (scale == "Left"):
                        self.driveToPosition(1,0.2)
                        self.driveToAngle(0.2,-60)
                        self.driveToPosition(3,0.2)
                        self.driveToAngle(0.2,60)
                        self.driveToPosition(10,0.2)
                        """
                        Magic tall cube drop
                        """
                    if (scale == "Right"):
                        self.driveToPosition(1,0.2)
                        self.driveToAngle(0.2,60)
                        self.driveToPosition(3,0.2)
                        self.driveToAngle(0.2,-60)
                        self.driveToPosition(10,0.2)
                        """
                        Magic tall cube drop
                        """
                if (position == "Right"):
                    if (scale == "Left"):
                        self.driveToPosition(10,0.2)
                        self.driveToAngle(0.2,90)
                        self.driveToPosition(5,0.2)
                        """
                        Magic tall cube drop
                        """
                    if (scale == "Right"):
                        self.driveToPosition(10,0.2)
                        """
                        Magic tall cube drop
                        """
        else
            if (targetSwitch == True):
                if (position == "Left"):
                    if (switch == "Right"):
                        self.driveToPosition(1,0.2)
                        self.driveToAngle(0.2, 60)
                        self.driveToPosition(4,0.2)
                        """
                        Drop the cube
                        """
                    if (switch == "Left"):
                        self.driveToPosition(5,0.2)
                        """
                        Drop the cube
                        """
                if (position == "Center"):
                    if (switch == "Right"):
                        self.driveToPosition(1,0.2)
                        self.driveToAngle(0.2, 60)
                        self.driveToPosition(3,0.2)
                        """
                        Drop the cube
                        """
                    if (switch == "Left"):
                        self.driveToPosition(1,0.2)
                        self.driveToAngle(0.2, -60)
                        self.driveToPosition(3,0.2)
                        """
                        Drop the cube
                        """
                if (position == "Right"):
                    if (switch == "Right"):
                        self.driveToPosition(5,0.2)
                        """
                        Drop the cube
                        """
                    if (switch == "Left"):
                        self.driveToPosition(1,0.2)
                        self.driveToAngle(0.2, -60)
                        self.driveToPosition(4,0.2)
                        """
                        Drop the cube
                        """
            else
                self.driveToPosition(5, 0.2)
