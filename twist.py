from __future__ import division
import os,sys
os.environ["PYSDL2_DLL_PATH"]="."
import sdl2, sdl2.ext#, sdl2.color
import math, random

txtr=1

#fit to old code
class rectangle(object):
    def __init__(self, x1, y1, x2, y2):
        self.bottom=y2
        self.right=x2
window_size=(800,600)
rect=rectangle(0,0,window_size[0],window_size[1])

#new sdl2 implementation in python

class velocity(object):
    def __init__(self):
        self.vx = 0
        self.vy = 0

class end_point(sdl2.ext.Entity):
    def __init__(self, pos, vel=None):#color=sdl.color.convert_to_color(255,255,255,0.75)):
        self._pos = pos
        self._color = color
        if vel is None:
            self._vel = velocity()
        else:
            self._vel = vel
    

#from old c code

#based on the same calculations used in a rotation matrix, some variatons similar to cartiod, leminscant, et c
#some simiplification of 3d to 2d, some just to make pretty pictures



TABLESIZE=256 #we can take advantage of variable roll over here


#do rotations precalc
#rotation=[]
#[TABLESIZE]
#for i in range(0, TABLESIZE):
#    rotation.append(math.sin(i*((TABLESIZE/2)/3.14))
#    #calculate screen coords from width based on stepsizes from center

new_i=0
new_theta=0.001
def generate_new(center, width, renderer):

       #drawbits=(char *)ddsd.lpSurface;

        #pixel access (PixelView)
        
#        memset(drawbits, 0, ddsd.lPitch*rect.bottom);
        for y in range(-rect.bottom/2, rect.bottom/2):#offset y, one line per scanline in resolution (higher resolution, more intracate)
        #draw line with midpoint on center x and y+rotation, y+rotation[tablesize/2] is half period
        #unsigned ypi=y*3.14;
            new_i+=.01
        #static float theta=0.001;
        
            x1=width*math.cos(y*new_theta+new_i) - y*math.sin(y*new_theta+new_i);
            y1=width*math.sin(y*new_theta) + y*math.cos(y*new_theta);
            x2=width*math.cos(y*new_theta-new_i) - y*math.sin(y*new_theta-new_i);
            y2=width*math.sin(y*new_theta) + y*math.cos(y*new_theta);

        renderer.draw_line((center-x1, y1+rect.bottom/2, center+x2, y2+rect.bottom/2), 0x00ffffff)

i_2=0.000001
def generate2(center, width, renderer):
        i_2=0.000001

        #drawbits=(char *)ddsd.lpSurface;
        #memset(drawbits, 0, ddsd.lPitch*rect.bottom);
        x1=center-width 
        x2=center+width
        for y in range(-3000, 3000):	#do a y for every line
        #draw line with midpoint on center x and y+rotation, y+rotation[tablesize/2] is half period
            ypi=i_2+y*3.14;
            i_2+=.000003;
            renderer.draw_line((int((rect.bottom/2)+x1/6*math.cos(ypi+i) - y/6*math.sin(ypi+i)), int( (rect.right/2)+x1/6*math.sin(ypi+i)+y/6*math.cos(ypi+i)), int( (rect.bottom/2)+x2/6*math.cos(y+i)- y/6*math.sin(y+i)), int((rect.right/2)+x2/6*math.sin(y)+y/6*math.cos(y))), 0xA0ffffff&0xff<<y%32)
