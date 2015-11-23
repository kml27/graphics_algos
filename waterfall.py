import os, sys, random
os.environ["PYSDL2_DLL_PATH"]='.'
import sdl2, sdl2.ext

txtr=1
#window_size=(800,600)
window_size=(1920,1080)
sprite_scale=1
quickness = 2

percentage=0.5
    
def init_sprite_loc(sprite):
    sprite.x = int(random.random()*window_size[0])
    sprite.y = int(random.random()*int(window_size[1]*percentage))+int(window_size[1]//2.0)-int(window_size[1]*percentage//2.0)
    
class noise_obj(sdl2.ext.Entity):
    def __init__(self, world, sprite, vel=None):
        super(noise_obj, self).__init__(world)
        
        if vel is None:
            self._vel = Velocity()
        else:
            self._vel=vel
        
        self._sprite=sprite

vels = []
#objsl = []
class move(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(move, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.minx=minx
        self.miny=miny
        self.maxx=maxx
        self.maxy=maxy
        self.active_y_boundary = (window_size[1]/2)+int(window_size[1]*percentage//2.0)
        print('created move')
    
    def process(self, world, componentsets):
        #print("move process")
        #print(componentsets)
        for vel, sprite in componentsets:
            #print(object)
            #print(type(vel), type(sprite))
            #print('sprite x' + str(sprite.x))
            sprite.x += vel.vx
            #print('sprite y' + str(sprite.y))
            sprite.y += vel.vy
            
            if sprite.y > self.active_y_boundary:
                init_sprite_loc(sprite)

class Velocity(object):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vx=0
        self.vy=0
        




def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Parallax Scroll", size=window_size)
    world = sdl2.ext.World()
    
    renderer = sdl2.ext.Renderer(window)
    renderer.blendmode = sdl2.SDL_BLENDMODE_BLEND
    if txtr == 1:
        sprite_factory = sdl2.ext.SpriteFactory(renderer=renderer)
    else:
        sprite_factory = sdl2.ext.SpriteFactory(sprite_type=sdl2.ext.SOFTWARE, renderer=renderer)
    
    sprite_render_system = sprite_factory.create_sprite_render_system(window)

    print("created sprite render system "  + str(type(sprite_render_system)))

    
    movement = move(0,0,window_size[0], window_size[1])
    
    rands = []#([],[],[])
    
    
    
    for i in range(0, (window_size[1]/2)*3):
        #print(i)
        for j in range(0,3):
            #print(j)
            scale = 1.25#random.random()#
            mod = random.random()*0x40*scale
            color = (int(0x60-mod),int(mod),int(0xff-mod),0.25)
            if txtr==1:
                sprite = sprite_factory.from_color(color, (sprite_scale*8,sprite_scale*8))#.create_texture_sprite(renderer, (8,8))
            else:
                sprite = sprite_factory.create_software_sprite((sprite_scale*8,sprite_scale*8))
                
                sprite.fill(color)
            #sprite.from
            init_sprite_loc(sprite)
            vel = Velocity()
            vel.vy = j*quickness
            vels.append(vel)
            #rands[j].append((vel, sprite))
            rands.append(sprite)
            noise_obj(world, sprite, vel)
    
    #print(rands)
    
    window.show()
    #divide in half whatever the desired percentage of the screen is (0.5 becomes 0.25, 0.8 would be 0.4)
    #for i in range(0,int(window_size[1]*percentage//2.0)):
    #    renderer.draw_line((0, (window_size[1]/2)-i-2, window_size[0], (window_size[1]/2)-i-2), (0xff0000FF))
    #    renderer.draw_line((0, (window_size[1]/2)-i-1, window_size[0], (window_size[1]/2)-i-1), (0xff0000FF))
    #    renderer.draw_line((0, (window_size[1]/2)-i, window_size[0], (window_size[1]/2)-i), (0xff0000AF))
    #    renderer.draw_line((0, (window_size[1]/2)+i, window_size[0], (window_size[1]/2)+i), (0xff0000AF))
    #    renderer.draw_line((0, (window_size[1]/2)+i+1, window_size[0], (window_size[1]/2)+i+1), (0xff0000FF))
    #    renderer.draw_line((0, (window_size[1]/2)+i+2, window_size[0], (window_size[1]/2)+i+2), (0xff0000FF))
    #    renderer.present()
    #    sdl2.SDL_Delay(10)
        
    world.add_system(movement)
    
    #print(world.systems)
    
    running=True
    while running:
        events = sdl2.ext.get_events()
        #for i in range(0, 300):
        sprite_render_system.render(rands)
        renderer.present()
        
        for event in events:
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running = False
                break
        #sdl2.SDL_Delay(33)
        world.process()
        sprite_render_system.render(rands)#, clear=True)
        #renderer.clear()
        if txtr==1:
            renderer.present()
        #refresh only needed for sw/surface
        else:
            window.refresh()
    return 0

if __name__ == "__main__":
    sys.exit(run())