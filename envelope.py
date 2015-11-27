from __future__ import division
import interpolate
#dont need inspect
import sys

class envelope_node(object):
    #delay  = 0#also used for sustain
    #attack = 1#add
    #decay  = 2#subtract

    def __init__(self, duration, target, prev_target, fixed_step=0.01):
        self.type = type
        #x
        self.duration = duration
        #y, target ignored in delay/sustain types
        self.target = target
        self.prev_target=prev_target
        self.cur = prev_target
        self.fixed_step = fixed_step

    def get_value(self, time):#, prev_target):
        #print(time, self.target)
        start = self.prev_target
        end = self.target
        
        factor = (time+1)/self.duration
        
        if type(time) is float:
            print("warning: you better know what you're doing " + str(__file__) + " line " + str(sys._getframe().f_back.f_lineno) + " comment out this line")
            factor = time
        
        return interpolate.linear_interpolate((start, end), factor, type=float)
        
    def get_fixed_step(self):
        self.cur += self.fixed_step
        return interpolate.linear_interpolate((self.prev_target, self.target), self.fixed_step)
#delay, attack, sustain, decay

#channels = [ "color",
#             "development"]#,
             #""]

#use a generator instead?
class envelope(object):
    def __init__(self):
        #self.position=0
    
#        self.channel = "development"
        self.envelope = []
    
    def add_node(self, node):
        if type(node) is envelope_node:
            self.envelope.append(node)
        elif type(node) is tuple:
            prev_target = 0
            if len(self.envelope)>0:
                prev_target = self.envelope[len(self.envelope)-1].target
            self.envelope.append(envelope_node(node[0], node[1], prev_target))
    
    def get_node(self, time):
        
        if len(self.envelope)==0 or time < 0:
            return None
        
        envelope_time = 0
        position = 0
        while(time>=envelope_time):
            if position < len(self.envelope):
                envelope_time += self.envelope[position].duration
                position +=1
            else:
                return None
        
        return (position-1, self.envelope[position-1])

    def get_duration(self):
        duration =0
        for node in self.envelope:
            duration += node.duration
        
        return duration
        

    def get_value(self, time):
        #lookup the node for this time
        #print('get_node '+str(time))
        node = self.get_node(time)
        #if there is one
        if node is not None:
            prev_time = 0
            
            for i in range(0, node[0]):
                prev_time += self.envelope[i].duration
                
            
            #print(prev_time)
            
            return node[1].get_value(time-prev_time)

    #def set_duration(duration):
    #    self.duration = duration
