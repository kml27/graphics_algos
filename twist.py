from __future__ import division
import os,sys,translation
os.environ["PYSDL2_DLL_PATH"]="."
import sdl2, sdl2.ext#, sdl2.color
import math, random

window_size=(1920,1080)
#window_size=(800,600)
txtr=1


#fit to old code
class rectangle(object):
    def __init__(self, x1, y1, x2, y2):
        self.bottom=y2
        self.right=x2

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

def generate_new(center, width, renderer, alpha=0):

       #drawbits=(char *)ddsd.lpSurface;

        #pixel access (PixelView)
        
#        memset(drawbits, 0, ddsd.lPitch*rect.bottom);
        for y in range(-rect.bottom/2, rect.bottom/2):#offset y, one line per scanline in resolution (higher resolution, more intracate)
        #draw line with midpoint on center x and y+rotation, y+rotation[tablesize/2] is half period
        #unsigned ypi=y*3.14;
            generate_new.i+=.01
        #static float theta=0.001;
        
            x1=width*math.cos(y*new_theta+generate_new.i) - y*math.sin(y*new_theta+generate_new.i);
            y1=width*math.sin(y*new_theta) + y*math.cos(y*new_theta);
            x2=width*math.cos(y*new_theta-generate_new.i) - y*math.sin(y*new_theta-generate_new.i);
            y2=width*math.sin(y*new_theta) + y*math.cos(y*new_theta);
        
        renderer.draw_line((center-x1, y1+rect.bottom/2, center+x2, y2+rect.bottom/2), 0x00ffffff+(int(0xFF*alpha)<<24))
generate_new.i=0

def generate2(center, width, renderer, alpha=0):
        #i_2=0.000001

        #drawbits=(char *)ddsd.lpSurface;
        #memset(drawbits, 0, ddsd.lPitch*rect.bottom);
        x1=center-width 
        x2=center+width
        for y in range(-3000, 3000):	#do a y for every line
        #draw line with midpoint on center x and y+rotation, y+rotation[tablesize/2] is half period
            ypi=generate2.i+y*3.14
            generate2.i+=.000003
            
            p1=translation.translate((rect.bottom/2+x1/6*math.cos(ypi+generate2.i) - y/6*math.sin(ypi+generate2.i),
            rect.right/2+x1/6*math.sin(ypi+generate2.i)+y/6*math.cos(ypi+generate2.i)), (200, -200))
            
            p2=translation.translate( (rect.bottom/2+x2/6*math.cos(y+generate2.i)- y/6*math.sin(y+generate2.i),
            rect.right/2+x2/6*math.sin(y)+y/6*math.cos(y)),(200, -200))
            
            renderer.draw_line((p1[0], p1[1], p2[0], p2[1]), (0x00ffffff&0xff<<y%32) +( int(0xFF*alpha)<<24))
generate2.i=0.000001

