from __future__ import division
import rotation, translation
import os, sys, math
os.environ["PYSDL2_DLL_PATH"]="."

import sdl2, sdl2.ext

window_size = (800, 600)
clear_color = 0x00000000

draw_color = 0xffffffff

steps = 1000

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Leaf", window_size)
    
    renderer = sdl2.ext.Renderer(window)
    
    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    
    renderer.blendmode = sdl2.SDL_BLENDMODE_BLEND
    
    window.show()
    renderer.clear(clear_color)
    
    delta_theta = 2*math.pi/steps
    
    running=True
    while(running):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running=False
        center = (int(window_size[0]/2), int(window_size[1]/2))
        
        point = (int(window_size[0]/4), int(window_size[1]/3))
        
        renderer.draw_point(translation.translate(point, center), draw_color)
        
        for i in range(0, steps):
            new_point = rotation.rotate(point, delta_theta*i)
            
            percent = ((2*math.pi)/(i+delta_theta))
            #print(percent)
            
            renderer.draw_point(translation.translate(center, new_point), draw_color-(int(percent*0xffffffff)))
        
        renderer.present()
                
    return 0
    
if __name__ == "__main__":
    sys.exit(run())