i=0.000001
def generate(center, width, renderer):
        i=0.000001
        x1=center-width/2
        x2=center+width/2
        for y in range(int(-rect.bottom//2), int( rect.bottom//2)):
            i+=0.00003;
            renderer.draw_line((int((rect.bottom/2-width/2)+x1/4*math.cos(y+i) - y/2*math.sin(y+i)), int( (rect.right/2-width/2)+x1/4*math.sin(y+i)+y/4*math.cos(y+i)), int((rect.bottom/2+width/2)+x2/4*math.cos(-y-i)- y/4*math.sin(-y-i)), int((rect.right/2+width/2)+x2/4*math.sin(-y-i)+y/4*math.cos(-y-i))), y*0xff)

def generate4(center, width, renderer):
        x1=center-width/2
        x2=center+width/2
        for y in range(0, rect.bottom):
            renderer.draw_line((int(x1*math.sin(y)+y*math.cos(y)), int(x1*math.cos(y) - y*math.sin(y)), int(x2*math.cos(-y)- y*math.sin(-y)), int(x2*math.sin(-y)+y*math.cos(-y))), 0x00ffffff)

def generate5(center, width, renderer):
        x1=center-width/2
        x2=center+width/2
        for y in range(0, rect.bottom):
            renderer.draw_line((int(x1*math.sin(y)+y*math.cos(y)), int(x1*math.cos(y) - y*math.sin(y)), int(x2*math.sin(-y)+y*math.cos(-y)), int(x2*math.cos(-y)- y*math.sin(-y))), 0x00ffffff)

def generate6(center, width, renderer):
        x1=center-width
        x2=center+width/2
        for y in range(0, rect.bottom):
            renderer.draw_line((int(x1+((width/2)*math.sin(y)+y*math.cos(y))), int(x1+((width/2)*math.cos(y) - y*math.sin(y))), int(x2+(-width/2*math.cos(-y)- y*math.sin(-y))), int(x2+((-width/2)*math.sin(-y)+y*math.cos(-y)))), 0x00ffffff)


i_7=0.000001
def generate7(center, width, renderer):
        #the number of loops and the size of the divisor for x1,y1 in line algo are inversly proportional f(x)??? 
        i_7=0.000001
        for y in range(-4000, 4000):
            i_7+=0.000000006;
            
            x1=width*math.cos(y*i) - y*math.sin(y*i);
            y1=width*math.sin(y*i) + y*math.cos(y*i);
            x2=width*math.cos(-y*i)- y*math.sin(-y*i);
            y2=width*math.sin(-y*i)+ y*math.cos(-y*i);
            renderer.draw_line((int(center-x1/8), int(y1/8+rect.bottom/2), int(center+x2/8), int(y2/8+rect.bottom/2)), 0xA0FFffff&0xFF<<y%32)

def generate8(center, width, renderer):
        for y in range(-rect.bottom/20, rect.bottom/20):
            x1=width*math.cos(y*.1) - y*math.sin(y*.1);
            y1=width*math.sin(y*.1) + y*math.cos(y*.1);
            x2=width*math.cos(-y*.1)- y*math.sin(-y*.1);
            y2=width*math.sin(-y*.1)+ y*math.cos(-y*.1);
            renderer.draw_line((center+x1, y1+rect.bottom/2, x2+width, y2+rect.bottom/2), 0x00ffffff)

def generate9(center, width, renderer):
        for y in range(-rect.bottom/2, rect.bottom/2):
            x1=width*math.cos(y*.01) - y*math.sin(y*.01);
            y1=width*math.sin(y*.01) + y*math.cos(y*.01);
            x2=width*math.cos(-y*.01)- y*math.sin(-y*.01);
            y2=width*math.sin(-y*.01)+ y*math.cos(-y*.01);
            renderer.draw_line((center-x1, y1+rect.bottom/2, center+x2, y2+rect.bottom/2), 0x00ffffff)

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Twist", size=window_size)
    world = sdl2.ext.World()
    
    renderer = sdl2.ext.Renderer(window)
    renderer.blendmode = sdl2.SDL_BLENDMODE_NONE
    if txtr == 1:
        sprite_factory = sdl2.ext.SpriteFactory(renderer=renderer)
    else:
        sprite_factory = sdl2.ext.SpriteFactory(sprite_type=sdl2.ext.SOFTWARE, renderer=renderer)
    
    sprite_render_system = sprite_factory.create_sprite_render_system(window)

    print("created sprite render system "  + str(type(sprite_render_system)))
#    movement = move(0,0,window_size[0], window_size[1])
    
    window.show()

#    world.add_system(movement)
    
    running=True
    while running:
        events = sdl2.ext.get_events()
        #for i in range(0, 300):
        #sprite_render_system.render(rands)
        renderer.present()
        
        for event in events:
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running = False
                break
        #sdl2.SDL_Delay(33)
        #world.process()

        renderer.clear()

        #generate7(rect.right/2, rect.right/10, renderer)
        #+random.random()*155
        generate5((rect.right/2)+random.random()*155, rect.right/10+random.random()*155, renderer)

        
        renderer.present()
        
        #refresh only needed for sw/surface
        window.refresh()
    return 0

if __name__ == "__main__":
    sys.exit(run())