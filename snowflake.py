from __future__ import division
import os, sys, math, random
import interpolate, rotation, translation
os.environ["PYSDL2_DLL_PATH"]="."

import sdl2, sdl2.ext

number=2

window_size = (800, 600)
clear_color = 0xFF000060

draw_color = 0x20D0D0F0


delta_t = 10
    

def get_center():
    return [window_size[0]*random.random(), window_size[1]*random.random()]

#def init_wind():
#    return random.random()<0.5

def init_snowflake_height():
    return int(window_size[1]*random.random()*.3+window_size[1]*0.075)
    
#height = init_snowflake_height()
#width = height*dimension_ratio

#subdivision_factor = 0.7

growth_rate = 4

tolerance= 1

#to choose a number of branches per snowflake
def init_number_of_branches():
    return int(3+random.random()*6)#12)

def init_subdivision_factor():
    return 0.7*random.random()
    
class snowflake(object):
    #def __init__(self, renderer):
    #    self.pos = get_center()
    #    mb_tree.root_value=0
        
    #    self.height = init_snowflake_height()
    def __init__(self, pos, growth_direction_vector, branches, subdivision_factor, renderer, draw_color):
        self.pos = pos
        self.branches = branches
        self.mb_tree = multibranch_tree()
        self.mb_tree.root_value=0 
        self.subdivision_factor = subdivision_factor
        self.growth_direction_vector = growth_direction_vector
        #self.height = height
        self.draw_color = draw_color
        
        self.t = 0
        self.delta_t=delta_t
        self.renderer=renderer
    
    def draw(self):
        self.mb_tree.root_value = self.subdivision_factor+self.delta_t*self.t*growth_rate
        self.t+=1
        self.draw_color+=0x01010100
        self.branch(self.pos, self.mb_tree.root_value, self.subdivision_factor, self.branches, self.growth_direction_vector, self.renderer, self.mb_tree, self.draw_color)
        
        if self.t > 1*self.growth_direction_vector[0]:
            self.branches= init_number_of_branches()
            self.t=0
            self.mb_tree = multibranch_tree()
            #self.renderer.clear(clear_color)
            self.pos = get_center()
            self.draw_color=draw_color
#9.21749335368
#6.6250543276
            print("branches"+str(self.branches))
            
    def branch(self, start_pos, branch_development_factor, subdivision_factor, branches, growth_direction_vector, renderer, parent_node, color):
    
        parent_length = growth_direction_vector[0]
        initial_angle = growth_direction_vector[1]
    
    #print(parent_length)
    
    #could be defined relationship between the number of subdivisions and unit length of the object in ratio to the screen resolutions ratio to the parent length
    
    #if parent_length*subdivision_factor < 2:#growth_rate:
        #print('pruning small branches')
    #    return
    
        number_subdivisions = int(1/subdivision_factor)
    #print(number_subdivisions)
    
        create_branch = False
    #for i in range(0, number_subdivisions):
    #    if math.fabs(leaf_development_factor - i*subdivision_factor) < growth_rate:
    #        create_branch = True
    
        if branch_development_factor >= subdivision_factor:
                create_branch = True
    
        if create_branch:
            branch_development_factor=0
        #fraction of radians per split/fork
            angle_of_rotation_per_branch = 2*math.pi/branches
        #print(angle_of_rotation_per_branch)
                
        
        
            for branch in range(int(-branches/2), (int(branches/2)+1)):
            
                new_branch = parent_node.grow(parent_node, branch)
                angle_of_rotation = (branch*angle_of_rotation_per_branch)+initial_angle
                growth_direction_vector = (parent_length*subdivision_factor, angle_of_rotation)
                
                self.grow_leaf(renderer, start_pos, growth_direction_vector, new_branch, branches, subdivision_factor, color)
            #envelope should control growth rate
                new_branch.root_value += 0.01
            
        
    #else:
    #    for branch in range(int(-branches/2), (int(branches/2)+1)):
    #    if branch!=0:
    #        grow_leaf(renderer, start_pos, growth_direction_vector, new_branch, branches, subdivision_factor, color)

    def grow_leaf(self, renderer, start_pos, growth_direction_vector, parent_node, branches, subdivision_factor, color):
    
        leaf_development_factor = parent_node.root_value
    #print(leaf_development_factor)
    
    #growth direction vector (magnitude, rotation)
        if growth_direction_vector[0] < tolerance:#growth_rate:#== 0:
            return
    
        if leaf_development_factor >= 1:
        #print('saturating leaf development')
            leaf_development_factor = 1
    
        wind_step = 0.00000
    
        if math.fabs(self.grow_leaf.wind_target-self.grow_leaf.toward_wind) < wind_step:
            self.grow_leaf.wind_target = (random.random()*math.pi/8)-math.pi/16
        #print(grow_leaf.wind_target)
    
        if self.grow_leaf.toward_wind < self.grow_leaf.wind_target:
            self.grow_leaf.toward_wind += wind_step
        elif self.grow_leaf.toward_wind > self.grow_leaf.wind_target:
            self.grow_leaf.toward_wind -= wind_step
    
    #print(grow_leaf.toward_wind)
       
        rotated_point = translation.translate(start_pos, rotation.rotate((growth_direction_vector[0], 0), growth_direction_vector[1]+self.grow_leaf.toward_wind))
    
        center_line = (int(start_pos[0]), int(start_pos[1]), int(rotated_point[0]), int(rotated_point[1]))
        
    #center_line = (int(start_pos[0]), int(start_pos[1]), int(start_pos[0]), int(start_pos[1]-height))

    #renderer.draw_line(center_line, 0xFFFF0000)
        interpolator = interpolate.linear_interpolate
    
        number_subdivisions = int(1/subdivision_factor)
    
    #for i in range(1, number_subdivisions):
    #    if (i*subdivision_factor - leaf_development_factor) < growth_rate:
    #        developed_line = interpolator(center_line, i*subdivision_factor)
    #        branch((developed_line[2], developed_line[3]), leaf_development_factor, subdivision_factor, branches, growth_direction_vector, renderer, parent_node, color- 0x102000)
    
    
        developed_line = interpolator(center_line, leaf_development_factor)
    
        #if developed_line[0]-developed_line[2] + developed_line[1]-developed_line[3] == 0:
        renderer.draw_line(developed_line, color)
    #draw_color = color
    #use leaf envelope to decide when to branch and modulate interpolation based on leaf_development_factor
    
    #subdivision_length = (center_line[3] - center_line[1]) * subdivision_factor
    #current_length = developed_line[3] - developed_line[1]
    #if current_length >= subdivision_length:
    
    #if color > 0x102000:
    #    color = color - 0x102000
    #else:
    #    color = 0xFFFF0000
    #create branches
        self.branch((developed_line[2], developed_line[3]), leaf_development_factor, subdivision_factor, branches, growth_direction_vector, renderer, parent_node, color- 0x404000)
    grow_leaf.wind_target=0
    grow_leaf.toward_wind=0
    


