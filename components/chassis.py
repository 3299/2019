"""
Drives. Can accept input from joysticks or values [-1, 1].
Uses the wheel-attached encoders as input for a threaded PID
loop on each wheel.
"""
import helpers
import wpilib
import math
from networktables import NetworkTables

class Chassis(object):
    def __init__(self, drive, gyro):
        self.drive          = drive
        self.gyro           = gyro
        self.jDeadband      = 0.05
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

    def run(self, leftX, leftY, rightX, microLeft, microTop, microRight, microBackward):
        self.arcade(helpers.raiseKeepSign(leftX, 2) + 0.4*(microRight - microLeft),
                    helpers.raiseKeepSign(leftY, 2) + 0.4*(microBackward - microTop),
                    rightX)

    def arcade(self, x1, y1, x2):
        # rotation curve
        rotation = helpers.raiseKeepSign(helpers.deadband(-x2 * 0.8, self.jDeadband), 2) 
        self.cartesian(x1, y1, rotation)

    def cartesian(self, x, y, rotation):
        """Uses the gryo to compensate for bad design :P"""
        self.pidAngle.setP(self.sd.getNumber("P", 0.03))
        self.pidAngle.setI(self.sd.getNumber("I", 0))
        self.pidAngle.setD(self.sd.getNumber("D", 0.1))
        if rotation == 0:
            # reset gryo when rotation stops
            if (self.wasRotating):
                print("gyro reset! :D")
                self.gyro.reset()
                self.wasRotating = False

            # PID controller
            self.pidAngle.setSetpoint(0)
            self.pidAngle.enable()
            self.pidAngle.setContinuous(True)
            rotation = -self.pidRotateRate
        else:
            # if there's non-zero rotation input from the joystick, don't run the PID loop
            #self.pidAngle.disable()
            self.wasRotating = True


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
        self.drive['frontLeft'].set(math.sin(speeds[0]))
        self.drive['frontRight'].set(math.sin(speeds[1]))
        self.drive['backLeft'].set(math.sin(speeds[2]))
        self.drive['backRight'].set(math.sin(speeds[3]))

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
