import os, sys
os.environ["PYSDL2_DLL_PATH"]="."

import sdl2, sdl2.ext
from sdl2.ext.common import series_product

from sdl2.ext import MemoryView

from array import array

dims = [3,3,3]

#(self, source, itemsize, strides, getfunc=None, setfunc=None,
#                 srcsize=None)

class ndim_array(MemoryView):
    def __init__(self, n_elements, itemsize):
        
        __super(array.array('c', n_elements*itemsize), itemsize )
        
    def getfunc(start, end):
        return self._source[start:end]
    
    def setfunc(start, end, value):
        self._source[start:end] = value
        
initializer = []

for i in range(series_product(dims)):
    initializer.append("{0}".format(str(i).zfill(3)))

initializer = "".join(initializer)

print initializer

src = array('c', initializer)
itemsize = src.itemsize

mv = MemoryView(src, 3, dims)

print mv

for i in range(dims[0]):
    for j in range(dims[1]):
        for k in range(dims[2]):
            #print "k: {0}".format(k)
            id = [str(i),str(j),str(k)]
            print id
            k_component = k*dims[0]*dims[1]
            j_component = j*dims[1]
            
            #print k_component
            #print j_component
            index = i + j_component + k_component 
            print "Index: {0}".format(index)
            mv[index] = array('c', id)
            
#print mv

print "----------"

for i in range(dims[0]):
    for j in range(dims[1]):
        for k in range(dims[2]):
            id = [str(i),str(j),str(k)]
            print "".join(id)
            #print mv[i]
            #print mv[i][j]
            print mv[i][j][k].tostring()
            print id==mv[i][j][k]