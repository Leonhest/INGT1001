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


ev3 = EV3Brick()

right_motor = Motor(Port.A)
left_motor = Motor(Port.D)
robot = DriveBase (right_motor, left_motor, wheel_diameter = 56, axle_track = 114)
back_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

cs1 = ColorSensor(Port.S1)
cs2 = ColorSensor(Port.S4)
us = UltrasonicSensor(Port.S3)

kp = 2

speed = 150

ev3.speaker.say("Start")
ref_limit1 = cs1.reflection()
ref_limit2 = cs2.reflection()


while True:
    devi1 = ref_limit1 - cs1.reflection()
    devi2 = (cs2.reflection() - ref_limit2) * 0.66
    
    turn_r = kp * (devi1 + devi2)

    if devi1 > 0 and devi2 < 0:
        robot.drive(speed, 0)
    else:
        robot.drive(speed, turn_r)
        back_motor.run(abs(turn_r) * 2)

    if us.distance() < 40:
        robot.stop()
        wait(1000)
