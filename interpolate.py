from __future__ import division
import math

def linear_interpolate(line_coords, factor):
    return (int(line_coords[0]), int(line_coords[1]), int(line_coords[0] + ((line_coords[2]-line_coords[0])*factor)), int(line_coords[1]+((line_coords[3]-line_coords[1])*factor)))