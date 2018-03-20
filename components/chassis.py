"""
Drives. Can accept input from joysticks or values [-1, 1].
"""
import helpers
import wpilib
import math
import time
import hal
from networktables import NetworkTables

class Chassis(object):
    def __init__(self, drive, gyro, encoderY):
        self.drive          = drive
        self.gyro           = gyro
        self.encoderY       = encoderY
        self.jDeadband      = 0.06
        self.sd             = NetworkTables.getTable('SmartDashboard')

        self.oldSpeeds      = [0, 0, 0, 0]
        self.rampFactor     = 0.3

        # Boundry on speed (in / sec)
        self.maxSpeed = 37.5

        # PID loop for angle
        self.useAnglePID = False
        self.pidAngle = wpilib.PIDController(0.03, 0, 0.1, self.gyro, lambda: self.updateAnglePID())
        self.pidAngle.setInputRange(-180.0, 180.0)
        self.pidAngle.setOutputRange(-1.0, 1.0)
        self.pidAngle.setAbsoluteTolerance(5)
        self.pidAngle.setContinuous(False)
        self.pidRotateRate = 0
        self.wasRotating = False

        # PID loop for Cartesian Y direction
        self.useYPID = True
        self.pidY = wpilib.PIDController(0.05, 0, 0.02, lambda: self.encoderY.getRate(), self.updateYPID)
        self.pidY.setInputRange(-self.maxSpeed, self.maxSpeed)
        self.pidY.setOutputRange(-1.0, 1.0)
        self.pidY.setContinuous(True)
        self.pidYRate = 0

    def cartesian(self, x, y, rotation):
        # Map joystick values to curve
        x = self.curve(x)
        y = self.curve(y)
        rotation = -rotation * 0.5

        """Uses the gryo to compensate for bad design :P"""
        if (self.useAnglePID != False):
            self.pidAngle.setP(self.sd.getNumber("P", 0.03))
            self.pidAngle.setI(self.sd.getNumber("I", 0))
            self.pidAngle.setD(self.sd.getNumber("D", 0.1))
            if rotation == 0:
                # reset gryo when rotation stops
                if (self.wasRotating):
                    self.gyro.reset()
                    self.wasRotating = False

                # PID controller
                self.pidAngle.setSetpoint(0)
                self.pidAngle.enable()
                self.pidAngle.setContinuous(True)
                rotation = -self.pidRotateRate
            else:
                # if there's non-zero rotation input from the joystick, don't run the PID loop
                self.wasRotating = True

        if (self.useYPID != False):
            mappedY = helpers.remap(y, -1, 1, -self.maxSpeed, self.maxSpeed)
            self.pidY.enable()
            self.pidY.setSetpoint(mappedY)
            y = self.pidYRate
            print(y)

        # assign speeds
        speeds = [0] * 4
        speeds[0] =  x + y + rotation # front left
        speeds[1] = -x + y - rotation # front right
        speeds[2] = -x + y + rotation # back left
        speeds[3] =  x + y - rotation # back right

        # scales all speeds if one is in range
        # (-inf, -1) U (1, inf)
        maxSpeed = max(abs(x) for x in speeds)
        if maxSpeed > 1.0:
            for i in range(0, 4):
                speeds[i] = speeds[i] / maxSpeed

        # write speeds to controllers
        for i in range(0, 4):
            self.drive[i].set(speeds[i])

    def updateAnglePID(self, value):
        self.pidRotateRate = value

    def updateYPID(self, value):
        self.pidYRate = value

    def curve(self, value):
        """Because this divides by sin(1), an input
        in range [-1, 1] will always have an output
        range of [-1, 1]. """

        value = helpers.deadband(helpers.raiseKeepSign(value, 1), self.jDeadband)

        return (math.sin(value) / math.sin(1));

    def straight(self, duration, power):
        """Intended for use in auto."""
        if hal.isSimulation() == False:
            startTime = time.clock()
            while (time.clock() - startTime < duration):
                self.cartesian(0, power, 0)
                print(time.clock())

            # Stop
            self.cartesian(0, 0, 0)

    def driveToAngle(self, power, angle):
        """Intended for use in auto."""
        self.gyro.reset()
        self.pidAngle.setSetpoint(angle)
        self.pidAngle.enable()

        while (abs(self.pidAngle.getError()) > 2):
            print(self.pidAngle.getError())
            self.cartesian(0, 0, -self.pidRotateRate)

            self.pidAngle.disable()
            self.cartesian(0, 0, 0)
            self.gyro.reset()
            return

    def driveToPosition(self, distance):
        print (distance)
