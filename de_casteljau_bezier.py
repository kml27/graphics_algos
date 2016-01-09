#de casteljau bezier class

import interpolate


lerp = interpolate.linear_interpolate


class bezier_segment(object):
    def __init__(self):
        self.control_point=[0,0]
        self.end_point=[0,0]

class bezier(object):
    def __init__(self):
        self.segments = [bezier_segment(), bezier_segment()]
        
    def __len__(self):
        return len(self.segments)
        
    def add_segment(self):
        self.segments.append(bezier_segment())
        
    def modify_segment(self, segment_index, control_point=None, end_point=None):
        #todo: determine if segments[segment_index] can be referenced and updated by value, and verify segment.control_point = control_point would reference the passed control point
        #print end_point
        #print control_point
        #if segment index is oob or no point info to update return
        if segment_index >= len(self.segments) or (control_point is None and end_point is None):
            return
        
        if control_point is not None:
            self.segments[segment_index].control_point[0]=control_point[0]
            self.segments[segment_index].control_point[1]=control_point[1]
            
        if end_point is not None:
            self.segments[segment_index].end_point[0]=end_point[0]
            self.segments[segment_index].end_point[1]=end_point[1]
            
    def __getitem__(self, segment_index):
        #return by value or reference? for a better api, return by value, only allow modification of segments by the implementation
        return self.segments[segment_index]
    
    def __str__(self):
        #dont allow parallel, use range, does not follow PEP
        print_str = "S" + str(len(self.segments)) + "\n"
        for i in range(len(self.segments)):
            print_str += "C"+str(i)+": "
            #output segment end points and control points to stdout
            print_str += str(self.segments[i].control_point[0]) + ", " + str(self.segments[i].control_point[1]) + "\n"
            print_str+= "E"+str(i)+": "
            print_str += str(self.segments[i].end_point[0]) + ", " + str(self.segments[i].end_point[1]) + "\n"
        return print_str
            
    def solve(self, t, draw_lines=False, renderer= None, segment=0):
        number_of_segments = len(self.segments)-1
            #from 0 to len-1-1 for index
        #for i in range(number_of_segments):
                
        current_segment = self.segments[segment]
                
        #if i+1 < number_of_segments:
        next_segment = self.segments[segment+1]
        
        #could op by storing 1st derivative lines and derivatives deltas and just incrementing by delta along solution lines for 2nd derivative
        
        #these wont change, though t will
        #interpolate along end_point to control_point
        dx1=lerp((current_segment.end_point, current_segment.control_point), t)
        
        #print dx1
        #interpolate along control_point to control_point
        dx2=lerp((current_segment.control_point, next_segment.control_point), t)
        #print dx2
        #interpolate between next control_point and end_point
        dx3=lerp((next_segment.control_point, next_segment.end_point), t)
        #print dx3
        
        #interpolate between dx1,dx2, and dx2,dx3 to find the line of the first derivative
            
        dt_sub0 = lerp((dx1, dx2), t)
        
        dt_sub1 = lerp((dx2, dx3), t)
        
        if draw_lines:
            renderer.draw_line((dx1[0], dx1[1], dx2[0],dx2[1]),0x01FF0000)
            renderer.draw_line((dx2[0], dx2[1], dx3[0],dx3[1]),0x01FF0000)
            renderer.draw_line((dt_sub0[0], dt_sub0[1], dt_sub1[0], dt_sub1[1]), 0x0100FF080)
        
        #this is the 2nd derivative solution point at t        
        dt_prime = lerp((dt_sub0, dt_sub1), t)
        
        return dt_prime