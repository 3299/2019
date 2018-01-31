"""
Main logic code
"""
import wpilib
import time

from inits import Component
import helpers

from components.chassis import Chassis

from autonomous import Autonomous
from components.lights import Lights

class Randy(wpilib.SampleRobot):
    def robotInit(self):
        # init cameras
        wpilib.CameraServer.launch()

        self.C = Component() # Components inits all connected motors, sensors, and joysticks. See inits.py.

        # Setup subsystems
        self.drive = Chassis(self.C.driveTrain, self.C.gyroS)
        self.lights = Lights()

        self.autonomousRoutine = Autonomous(self.drive)
        
        # Joysticks or xBox controller?
        self.controller = 'xbox' # || xbox

        if (self.controller == 'joysticks'):
            self.C.leftJ = wpilib.Joystick(0)
            self.C.middleJ = wpilib.Joystick(1)
            self.C.rightJ = wpilib.Joystick(2)
        elif (self.controller == 'xbox'):
            self.C.joystick = wpilib.XboxController(0)

    def operatorControl(self):
        # runs when robot is enabled
        while self.isOperatorControl() and self.isEnabled():
            '''
            Components
            '''
            # Drive
            if (self.controller == 'joysticks'):
                self.drive.run(self.C.leftJ.getX(),
                               self.C.leftJ.getY(),
                               self.C.middleJ.getX(),
                               self.C.leftJ.getRawButton(4),
                               self.C.leftJ.getRawButton(3),
                               self.C.leftJ.getRawButton(5),
                               self.C.leftJ.getRawButton(2))

            elif (self.controller == 'xbox'):
                self.drive.arcade(self.C.joystick.getRawAxis(0), self.C.joystick.getRawAxis(1), self.C.joystick.getRawAxis(4))

            # Lights
            self.lights.stagger('blue', True, 255)

            wpilib.Timer.delay(0.002) # wait for a motor update time

    def test(self):
        """This function is called periodically during test mode."""

    def autonomous(self):
        """Runs once during autonomous."""
        self.autonomousRoutine.run() # see autonomous.py

if __name__ == "__main__":
    wpilib.run(Randy)
