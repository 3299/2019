from pyfrc.physics import drivetrains
import math


class PhysicsEngine(object):
    '''
       Simulates a 4-wheel mecanum robot using Tank Drive joystick control
    '''

    def __init__(self, physics_controller):
        '''
            :param physics_controller: `pyfrc.physics.core.Physics` object
                                       to communicate simulation effects to
        '''

        self.physics_controller = physics_controller

        # Precompute the encoder constant
        # -> encoder counts per revolution / wheel circumference
        self.kEncoder = 100 / (0.5 * math.pi)
        self.distance = 0


    def update_sim(self, hal_data, now, tm_diff):
        '''
            Called when the simulation parameters for the program need to be
            updated.

            :param now: The current time as a float
            :param tm_diff: The amount of time that has passed since the last
                            time that this function was called
        '''

        # Simulate the drivetrain
        # -> Remember, in the constructor we inverted the left motors, so
        #    invert the motor values here too!
        lr_motor = -hal_data['pwm'][6]['value']
        rr_motor = hal_data['pwm'][5]['value']
        lf_motor = -hal_data['pwm'][7]['value']
        rf_motor = hal_data['pwm'][3]['value']

        vx, vy, vw = drivetrains.mecanum_drivetrain(lr_motor, rr_motor, lf_motor, rf_motor)
        self.physics_controller.vector_drive(vx, vy, vw, tm_diff)

        # Update encoders
        self.distance += vy * tm_diff
        hal_data['encoder'][1]['count'] = int(self.distance * self.kEncoder)
