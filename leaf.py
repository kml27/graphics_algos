from __future__ import division
import os, sys, math
import interpolate, rotation, translation
os.environ["PYSDL2_DLL_PATH"]="."

import sdl2, sdl2.ext

window_size = (800, 600)
clear_color = 0x00000000

draw_color = 0x80A0A020

dim_ratio = 0.75

height = window_size[1]*0.75
width = height*dim_ratio

subdivision_factor = 0.5


#class simple_hash(Dict):
#    def __getitem():




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
    
    

class envelope_node(object):
    delay =0#also used for sustain
    attack =1#add
    decay = 2#subtract

    def __init__(self, type, duration, target):
        self.type = type
        #x
        self.duration = duration
        #y, target ignored in delay/sustain types
        self.target = target

#delay, attack, sustain, decay

channels = [ "color",
             "development"]#,
             #""]

#use a generator instead?
class growth_envelope(object):
    def __init(self):
        #self.position=0
    
        self.channel = "development"
        self.envelope = []
    
    def add_node(self, node):
        envelope.append(node)
    
    
    
    def get_node(self, time):
        
        if len(envelope)==0:
            return None
        
        envelope_time = 0
        position = 0
        while(time>=envelope_time):
            envelope_time += envelope[position].duration
            if position < len(envelope):
                position +=1
            else:
                break
        
        return envelope[position]

    def get_duration():
        duration =0
        for node in self.envelope:
            duration += node.duration
        
        return duration
        
    #def set_duration(duration):
    #    self.duration = duration
        
class leaf(object):
    def __init__(self, center_x, height, dim_ratio, branches, leaf_envelope):
        self.center= center_x
        self.height=height
        self.width=height*dim_ratio
        self.x=0
        self.y=0
        self.growth_envelope = leaf_envelope

def branch(start_pos, leaf_development_factor, subdivision_factor, branches, initial_angle, renderer, parent_node, color):
    
    if leaf_development_factor >= subdivision_factor:
        branch_development_factor=0
        #fraction of radians per split/fork
        angle_of_rotation_per_branch = math.pi/branches
        #print(angle_of_rotation_per_branch)
                
        
        for branch in range(int(-branches/2), (int(branches/2)+1)):
            if branch != 0:
                new_branch = parent_node.grow(parent_node, branch)
                angle_of_rotation = (branch*angle_of_rotation_per_branch)+initial_angle
                #print(angle_of_rotation)
                growth_direction_vector = (height*subdivision_factor, angle_of_rotation)
                
                grow_leaf(renderer, start_pos, growth_direction_vector, new_branch, branches, subdivision_factor, color)
                #envelope should control growth rate
                new_branch.root_value += 0.001
            
        

def grow_leaf(renderer, start_pos, growth_direction_vector, parent_node, branches, subdivision_factor, color):
    
    leaf_development_factor = parent_node.root_value
    #print(leaf_development_factor)
    #growth direction vector (magnitude, rotation)
    if growth_direction_vector[0] == 0 or leaf_development_factor >= 1:
        return
    rotated_point = translation.translate(start_pos, rotation.rotate((growth_direction_vector[0], 0), growth_direction_vector[1]))
    
    center_line = (int(start_pos[0]), int(start_pos[1]), int(rotated_point[0]), int(rotated_point[1]))
        
    #center_line = (int(start_pos[0]), int(start_pos[1]), int(start_pos[0]), int(start_pos[1]-height))

    #renderer.draw_line(center_line, 0xFFFF0000)
    interpolator = interpolate.linear_interpolate
    developed_line = interpolator(center_line, leaf_development_factor)
    
    
    renderer.draw_line(developed_line, color)
    #draw_color = color
    #use leaf envelope to decide when to branch and modulate interpolation based on leaf_development_factor
    
    subdivision_length=(center_line[3] - center_line[1])*subdivision_factor
    current_length = developed_line[3] - developed_line[1]
    
    #if current_length >= subdivision_length:
    #create branches
    branch((developed_line[2], developed_line[3]), leaf_development_factor, subdivision_factor, branches, growth_direction_vector[1], renderer, parent_node, color - 0x102000)
    
    
    
    

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Leaf", window_size)
    
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
    start_pos = (center, lower_third_line + height/3)
    
    #number of multifurcations
    branches= 6
    
    mb_tree = multibranch_tree()
    
    
    
    #add random deviations to repartition the radial sections more organically
    
    
    delta_t = 0.01
    
    t=0
    
    growth_rate = 0.01
    
    
    running=True
    while(running):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type==sdl2.SDL_QUIT or (event.type==sdl2.SDL_KEYDOWN and event.key.keysym.sym==sdl2.SDLK_ESCAPE):
                running=False
        
        #leaf_development_factor 
        mb_tree.root_value = delta_t*t*growth_rate    
        
        t+=1
        
        growth_direction_vector = (height, math.pi/2)
        
        grow_leaf(renderer, start_pos, growth_direction_vector, mb_tree, branches, subdivision_factor, draw_color)
        
        renderer.present()
        
    return 0
    
if __name__ == "__main__":
    sys.exit(run())