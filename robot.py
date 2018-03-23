"""
Main logic code
"""
import wpilib

from inits import Component
import helpers

from components.chassis import Chassis

from autonomous import Autonomous
from components.lights import Lights
from components.metabox import MetaBox
from components.winch import Winch
from components.pdb import Power

class Randy(wpilib.TimedRobot):
    def robotInit(self):
        self.C = Component() # Components inits all connected motors, sensors, and joysticks. See inits.py.

        # Setup subsystems
        self.driverStation = wpilib.DriverStation.getInstance()
        self.drive = Chassis(self.C.driveTrain, self.C.gyroS, self.C.driveYEncoderS)
        self.lights = Lights()
        self.metabox = MetaBox(self.C.elevatorEncoderS, self.C.elevatorLimitS, self.C.elevatorM, self.C.intakeM, self.C.jawsSol, self.C.pusherSol)
        self.winch = Winch(self.C.winchM)
        self.power = Power()

        self.autonomousRoutine = Autonomous(self.drive, self.driverStation)

        # Joysticks
        self.C.joystick = wpilib.XboxController(0)
        self.C.leftJ = wpilib.Joystick(1)

        # default to rainbow effect
        self.lights.run({'effect': 'rainbow'})


    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        '''Components'''
        # Drive
        self.drive.run(self.C.joystick.getRawAxis(0), self.C.joystick.getRawAxis(1), self.C.joystick.getRawAxis(4))

        # MetaBox
        self.metabox.run(self.C.leftJ.getY(),          # elevator rate of change
                         self.C.leftJ.getRawButton(1), # run intake wheels in
                         self.C.leftJ.getRawButton(4), # run 1st push out preset
                         self.C.leftJ.getRawButton(3), # run 2nd push out preset
                         self.C.leftJ.getRawButton(5)) # run 3rd push out preset

        # Winch
        if (self.C.leftJ.getRawButton(9)):
            self.winch.run(1)
        else:
            self.winch.run(0)

        # Lights
        self.lights.setColor(self.driverStation.getAlliance())

        if (self.driverStation.getMatchTime() < 30 and self.driverStation.getMatchTime() != -1):
            self.lights.run({'effect': 'flash', 'fade': True, 'speed': 255})
        elif (helpers.deadband(self.C.leftJ.getY(), 0.1) != 0):
            self.lights.run({'effect': 'stagger'})
        else:
            self.lights.run({'effect': 'rainbow'})

    def teleopInit(self):
        """This function is run once each time the robot enters teleop mode."""
        # reset gyro
        self.C.gyroS.reset()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.lights.run({'effect': 'flash', 'fade': True, 'speed': 400})
        # reset gyro
        self.C.gyroS.reset()

    def autonomousPeriodic(self):
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
        #self.autonomousRoutine.run() # see autonomous.py

if __name__ == "__main__":
    wpilib.run(Randy)
