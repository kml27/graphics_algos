import os, sys, random
os.environ["PYSDL2_DLL_PATH"]="."

import sdl2, sdl2.ext, sdl2.ext.pixelaccess

software = True

width = 800
height = 600

window_size = (width, height)
clear_color = 0x00000000

#flame_size

flame_offset=(width/6, 0)

flame_area=((width*2)/3, height)

#heat
rate =  1

old_triangle_kernel = [    0, 0.25,    0,
                        0.25, 0.25, 0.25
                       ]

#starts blur at top + kernel_height, left + kernel_width
def blur(mem,  width, height, x_dir, y_dir, kernel_width, kernel_height, kernel_shape_mask):
    start_y = kernel_height
    start_x = kernel_width
    
    
    end_y = height
    end_x = width
    
    if y_dir < 0:
        start_y, end_y = end_y, start_y
    
    for offset_y in range(start_y, end_y):
        for offset_x in range(start_x, end_x):
        
            #initialize pixel contribution to current pixel from kernel sampled pixels
            pixel_contribution = 0
            
            #gather contributions from kernel pixels
            for y in range(len(kernel_height)):
                for x in range(len(kernel_width)):
                    pixel_contribution = mem[offset_x+x+y*width]*kernel_shape_mask[x+y*kernel_width]
            
            mem[offset_x+offset_y*width] += blur_contribution

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Olde Blur Fire", window_size)
    
    renderer = sdl2.ext.Renderer(window)
    
    if software:
        sprite_factory = sdl2.ext.SpriteFactory(sprite_type=sdl2.ext.SOFTWARE, renderer=renderer)
    else:
        sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    
    sprite_render_system = sprite_factory.create_sprite_render_system(window)
    
    renderer.blendmode = sdl2.SDL_BLENDMODE_BLEND
    
    fire_sprite = None
    if software:
        fire_sprite = sprite_factory.create_software_sprite(size=flame_area)
    else:
        fire_sprite = sprite_factory.create_texture_sprite(size=flame_area)
    
    
    window.show()
    renderer.clear(clear_color)
    
    fire_mem = sdl2.ext.pixelaccess.PixelView(fire_sprite)
    
    print("sprite memory has {0} dimensions".format(fire_mem.ndim))
    
    last_sprite_y = flame_area[1]/2#flame_area[1]-1
    print("last_sprite_y {0}".format(last_sprite_y))
    x_offset = last_sprite_y*flame_area[0]
    print("linear offset {0}".format(x_offset))
    
    for x in range(flame_area[0]):
        seed = (long(random.random()*0xFF7F)<<16)+0x7F000000
        #print "pixel {0} = 0x{1:X}".format(x, seed)
        #print "linear pixel offset {0}".format(x_offset+x)
        fire_mem[x_offset+x] = seed
        #raw_input()
    
    running=True
    
    n=0
    
    while(running):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running=False
        
        
        blur(fire_mem, flame_area[0], flame_area[1], 0, -1, 3, 2, old_triangle_kernel)
        
        sprite_render_system.render(fire_sprite, flame_offset[0], flame_offset[1])
        n+=1
        print(n)
        #renderer.present()
        
    
    return 0
    
if __name__ == "__main__":
    sys.exit(run())