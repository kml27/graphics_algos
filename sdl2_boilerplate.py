import os, sys
os.environ["PYSDL2_DLL_PATH"]="."

import sdl2, sdl2.ext

window_size = (800, 600)
clear_color = 0x00000000


def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Leaf", window_size)
    
    renderer = sdl2.ext.Renderer(window)
    
    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    
    renderer.blendmode = sdl2.SDL_BLENDMODE_BLEND
    
    window.show()
    renderer.clear(clear_color)
    
    running=True
    while(running):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running=False
        renderer.present()
                
    return 0
    
if __name__ == "__main__":
    sys.exit(run())