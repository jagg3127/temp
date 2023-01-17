#!/usr/bin/env python3
from ev3dev2.motor import Motor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from sys import argv
print(argv)

num=argv[1]

fire    = Motor(address='outA')

def run(motor: Motor):
    motor.on_for_rotations(1, 1)

run(fire)
