import os, sys
os.environ["PYSDL2_DLL_PATH"]="."

import sdl2, sdl2.ext

import time

import de_casteljau_bezier

window_size = (800, 600)
clear_color = 0x00000000
draw_color = 0x8000FFFF
guide_color1 = 0x80FF00FF
guide_color2 = 0x80FFFFFF
highlight_line = 0x40FFFF00
highlight_point = highlight_line

#Globals
MODIFY_END_POINT = 0
MODIFY_CONTROL_POINT = 1

def update_point(dcb, mode, point, segment_index):
    if mode == MODIFY_CONTROL_POINT:
        #print "setting new control point for segment", segment_index, point
        dcb.modify_segment(segment_index, control_point=point)
    elif mode == MODIFY_END_POINT:
        #print "setting new end point for segment", segment_index, point
        dcb.modify_segment(segment_index, end_point=point)

def run():
    SHOW_CONTROL_LINES=False

    sdl2.ext.init()
    window = sdl2.ext.Window("De Casteljau Bezier", window_size)
    
    renderer = sdl2.ext.Renderer(window)
    
    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    
    renderer.blendmode = sdl2.SDL_BLENDMODE_BLEND
    
    window.show()
    renderer.clear(clear_color)
    
    running=True
    
    #index of current endpoint to modify
    segment_index = 0
    
    #modify control or endpoint
    modify = MODIFY_END_POINT
    
    dcb = de_casteljau_bezier.bezier()

    #left_button_down = SDL_GetMouseState()
    left_button_down = False
    
    
    print "A: add segment"
    print "S: cycle select segment, segment will be selected for modification"
    print "C: select control point to modify"
    print "E: select end point to modify"
    print "P: print all points"
    print "B: blank canvas"
    print "G: toggle guides"
    print "W: write bezier to file"
    
    while(running):
        events = sdl2.ext.get_events()
        for event in events:
            #exit
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running=False
            elif event.type==sdl2.SDL_KEYDOWN:
            #change to endpoint or control modification
                if event.key.keysym.sym == sdl2.SDLK_c:
                    print "modify control point mode"
                    modify = MODIFY_CONTROL_POINT
                elif event.key.keysym.sym == sdl2.SDLK_e:
                    print "modify end point mode"
                    modify = MODIFY_END_POINT
                elif event.key.keysym.sym == sdl2.SDLK_s:
                    segment_index = (segment_index+1)%len(dcb)
                    print "cycled to next segment", segment_index
                elif event.key.keysym.sym == sdl2.SDLK_a:
                    #add segment
                    dcb.add_segment()
                    print "adding new segment", len(dcb)
                elif event.key.keysym.sym == sdl2.SDLK_b:
                    renderer.clear(clear_color)
                elif event.key.keysym.sym == sdl2.SDLK_p:
                    print "\n" + str(dcb)
                elif event.key.keysym.sym == sdl2.SDLK_g:
                    SHOW_CONTROL_LINES = not SHOW_CONTROL_LINES
                elif event.key.keysym.sym == sdl2.SDLK_w:
                    fn = str(time.time())+".dcb"
                    file = open(fn, "w+")
                    print "writing with filename: ", fn
                    file.write(str(dcb))
                    file.close()
            elif event.type==sdl2.SDL_MOUSEBUTTONUP:
                if(event.button.button== sdl2.SDL_BUTTON_LEFT):
                    left_button_down = False
                    #print "left mouse button up"
            elif event.type==sdl2.SDL_MOUSEBUTTONDOWN:
                #class SDL_MouseButtonEvent(Structure):
                #_fields_ = [("type", Uint32),
                #("timestamp", Uint32),
                #("windowID", Uint32),
                #("which", Uint32),
                #("button", Uint8),
                #("state", Uint8),
                #("clicks", Uint8),
                #("padding1", Uint8),
                #("x", Sint32),
                #("y", Sint32)
                #]
                
                if(event.button.button== sdl2.SDL_BUTTON_LEFT):
                    left_button_down = True
                    #print "left mouse button down"
                    point=(event.button.x, event.button.y)
                    update_point(dcb, modify, point, segment_index)
            elif event.type == sdl2.SDL_MOUSEMOTION and left_button_down:
                    #print "draw"
                    point=(event.motion.x, event.motion.y)
                    update_point(dcb, modify, point, segment_index)
        #todo: determine equation for correct minimal number of steps
        N=1000
        
        if SHOW_CONTROL_LINES:
            #print "drawing lines"
            #for each segment, sub one for last segment being the last 'next_segment'
            
            number_of_segments = len(dcb)-1
            #from 0 to len-1-1 for index
            for i in range(number_of_segments):
                
                current_segment = dcb[i]
                
                #if i+1 < number_of_segments:
                next_segment = dcb[i+1]
                
                
                renderer.draw_line((current_segment.end_point[0], current_segment.end_point[1], current_segment.control_point[0], current_segment.control_point[1]), guide_color1)
                #if there is a next segment, draw a line between the control points
                #if next_segment is not None:
                renderer.draw_line((current_segment.control_point[0], current_segment.control_point[1], next_segment.control_point[0], next_segment.control_point[1]), guide_color2)
                
                renderer.draw_line((next_segment.control_point[0], next_segment.control_point[1], next_segment.end_point[0], next_segment.end_point[1]), guide_color1)
                
            
            renderer.draw_point(dcb[segment_index].end_point, highlight_point)
            p1 = dcb[segment_index].control_point
            p2 = dcb[segment_index].end_point
            renderer.draw_line((p1[0], p1[1], p2[0], p2[1]), highlight_line)
            
        for s in range(len(dcb)-1):
            for t in range(N):
            
                point = dcb.solve(t/float(N), SHOW_CONTROL_LINES, renderer, segment=s)
                
                renderer.draw_point(point, draw_color)
        
        renderer.present()
            
    return 0
    
if __name__ == "__main__":
    sys.exit(run())