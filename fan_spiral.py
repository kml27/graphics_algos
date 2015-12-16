import os, sys
os.environ["PYSDL2_DLL_PATH"]="."

import sdl2, sdl2.ext
import rotation, translation, math

window_size = (800, 600)
clear_color = 0x000070CF

divisions = 60
#divisions = 30
fan_interior_angle = 30

length_inc_percentage = 0.5


def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("TriFan", window_size)
    
    renderer = sdl2.ext.Renderer(window)
    
    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    
    renderer.blendmode = sdl2.SDL_BLENDMODE_BLEND
    
    window.show()
    renderer.clear(clear_color)
    
    
    rot_per_div = 2*math.pi/divisions
    
    
    center = (window_size[0]/2, window_size[1]/2)
    
    rot_inc = 0#math.pi/600
    
    rot = 2*math.pi/600
    
    length = center[1]/4
    
    total_rot=0
    sub = 1
    total_lip = length_inc_percentage
    
    running=True
    while(running):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running=False
        
        renderer.clear(clear_color)
        total_rot +=rot_inc
        total_lip-=0.01
        for p in range(0,6):
            for m in range(0,divisions):
                len = (6-p)*length*total_lip#length_inc_percentage
                
                #print len
                current_length = length-(len)
                #lines = []
                for n in range(0,30):#divisions):
                    p2 = translation.translate(rotation.rotate((0,current_length), total_rot),center)
                    renderer.draw_line((center[0], center[1],p2[0], p2[1]),0x2f606060+p*0x001010)
                    total_rot+=rot#rot_per_div
                    current_length -=sub
                
        
        renderer.present()
                
    return 0
    
if __name__ == "__main__":
    sys.exit(run())