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
robot = DriveBase (right_motor, left_motor, wheel_diameter = 56, axle_track = 114)

cs1 = ColorSensor(Port.S1)
cs2 = ColorSensor(Port.S4)
us = UltrasonicSensor(Port.S3)




kp = 2

speed = 150


program_on = True
robo_on = True




while program_on == True:
    if ev3.buttons.pressed():
        
        ev3.speaker.say("Exercise 3")
        ref_limit1 = cs1.reflection()
        ref_limit2 = cs2.reflection()
        
        
        
        while robo_on == True:
            
            devi1 = ref_limit1 - cs1.reflection()
            devi2 = (cs2.reflection() - ref_limit2) * 0.66
            
            

            turn_r = kp * (devi1 + devi2)

            if devi1 > 0 and devi2 < 0 or devi1 < 0 and devi2 > 0:
                robot.drive(speed, 0)
                
            else:
                robot.drive(speed, turn_r)

            
            if us.distance() < 190:
                robot.stop()
                wait(2000)

            if ev3.buttons.pressed():
                ev3.speaker.say("We won!")
                robo_on = False
                program_on = False
            
            

# Create your objects here.

 
 
 




