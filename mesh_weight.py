from __future__ import division
import math
import os, sys
os.environ["PYSDL2_DLL_PATH"]="."

import rotation, translation

import sdl2, sdl2.ext

width = 800
height = 600

window_size = (width, height)
clear_color = 0x40000000

x_spacing = 20
y_spacing = 20

x_spaces = width / x_spacing
y_spaces = height / y_spacing

def perturb_points(points, offsets, pattern, center):
    new_points = []
    pattern_height = len(pattern)
    pattern_width = len(pattern[0])
    
    grid_pos = [int(center[0]/x_spacing), int(center[1]/y_spacing)]
    
    upperleft = [int(grid_pos[0]-pattern_width/2), int(grid_pos[1]-pattern_height/2)]
    #(center[0]-(x_spacing*pattern_width/2), center[1]-(y_spacing*pattern_height/2))
    #print upperleft
    
    for i, point in enumerate(points):
        #print i, point
        
        cur_x = int(i%x_spaces)
        cur_y = int(i/x_spaces)
        
        
        #print cur_x, cur_y
        
        pattern_x = cur_x - upperleft[0]
        pattern_y = cur_y - upperleft[1]
        
        y_offset = 0
        #print pattern_x, pattern_y
        if pattern_x >= 0 and pattern_x < pattern_width and pattern_y >= 0 and pattern_y < pattern_height :
        #
            #print pattern_x, pattern_y
            y_offset = 3.5*pattern[pattern_y][pattern_x]
        
        point[1] += int(y_offset)
        
        new_points.append([point[0], point[1]])
    return new_points

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Weight", window_size)
    
    renderer = sdl2.ext.Renderer(window)
    
    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    
    renderer.blendmode = sdl2.SDL_BLENDMODE_BLEND
    
    num_x = width/x_spacing
    #print num_x
    num_y = height/y_spacing
    #print num_y
    
    points=[]
    offset_points=[]
    
    #rotation_offset = 
    
    for y in range(int(num_y)):
        for x in range(int(num_x)):
            points.append([0, 0])
            offset_points.append((x*x_spacing, y*y_spacing))
    
    window.show()
    renderer.clear(clear_color)
    
    center_position = [int(width/2), int(height/2)]

    #print offset_points
    
    pattern =   [ 
                  [0.10,  0.25,  0.50,  0.65,  0.75,  0.65,  0.50,  0.25, 0.10], 
                  [0.25,  0.50,  0.75,  1.00,  1.25,  1.00,  0.75,  0.50, 0.25],
                  [0.25,  0.75,  1.00,  1.25,  1.50,  1.25,  1.00,  0.75, 0.25],
                  [0.25,  0.50,  0.75,  1.00,  1.25,  1.00,  0.75,  0.50, 0.25],
                  [0.10,  0.25,  0.50,  0.65,  0.75,  0.65,  0.50,  0.25, 0.10]
                ]
    
    mouse_down = False
    
    auto_center = [0, 160]
    
    theta= 0
    
    output=[]
    
    running=True
    while(running):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running=False
            elif event.type==sdl2.SDL_MOUSEMOTION:
                center_position = [int(event.motion.x), int(event.motion.y)] 
                if event.motion.x == 0 or event.motion.y == 0 or event.motion.x == width-1 or event.motion.y == height-1:
                    mouse_down = False
                else:
                    mouse_down = True
            #elif event.type==sdl2.SDL_MOUSEBUTTONDOWN:
            #    mouse_down = True
            #elif event.type==sdl2.SDL_MOUSEBUTTONUP:
            #    mouse_down = False
            
        theta-=0.0075
        rotated_auto_center= translation.translate(rotation.rotate(auto_center, theta), [width/3, height/3]) 
        neg_rotated_auto_center= translation.translate(rotation.rotate(auto_center, -theta), [2*width/3, height/3])
        
            
        #print center_position
        
        placeholder = [center_position[0],center_position[1], 10, 10]
        
        #renderer.clear(clear_color)
        
        #renderer.draw_rect(placeholder, 0x80FF00FF)
        
        if mouse_down:
            points = perturb_points(points, offset_points, pattern, center_position)
        else:
            points = perturb_points(points, offset_points, pattern, neg_rotated_auto_center)
            points = perturb_points(points, offset_points, pattern, rotated_auto_center)
        #print new_points#, offset_points
        
        
        
        output_cur = translation.translate(points, offset_points)
        
        #renderer.draw_point(output_cur, 0x80FFFFFF)
        
        renderer.draw_line(output_cur, 0x40204000)
        
        if len(output)<1:
            #print len(output)
            output.append(output_cur)
        else:
            renderer.draw_point(output[0], clear_color)
            renderer.draw_line(output[0], clear_color)
            output.append(output_cur)
            del output[0]
            
        
        for point in points:
            #print point
            if point[1] > 0:
                #print "return"
                point[1] -= 0.75
                
        renderer.present()
        
        
        
        
                
    return 0
    
if __name__ == "__main__":
    sys.exit(run())