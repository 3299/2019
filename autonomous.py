"""
Runs the auto routine. Called once.
"""
import time
import wpilib

class Autonomous(object):
    def __init__(self, drive):
        self.drive = drive

    def run(self):
        print('Autonomous has run')