class multibranch_tree(object):
    def __init__(self):
        self.root = []
        self.root_value = 0
        self.hash = {}


    def grow(self, node, branch_id=None):
        
        if node is None:
            branch = root
        else:
            branch = node.root

        #print(branch)
        new_branch = None
        
        try:
            self.hash[branch_id]
        except Exception as e:
            #print("adding key")
            new_branch = multibranch_tree()
            self.hash[branch_id]=len(branch)
            branch.append(new_branch)
            
            
        else:
            new_branch = branch[self.hash[branch_id]]
            
        return new_branch
    
    


#class envelope_node(object):
#    delay =0#also used for sustain
#    attack =1#add
#    decay = 2#subtract

#    def __init__(self, type, duration, target):
#        self.type = type
        #x
#        self.duration = duration
        #y, target ignored in delay/sustain types
#        self.target = target

#delay, attack, sustain, decay

#channels = [ "color",
#             "development"]#,
             #""]

#use a generator instead?
#class growth_envelope(object):
#    def __init(self):
        #self.position=0
    
#        self.channel = "development"
#        self.envelope = []
    
#    def add_node(self, node):
#        envelope.append(node)
    
    
    
#    def get_node(self, time):
        
#        if len(envelope)==0:
#            return None
        
#        envelope_time = 0
#        position = 0
#        while(time>=envelope_time):
#            envelope_time += envelope[position].duration
#            if position < len(envelope):
#                position +=1
#            else:
#                break
        
#        return envelope[position]

#    def get_duration():
#        duration =0
#        for node in self.envelope:
#            duration += node.duration
        
#        return duration
        
    #def set_duration(duration):
    #    self.duration = duration
        


    
    

def run():

    branches= init_number_of_branches()

    #9.21749335368
    #6.6250543276
    print("branches"+str(branches))

    sdl2.ext.init()
    window = sdl2.ext.Window("Snowflake", window_size)
    
    renderer = sdl2.ext.Renderer(window)
    
    sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    
    renderer.blendmode = sdl2.SDL_BLENDMODE_BLEND
    
    window.show()
    renderer.clear(clear_color)
    
    #display calculations (asthetics of display)
    center = window_size[0]/2
    
    screen_third = (window_size[1]/3)
    
    lower_third_line = screen_third*2
    
    #start position of the drawing offset to asthetic
    
    #number of multifurcations
    
    
    #add random deviations to repartition the radial sections more organically
    
    #because python global
    
    snowflakes = []
    for i in range(number):
        sf = snowflake(get_center(), (init_snowflake_height(), random.random()*2*math.pi), init_number_of_branches(), init_subdivision_factor(), renderer, draw_color)
        snowflakes.append(sf)
    
    #for y in range(int(lower_third_line), window_size[1]):
    #    renderer.draw_line((0,y,window_size[0],y), 0xA02020A0)
    
    running=True
    while(running):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running=False
        
        for sf in snowflakes:
            sf.draw()
        
        #sdl2.SDL_Delay(200)

        renderer.blendmode = sdl2.SDL_BLENDMODE_MOD
        renderer.present()
        renderer.blendmode = sdl2.SDL_BLENDMODE_BLEND
    
        renderer.present()
        
    return 0
    
if __name__ == "__main__":
    sys.exit(run())