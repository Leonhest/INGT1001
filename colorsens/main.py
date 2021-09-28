#!/usr/bin/env pybricks-micropython

 #import
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import random


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.



# Create your objects here.
ev3 = EV3Brick()


# Write your program here.

right_motor = Motor(Port.A)
left_motor = Motor(Port.D)
robot = DriveBase (left_motor, right_motor, wheel_diameter = 56, axle_track = 114)

cs1 = ColorSensor(Port.S1)
cs2 = ColorSensor(Port.S4)










robo_on = True








        
while robo_on == True:
    devi1 = cs1.reflection()
    devi2 = cs2.reflection() 

    print(devi1)
    print(devi2)

            

            
            
    wait(10000)

# Create your objects here.

 
 
 