def generate(center, width, renderer, alpha=1):
        #i=0.000001
        x1=center-width/2
        x2=center+width/2
        for y in range(int(-rect.bottom//2), int( rect.bottom//2)):
            generate.i+=0.00003;
            p1 = translation.translate((rect.bottom/2-width/2+x1/4*math.cos(y+generate.i) - y/2*math.sin(y+generate.i), rect.right/2-width/2+x1/4*math.sin(y+generate.i)+y/4*math.cos(y+generate.i)), (window_size[0]/4, -window_size[1]/2))
            p2 = translation.translate((rect.bottom/2+width/2+x2/4*math.cos(-y-generate.i)- y/4*math.sin(-y-generate.i), rect.right/2+width/2+x2/4*math.sin(-y-generate.i)+y/4*math.cos(-y-generate.i)),(window_size[0]/4,-window_size[1]/2))
            #print(y/rect.bottom*0xff+0x80)
            #color = y*0xff+int(0x80+y/rect.bottom*0xFF)<<24
            
            color = y*0xff+(int(alpha*0xff)<<24)
            #print(color)
            renderer.draw_line((p1[0],p1[1],p2[0],p2[1]), color)
generate.i=0.000001

def generate4(center, width, renderer, alpha=0):
        x1=center-width/2
        x2=center+width/2
        for y in range(0, rect.bottom):
            renderer.draw_line((int(x1*math.sin(y)+y*math.cos(y)), int(x1*math.cos(y) - y*math.sin(y)), int(x2*math.cos(-y)- y*math.sin(-y)), int(x2*math.sin(-y)+y*math.cos(-y))), 0x00ffffff+(int(0xff*alpha)<<24))
generate4.i=0

def generate5(center, width, renderer, alpha=0):
        #print(alpha)
        color = 0x00ffffff+(int(0xFF*alpha)<<24)
        #print("{:0x}".format( color))
        x1=center-width/2
        x2=center+width/2
        for y in range(0, rect.bottom):
            p1 = translation.translate((x1*math.sin(y)+y*math.cos(y), x1*math.cos(y) - y*math.sin(y)), (0, 0))
            p2 = translation.translate((x2*math.sin(-y)+y*math.cos(-y), x2*math.cos(-y)- y*math.sin(-y)), (0, 0))
            renderer.draw_line((p1[0], p1[1], p2[0], p2[1]), color)

def generate6(center, width, renderer, alpha=0):
        x1=center-width
        x2=center+width/2
        for y in range(0, rect.bottom):
            renderer.draw_line((int(x1+((width/2)*math.sin(y)+y*math.cos(y))), int(x1+((width/2)*math.cos(y) - y*math.sin(y))), int(x2+(-width/2*math.cos(-y)- y*math.sin(-y))), int(x2+((-width/2)*math.sin(-y)+y*math.cos(-y)))), 0x00ffffff+(int(0xFF*alpha)<<24))


def generate7(center, width, renderer, alpha=0):
        #the number of loops and the size of the divisor for x1,y1 in line algo are inversly proportional f(x)??? 
        #i_7=0.000001
        for y in range(-4000, 4000):
            generate7.i+=0.000000006;
            
            x1=width*math.cos(y*i) - y*math.sin(y*i);
            y1=width*math.sin(y*i) + y*math.cos(y*i);
            x2=width*math.cos(-y*i)- y*math.sin(-y*i);
            y2=width*math.sin(-y*i)+ y*math.cos(-y*i);
            renderer.draw_line((int(center-x1/8), int(y1/8+rect.bottom/2), int(center+x2/8), int(y2/8+rect.bottom/2)), 0xA0FFffff&0xFF<<y%32+(int(0xFF*alpha)<<24))
generate7.i=i_7=0.000001

def generate8(center, width, renderer, alpha=0):
        for y in range(int(-rect.bottom/20), int(rect.bottom/20)):
            x1=width*math.cos(y*.1) - y*math.sin(y*.1);
            y1=width*math.sin(y*.1) + y*math.cos(y*.1);
            x2=width*math.cos(-y*.1)- y*math.sin(-y*.1);
            y2=width*math.sin(-y*.1)+ y*math.cos(-y*.1);
            #print(alpha)
            renderer.draw_line((int(center+x1), int(y1+rect.bottom/2), int(x2+width), int(y2+rect.bottom/2)), 0x00ffffff+(int(0xFF*alpha)<<24))

def generate9(center, width, renderer, alpha=0):
        for y in range(int(-rect.bottom/2), int(rect.bottom/2)):
            x1=width*math.cos(y*.01) - y*math.sin(y*.01);
            y1=width*math.sin(y*.01) + y*math.cos(y*.01);
            x2=width*math.cos(-y*.01)- y*math.sin(-y*.01);
            y2=width*math.sin(-y*.01)+ y*math.cos(-y*.01);
            renderer.draw_line((int(center-x1), int(y1+rect.bottom/2), int(center+x2), int(y2+rect.bottom/2)), 0x00ffffff+(int(0xFF*alpha)<<24))

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Twist", size=window_size)
    world = sdl2.ext.World()
    
    renderer = sdl2.ext.Renderer(window)
    renderer.blendmode = sdl2.SDL_BLENDMODE_BLEND
    if txtr == 1:
        sprite_factory = sdl2.ext.SpriteFactory(renderer=renderer)
    else:
        sprite_factory = sdl2.ext.SpriteFactory(sprite_type=sdl2.ext.SOFTWARE, renderer=renderer)
    
    sprite_render_system = sprite_factory.create_sprite_render_system(window)

    print("created sprite render system "  + str(type(sprite_render_system)))
#    movement = move(0,0,window_size[0], window_size[1])
    
    window.show()

    #i=0.000001

#    world.add_system(movement)
    target_off=0.0
    current_off = 0.0
    step=0.005
    running=True
    gen_fns = [
        generate,
        generate4,
        generate5,
        generate6,
        generate8,
        #generate2,
        
        
        #generate7,
        generate9]#,
        #generate_new]
    fn=0
    
    x_off =0
    x_off_target=random.random()
    #new_i=0
    new_theta=0.001

    

    #i_2=0.000001
    while running:
        events = sdl2.ext.get_events()
        #for i in range(0, 300):
        #sprite_render_system.render(rands)
        renderer.present()
        
        for event in events:
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running = False
                break
        #sdl2.SDL_Delay(27)
        #world.process()
                
        renderer.clear()
        if math.fabs(target_off-current_off) < step:
                target_off=random.random()
                #print(str(target_off))
        if current_off < target_off:
                current_off += step
        elif current_off > target_off:
                 current_off -= step
        
        if math.fabs(x_off_target-x_off) < step:
            x_off_target = random.random()
        
        if x_off < x_off_target:
            x_off+=step
        elif x_off > x_off_target:
            x_off-=step
       #generate7(rect.right/2, rect.right/10, renderer)
        #+random.random()*155
        #print(str(current_off))
        
        
        fn+=step#*0.05
        alpha = 0.5-math.fabs(fn-0.5)# - (random.random()*0.1)
        
        #if alpha>1:
        alpha -= int(alpha)
        
        alpha = math.fabs(alpha%1)
        
        #alpha *=0.5
        
        print(alpha)
        #alpha*=0.5
        #if alpha < 0.01:
        #    alpha = 0
        #if(alpha>1):
        #    alpha=1
            
        #alpha2 = alpha-0.75
        #if(alpha2<0):
        #    alpha2=0
        
        gen_fn = gen_fns[int(fn)%(len(gen_fns)-1)]
        #gen_fn_to = gen_fns[int(fn)%(len(gen_fns)-1)]
        
        #print(gen_fn)
        #print(gen_fn_to)
        gen_fn((rect.right/2+rect.right/8)+current_off*160, rect.right/10+150, renderer, alpha)
        #gen_fn_to((rect.right/2+rect.right/8)+current_off*60, rect.right/10+150+(x_off*100)+(random.random()*0), renderer, alpha*0.5)
        
        
        if txtr==1:
            renderer.present()
        else:
        #refresh only needed for sw/surface
            window.refresh()
    return 0

if __name__ == "__main__":
    sys.exit(run())