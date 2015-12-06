from __future__ import division

def translate(points, offsets, results_interleaved=True):
    #print points
    #print offsets
    try:
        translated = []
        #[point in points in offsets]
        #print len(points)
        for i in range(0, len(points)):
            #print 'translating' 
            point = points[i]
            offset = offsets[i]
            if results_interleaved:
                translated.append(int(point[0]+offset[0]))
                translated.append(int(point[1]+offset[1]))
            else:
                translated.append((int(point[0]+offset[0]), int(point[1]+offset[1])))
            
            #print str(translated)
    
    except Exception as e:
        print e.message
    
    #print "translated" + str(translated)
    if len(translated)>0:
        return translated
    else:
        return (int(points[0]+offsets[0]), int(points[1]+offsets[1]))