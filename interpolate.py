from __future__ import division
import math

def linear_interpolate(coords, factor, type=int):
    #print coords,factor
    if type is int:
        #print type
        if len(coords)==4:
            #start p1 remains the same, line interpolated to new end point
            return (int(coords[0]), int(coords[1]), int(coords[0] + ((coords[2]-coords[0])*factor)), int(coords[1]+((coords[3]-coords[1])*factor)))
        elif len(coords)==2:
            #point between p1 and p2
            return (int(coords[0][0]+(coords[1][0] - coords[0][0])*factor), int(coords[0][1]+(coords[1][1] - coords[0][1])*factor))
    
    if type is float:
        #print type
        if len(coords)==2:
            #print coords
            return float(coords[0] + (coords[1] - coords[0]) *factor)