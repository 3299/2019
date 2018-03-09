"""
Controls intake wheels, the elevator, and the metabox.
"""

class MetaBox(object):
    def __init__(self, encoderS, limitS, elevatorM):
        self.encoder = encoderS
        self.limit = limitS
        self.elevatorM = elevatorM

    def run(self, value):
        self.elevatorM.set(value)

    def getEncoder(self):
        return self.encoder.getDistance()
