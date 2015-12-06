from __future__ import division
import math
import os, sys
os.environ["PYSDL2_DLL_PATH"]="."

import rotation, translation

import sdl2, sdl2.ext

width = 800
height=600

window_size = (width, height)
clear_color = 0x00000000

x_spacing = 20
y_spacing = 20

def rotation_offset():
    
    rotation=0
    while True:
        yield rotation
        rotation += 1

def rotate_points(points):
    new_points = []
    for point in points:
        #print point
        point[1]+= 0.01
        new_points.append(rotation.rotate(point[0], point[1]))
    return new_points

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Undulate", window_size)
    
    renderer = sdl2.ext.Renderer(window)
    
    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    
    renderer.blendmode = sdl2.SDL_BLENDMODE_BLEND
    
    num_x = width/x_spacing
    print num_x
    num_y = height/y_spacing
    print num_y
    
    points=[]
    offset_points=[]
    
    #rotation_offset = 
    
    for x in range(-1, int(num_x)+2):
        for y in range(-1, int(num_y)+2):
            points.append([(x_spacing,y_spacing), (x+(y*y_spacing))*0.01])
            offset_points.append((x*x_spacing, y*y_spacing))
    
    window.show()
    renderer.clear(clear_color)
    
    running=True
    while(running):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running=False
                
        
        
        renderer.clear(clear_color)
        
        new_points = rotate_points(points)
        
        renderer.draw_point(translation.translate(new_points, offset_points), 0x80FFFFFF)
        
        renderer.present()
        
        
        
        
                
    return 0
    
if __name__ == "__main__":
    sys.exit(run())