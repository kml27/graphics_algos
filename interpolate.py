from __future__ import division
import math

def linear_interpolate(coords, factor, type=int):
    #print coords,factor
    if type is int:
        #print type
        if len(coords)==4:
            return (int(coords[0]), int(coords[1]), int(coords[0] + ((coords[2]-coords[0])*factor)), int(coords[1]+((coords[3]-coords[1])*factor)))
        elif len(coords)==2:
            return int((coords[1] - coords[0])*factor)
    
    if type is float:
        #print type
        if len(coords)==2:
            #print coords
            return float(coords[0] + (coords[1] - coords[0]) *factor)