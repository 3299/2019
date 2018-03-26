'''
Runs the auto routine. Called once.
'''
import time
import wpilib
import hal
from paths import Paths
import pathfinder as pf

class Autonomous(object):
    def __init__(self, drive, encoder, gyro, driverStation):
        self.drive = drive
        self.encoder = encoder
        self.gyro = gyro
        self.driverStation = driverStation
        self.timer = wpilib.Timer()
        self.paths = Paths()

        mode = 'left'

        modifier = pf.modifiers.TankModifier(self.paths.trajectories[mode]).modify(2.667)

        trajectory = modifier.getLeftTrajectory()

        follower = pf.followers.EncoderFollower(trajectory)
        follower.configureEncoder(self.encoder.get(), 100, 0.5)
        follower.configurePIDVA(1.0, 0.0, 0.0, 1 / 5, 0)

        self.follower = follower

        # This code renders the followed path on the field in simulation (requires pyfrc 2018.2.0+)
        if wpilib.RobotBase.isSimulation():
            from pyfrc.sim import get_user_renderer
            renderer = get_user_renderer()
            if renderer:
                renderer.draw_pathfinder_trajectory(trajectory, color='#0000ff', offset=(-1,0))
                renderer.draw_pathfinder_trajectory(modifier.source, color='#00ff00', show_dt=1.0, dt_offset=0.0)
                renderer.draw_pathfinder_trajectory(trajectory, color='#0000ff', offset=(1,0))

    def run(self):
        velocity = self.follower.calculate(self.encoder.get())

        gyro_heading = -self.gyro.getAngle()
        desired_heading = pf.r2d(self.follower.getHeading())

        angleDifference = pf.boundHalfDegrees(desired_heading - gyro_heading)
        turn = 0.9 * (-1.0/80.0) * angleDifference

        self.drive.cartesian(0, velocity, turn)
        """
        targetScale = True
        targetSwitch = True
        position = 'Left'
        switch = 'Left'
        scale = 'Left'

        # Example:
                state = 0
                if (state == 0):
                    if (self.drive.toDistance(6)):
                        state += 1
                if (state == 1):
                    if (self.drive.toAngle(-45)):
                        state += 1
                if (state == 2):
                    if (self.drive.toDistance(10)):
                        state += 1
                print(state)

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
