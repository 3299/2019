"""
Main logic code
"""
import wpilib

from inits import Component
import helpers
import cameras

from components.chassis import Chassis

from autonomous import Autonomous
from components.lights import Lights
from components.metabox import MetaBox
#from components.winch import Winch
from components.pdb import Power
from components.Frontlift import Frontlift
from networktables import NetworkTables


class Randy(wpilib.TimedRobot):
    def robotInit(self):

        self.C = Component() # Components inits all connected motors, sensors, and joysticks. See inits.py.

        # Setup subsystems
        self.driverStation = wpilib.DriverStation.getInstance()
        self.drive = Chassis(self.C.driveTrain, self.C.gyroS, self.C.driveYEncoderS)
        self.lights = Lights()
        self.metabox = MetaBox(self.C.elevatorEncoderS,
                               self.C.elevatorLimitS,
                               self.C.jawsLimitS,
                               self.C.metaboxLimitS,
                               self.C.jawsM,
                               self.C.elevatorM,
                               self.C.intakeM,
                               self.C.jawsSol)
        #self.winch = Winch(self.C.winchM)
        self.power = Power()

        # Joysticks
        self.joystick = wpilib.XboxController(0)
        self.leftJ = wpilib.Joystick(1)
        self.Frontlift = Frontlift(self.C.frontLift, self.C.backLift, self.C.backWheel)
        # default to rainbow effect
        self.lights.run({'effect': 'rainbow'})

        self.sd = NetworkTables.getTable('SmartDashboard')
        self.sd.putNumber('station', 2)
        #wpilib.CameraServer.launch()
        print("init works")
        #cameras.main()
        #print("USB1 status is" usb1.isConnected())
    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        '''Components'''
        # Rumble
        averageDriveCurrent = self.power.getAverageCurrent([0, 1, 14, 15])
        if (averageDriveCurrent > 8):
            self.joystick.setRumble(0, 1)
        else:
            self.joystick.setRumble(0, 0)
        #print(self.metabox.getEncoder())

        '''
        TODO: calibrate sparks
        '''

        # Drive
        self.drive.run(self.joystick.getRawAxis(0), self.joystick.getRawAxis(1), self.joystick.getRawAxis(4))

        # MetaBox
        self.metabox.run(self.leftJ.getY(),          # elevator rate of change
                         self.leftJ.getRawButton(2), # run intake wheels in
                         self.leftJ.getRawButton(1), # open jaws
                         self.leftJ.getRawButton(3), # run intake wheels out
                         self.leftJ.getRawButton(4), # go to bottom
                         self.leftJ.getRawAxis(2),   # set angle of jaws
                         self.leftJ.getRawButton(8)) # calibrate elevator

        self.Frontlift.run(self.leftJ.getRawButton(6),
                           self.leftJ.getRawButton(7),
                           self.leftJ.getRawButton(11),
                           self.leftJ.getRawButton(10),
                           self.leftJ.getRawButton(8))
        # Lights
        self.lights.setColor(self.driverStation.getAlliance())

        if (self.driverStation.getMatchTime() < 30 and self.driverStation.getMatchTime() != -1):
            self.lights.run({'effect': 'flash', 'fade': True, 'speed': 200})
        elif (helpers.deadband(self.leftJ.getY(), 0.1) != 0):
            self.lights.run({'effect': 'stagger'})
        elif (self.leftJ.getRawButton(1) or self.leftJ.getRawButton(2)):
            self.lights.run({'effect': 'flash', 'fade': False, 'speed': 20})
        else:
            self.lights.run({'effect': 'rainbow'})

    def teleopInit(self):
        """This function is run once each time the robot enters teleop mode."""
        # reset gyro
        self.C.gyroS.reset()
        # reset encoder
        self.C.driveYEncoderS.reset()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        #self.lights.run({'effect': 'flash', 'fade': True, 'speed': 400})
        # reset gyro
        self.C.gyroS.reset()
        # reset encoder
        self.C.driveYEncoderS.reset()

        # Init autonomous
        self.autonomousRoutine = Autonomous(self.drive, self.C.driveYEncoderS, self.C.gyroS, self.metabox, self.driverStation)

        # reset state
        self.autonomousRoutine.state = 0

    def autonomousPeriodic(self):
        self.autonomousRoutine.run() # see autonomous.py

    def test(self):
        # reset gyro
        self.C.gyroS.reset()
        # reset encoder
        self.C.driveYEncoderS.reset()

if __name__ == "__main__":
    wpilib.run(Randy)
