from __future__ import division
import math


#a point x,y can be viewed as a rotation of any point in the set of solutions for the circle with radius r
#x = r cos theta
#y = r sin theta


#x'=x cos phi - y sin phi
#y'=y cos phi + x sin phi
#
#matrix
#[+cos theta | -sin theta]
#[+sin theta | +cos theta]

def rotate((x, y), angle_of_rotation):#, initial_angle=math.pi/2):
    return (int(x*math.cos(angle_of_rotation)+y*math.sin(angle_of_rotation)), int(-x*math.sin(angle_of_rotation) + y*math.cos(angle_of_rotation)))