'''
Launches the camera streamers in a seperate
thread to prevent the main robot thread
from being overloaded.

from components.cameraserver import CameraServer
#import CameraServer

def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    usb1 = cs.startAutomaticCapture(dev=0)
    #usb2 = cs.startAutomaticCapture(dev=1)

    #usb1.setConnectionStrategy(kKeepOpen)
    #usb2.setConnectionStrategy(kKeepOpen)
    usb1.setResolution(160, 120)
    #usb2.setResolution(160, 120)
    #print("before forever")
    cs.waitForever()
    #print("yay! it works kinda ish maybe")
'''
