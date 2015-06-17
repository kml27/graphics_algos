# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 12:21:48 2015

@author: Kenny
"""
from __future__ import division
import math, turtle


#archimedes spiral (ish)

turtle.speed(0)

turtle.getscreen().tracer(16, 5)

#iterate from this number of divisions to the min (triangle)
max_divisions = 10

triangle_min = 2

just_degrees=360

#full_circle_radians = 2*math.pi
#180/pi 
turtle.home()
turtle.clear()

iterations=10
#check if there's a relationship between the ratio of geometric sides to interior angles
#and the argand(polar) graph of riemman zeta(critical line)
#z=x+iy



#for set_i in range(-2, 5):
for set_i in range(1,2):
    
    
    turtle.pencolor((0,0,0))  
            
    
    for num_fragments in range(triangle_min, max_divisions):
    
        #turtle.clear()
        
     
        outer_diameter=math.pow(2, set_i)
        #dec_amt = 10
    
        turtle.penup() 
        turtle.home() 
        turtle.seth(90)
        turtle.forward(outer_diameter)
        turtle.pendown()    
    
        #interior_angle =(num_fragments-2)*180/num_fragments
#works for 4,5,6,?        
        #one_fragment =(num_fragments-2)*180/num_fragments    
            
        scale_den=num_fragments*iterations
        
        scale_den=num_fragments*(1/iterations)
        scale_den=1/iterations        
        print "scale den", scale_den
    
        #one_fragment = full_circle_radians/divisions
#works for 3        
        #one_fragment= just_degrees//(num_fragments*2)
        one_fragment=just_degrees/num_fragments    
    
        print "sides: ", num_fragments
        print "one arc: ", one_fragment
    
        cur_heading=0#one_fragment
    
    #    scale_inc = 360//scale_den
        scale_dec=(1/iterations)/scale_den
        print "scale dec",scale_dec
        scale= 1
            
        for d_it in range(0,num_fragments*iterations):    
            #turtle.pencolor((0.5,0.5,0.5))
            #turtle.circle(outer_diameter)        
            length=outer_diameter*scale#*math.cos(scale)        
            turtle.seth(cur_heading)
            #turtle.left(cur_heading)
                  
            
            print "heading ", cur_heading
            print "scale: ", scale#, math.cos(cur_heading)
            turtle.forward(length)
            scale=scale-scale_dec
            cur_heading=cur_heading-one_fragment#*-1        
            
            #print "diameter: ", outer_diameter