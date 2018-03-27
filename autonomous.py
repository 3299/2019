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

        self.state = 0

        # This code renders the followed path on the field in simulation (requires pyfrc 2018.2.0+)
        if wpilib.RobotBase.isSimulation():
            from pyfrc.sim import get_user_renderer
            renderer = get_user_renderer()
            if renderer:
                renderer.draw_pathfinder_trajectory(trajectory, color='#0000ff', offset=(-1,0))
                renderer.draw_pathfinder_trajectory(modifier.source, color='#00ff00', show_dt=1.0, dt_offset=0.0)
                renderer.draw_pathfinder_trajectory(trajectory, color='#0000ff', offset=(1,0))

    def run(self):
        '''
        velocity = self.follower.calculate(self.encoder.get())

        gyro_heading = -self.gyro.getAngle()
        desired_heading = pf.r2d(self.follower.getHeading())

        angleDifference = pf.boundHalfDegrees(desired_heading - gyro_heading)
        turn = 0.9 * (-1.0/80.0) * angleDifference

        self.drive.cartesian(0, velocity, turn)
        '''

        if (self.state == 0):
            if (self.drive.toDistance(6)):
                self.state += 1
        if (self.state == 1):
            if (self.drive.toAngle(-45)):
                self.state += 1
        if (self.state == 2):
            if (self.drive.toDistance(10)):
                self.state += 1
