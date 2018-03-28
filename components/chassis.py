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

        # PID loop for angle
        self.pidAngleDefault = {'p': 0.01, 'i': 0, 'd': 0.004}
        self.sd.putNumber('pidAngleP', self.pidAngleDefault['p'])
        self.sd.putNumber('pidAngleI', self.pidAngleDefault['i'])
        self.sd.putNumber('pidAngleD', self.pidAngleDefault['d'])

        self.pidAngle = wpilib.PIDController(self.pidAngleDefault['p'], self.pidAngleDefault['i'], self.pidAngleDefault['d'], self.gyro, self.updateAnglePID)
        self.pidAngle.setAbsoluteTolerance(2)
        self.pidRotateRate = 0
        self.wasRotating = False

        # PID loop for Cartesian Y direction
        self.pidYDefault = {'p': 0.15, 'i': 0, 'd': 0.05}
        self.sd.putNumber('pidYP', self.pidYDefault['p'])
        self.sd.putNumber('pidYI', self.pidYDefault['i'])
        self.sd.putNumber('pidYD', self.pidYDefault['d'])

        self.pidY = wpilib.PIDController(self.pidYDefault['p'], self.pidYDefault['i'], self.pidYDefault['d'], self.encoderY.getDistance, self.updateYPID)
        self.pidYRate = 0

        self.toDistanceFirstCall = True
        self.toAngleFirstCall = True
        self.lastAngle = 0

    def run(self, x, y, rotation):
        '''Intended for use in telelop. Use .cartesian() for auto.'''
        # Map joystick values to curve
        x = self.curve(helpers.deadband(x, 0.3))
        y = self.curve(helpers.deadband(y, 0.1))
        rotation = helpers.deadband(-rotation * 0.5, 0.1)

        # write manipulated values to motors
        self.cartesian(-x, y, rotation)

    def cartesian(self, x, y, rotation):
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
        self.pidAngle.setP(self.sd.getNumber('pidAngleP', self.pidAngleDefault['p']))
        self.pidAngle.setI(self.sd.getNumber('pidAngleI', self.pidAngleDefault['i']))
        self.pidAngle.setD(self.sd.getNumber('pidAngleD', self.pidAngleDefault['d']))

        self.pidRotateRate = value

    def updateYPID(self, value):
        self.pidY.setP(self.sd.getNumber('pidYP', self.pidYDefault['p']))
        self.pidY.setI(self.sd.getNumber('pidYI', self.pidYDefault['i']))
        self.pidY.setD(self.sd.getNumber('pidYD', self.pidYDefault['d']))

        self.pidYRate = value

    def curve(self, value):
        """Because this divides by sin(1), an input
        in range [-1, 1] will always have an output
        range of [-1, 1]. """

        value = helpers.deadband(helpers.raiseKeepSign(value, 1), self.jDeadband)

        return (math.sin(value) / math.sin(1));

    def toAngle(self, angle, reset=False):
        """Intended for use in auto."""
        if (self.toAngleFirstCall and reset == True):
            self.gyro.reset()
            self.toAngleFirstCall = False

        self.pidAngle.setSetpoint(angle)
        self.pidAngle.enable()

        print(self.pidAngle.getError())

        if (self.pidAngle.getError() < 2):
            self.pidAngle.disable()
            self.toAngleFirstCall = True
            self.lastAngle = angle
            return True
        else:
            self.cartesian(0, 0, -self.pidRotateRate)
            return False

    def toDistance(self, distance):
        """Intended for use in auto."""
        if (self.toDistanceFirstCall):
            self.encoderY.reset()
            self.toDistanceFirstCall = False

        self.pidY.setContinuous(False)
        self.pidY.setSetpoint(distance)
        self.pidY.enable()

        # simple P for rotation
        rotation = helpers.remap((self.lastAngle - self.gyro.getAngle()), -180, 180, -1, 1)
        rotation = rotation * 1
        print(rotation)

        if (self.pidY.getError() < 0.2):
            self.pidY.disable()
            self.toDistanceFirstCall = True
            return True
        else:
            self.cartesian(0, -self.pidYRate, -rotation)
            return False
