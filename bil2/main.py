#!/usr/bin/env pybricks-micropython

 #import
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.



# Create your objects here.
ev3 = EV3Brick()


# Write your program here.

right_motor = Motor(Port.A)
left_motor = Motor(Port.D)
robot = DriveBase (left_motor, right_motor, wheel_diameter = 56, axle_track = 114)



 
ts1 = TouchSensor(Port.S2)
ts2 = TouchSensor(Port.S3)
program_on = True
robo_on = True


while program_on == True:
    if ev3.buttons.pressed():
        
        ev3.speaker.say("Exercise 2")
        
        while robo_on == True:
            robot.drive(100, 0)
            
            while ts1.pressed() == True or ts2.pressed() == True:
                robot.stop()
                
                robot.drive_time(-100, 0, 2000)
                robot.drive_time(100, 90, 1000)
                wait(300)
        
            if ev3.buttons.pressed():
                ev3.speaker.say("Exercise done")
                robo_on = False
                program_on = False

# Create your objects here.

 
 
 



