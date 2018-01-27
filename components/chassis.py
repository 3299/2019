"""
Drives. Can accept input from joysticks or values [-1, 1].
"""
import helpers
import wpilib
import math


class Chassis(object):
    def __init__(self, drive, gyro):
        self.drive          = drive
        self.gyro           = gyro
        self.jDeadband      = 0.05
        self.pidAngle       = wpilib.PIDController(0.03, 0, 0.1, self.gyro, output=self)

        self.pidAngle.setInputRange(-180.0, 180.0)
        self.pidAngle.setOutputRange(-1.0, 1.0)
        self.pidAngle.setAbsoluteTolerance(5)
        self.pidAngle.setContinuous(False)
        self.pidRotateRate = 0
        self.wasRotating = False

    def run(self, leftX, leftY, rightX, microLeft, microTop, microRight, microBackward):
        self.arcade(helpers.raiseKeepSign(leftX, 2) + 0.4*(microRight - microLeft),
                    helpers.raiseKeepSign(leftY, 2) + 0.4*(microBackward - microTop),
                    rightX)

    def arcade(self, x1, y1, x2):
        # rotation curve
        rotation = helpers.raiseKeepSign(helpers.deadband(-x2, self.jDeadband), 2)
        self.cartesian(x1, y1, rotation)

    def cartesian(self, x, y, rotation):
        """Uses the gryo to compensate for bad design :P"""
        if rotation == 0:
            # reset gryo when rotation stops
            if (self.wasRotating):
                self.gryo.reset()
                self.wasRotating = False

            # PID controller
            self.pidAngle.setSetpoint(0)
            self.pidAngle.enable()
            self.pidAngle.setContinuous(True)
            rotation = -self.pidRotateRate
        else:
            # if there's non-zero rotation input from the joystick, don't run the PID loop
            self.pidAngle.disable()
            self.wasRotating = True

        print(rotation)

        # asign speeds
        speeds = [0] * 4
        speeds[0] = -x + y + rotation
        speeds[1] = x + y - rotation
        speeds[2] = x + y + rotation
        speeds[3] = -x + y - rotation

        # TODO: this will currrently scale speeds if over `1`, but not if under `-1`
        if (max(speeds) > 1):
            maxSpeed = max(speeds)
            for i in range (0, 4):
                if (speeds[i] != 0):
                    speeds[i] = maxSpeed / speeds[i]

        # set scaled speeds
        self.drive['frontLeft'].set(speeds[0])
        self.drive['frontRight'].set(speeds[1])
        self.drive['backLeft'].set(speeds[2])
        self.drive['backRight'].set(speeds[3])

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

    def pidWrite(self, value):
        self.pidRotateRate = value

    def curve(self, value):
        return (math.sin(value) / math.sin(1));
