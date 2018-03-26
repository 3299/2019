import os.path
import pickle
import pathfinder as pf
import wpilib
import math
# because of a quirk in pyfrc, this must be in a subdirectory
# or the file won't get copied over to the robot
pickle_file = os.path.join(os.path.dirname(__file__), 'trajectory.pickle')

class Paths(object):
    def __init__(self):
        if wpilib.RobotBase.isSimulation():
            # Generate trajectories during testing
            paths = {
                'forward': [
                    pf.Waypoint(-11, 0, 0),
                    pf.Waypoint(0, 0, 0)
                ],

                'left': [
                    pf.Waypoint(0, 0, 0),
                    pf.Waypoint(6, -6, 0),
                    pf.Waypoint(11, -6, 0),
                    pf.Waypoint(8, 0, math.radians(-90)),
                    #pf.Waypoint(18, 0, 0)
                    #pf.Waypoint(14, 14, 0)
                    #pf.Waypoint(10, 15, 0),
                    #pf.Waypoint(14, 14, math.radians(-90))
                    #pf.Waypoint(-8, -5, 0),
                    #pf.Waypoint(-4, -1, math.radians(-45.0)),   # Waypoint @ x=-4, y=-1, exit angle=-45 degrees
                    #pf.Waypoint(-2, -2, 0),                     # Waypoint @ x=-2, y=-2, exit angle=0 radians
                ]
            }

            trajectories = {}

            for path in paths:
                info, trajectory = pf.generate(paths[path],
                                               pf.FIT_HERMITE_CUBIC,
                                               pf.SAMPLES_HIGH,
                                               dt = 0.05,
                                               max_velocity = 1.7,
                                               max_acceleration = 2,
                                               max_jerk = 100
                                               )
                trajectories[path] = trajectory

                self.trajectories = trajectories

            # and then write it out
            with open(pickle_file, 'wb') as fp:
                pickle.dump(self.trajectories, fp)
        else:
            with open(pickle_file, 'rb') as fp:
                self.trajectories = pickle.load(fp)
