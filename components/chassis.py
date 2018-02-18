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
    def __init__(self, drive, gyro):
        self.drive          = drive
        self.gyro           = gyro
        self.jDeadband      = 0.05

        self.usePID         = False
        self.pidAngle       = wpilib.PIDController(0.03, 0, 0.1, self.gyro, output=self)
        self.sd             = NetworkTables.getTable('SmartDashboard')
        self.sd.putNumber('P', 0.022)
        self.sd.putNumber('I', 0)
        self.sd.putNumber('D', 0)
        self.pidAngle.setInputRange(-180.0, 180.0)
        self.pidAngle.setOutputRange(-1.0, 1.0)
        self.pidAngle.setAbsoluteTolerance(5)
        self.pidAngle.setContinuous(False)
        self.pidRotateRate = 0
        self.wasRotating = False

    def run(self, leftX, leftY, rightX):
        self.cartesian(self.curve(leftX), self.curve(leftY), helpers.raiseKeepSign(-rightX * 0.7, 2))

    def cartesian(self, x, y, rotation):
        """Uses the gryo to compensate for bad design :P"""
        if (self.usePID != False):
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


        # assign speeds
        speeds = [0] * 4
        speeds[0] =  x - y - rotation
        speeds[1] =  x + y - rotation
        speeds[2] = -x - y - rotation
        speeds[3] = -x + y - rotation

        # scales all speeds if one is in range
        # (-inf, -1) U (1, inf)
        maxSpeed = max(speeds)
        minSpeed = min(speeds)

        if (maxSpeed > 1):
            for i in range (0, 4):
                if (speeds[i] != 0):
                    speeds[i] = speeds[i] / maxSpeed
        elif (minSpeed < -1):
            for i in range(0, 4):
                if (speeds[i] != 0):
                    speeds[i] =  - (speeds[i] / minSpeed)

        # set scaled speeds
        self.drive['frontLeft'].set(self.curve(speeds[0]))
        self.drive['frontRight'].set(self.curve(speeds[1]))
        self.drive['backLeft'].set(self.curve(speeds[2]))
        self.drive['backRight'].set(self.curve(speeds[3]))

    def polar(self, power, direction, rotation):
        power = power * math.sqrt(2.0)

        # The rollers are at 45 degree angles.
        dirInRad = math.radians(direction + 45)
        cosD = math.cos(dirInRad)
        sinD = math.sin(dirInRad)

        speeds = [0] * 4
        speeds[0] = sinD * power + rotation
        speeds[1] = cosD * power - rotation
        speeds[2] = cosD * power + rotation
        speeds[3] = sinD * power - rotation

        self.drive['frontLeft'].set(speeds[0])
        self.drive['frontRight'].set(speeds[1])
        self.drive['backLeft'].set(speeds[2])
        self.drive['backRight'].set(speeds[3])


    def driveToAngle(self, power, angle, continuous):
        self.gyro.reset()
        self.pidAngle.setSetpoint(angle)
        self.pidAngle.enable()
        self.pidAngle.setContinuous(continuous)

        if (continuous == True): # if true, runs continuously (for driving straight)
            print(self.pidRotateRate)
            self.cartesian(0, -power, -self.pidRotateRate)
        else:
            while (abs(self.pidAngle.getError()) > 2):
                print(self.pidAngle.getError())
                self.cartesian(0, 0, -self.pidRotateRate)

            self.pidAngle.disable()
            self.cartesian(0, 0, 0)
            self.gyro.reset()
            return;

    def pidWrite(self, value):
        self.pidRotateRate = value

    def curve(self, value):
        """Because this divides by sin(1), an input
        in range [-1, 1] will always have an output
        range of [-1, 1]. """
        value = helpers.raiseKeepSign(value, 1)

        return (math.sin(value) / math.sin(1));

    def straight(self, duration, power):
        if hal.isSimulation() == False:
            startTime = time.clock()
            while (time.clock() - startTime < duration):
                self.cartesian(0, power, 0)
                print(time.clock())

            # Stop
            self.cartesian(0, 0, 0)
