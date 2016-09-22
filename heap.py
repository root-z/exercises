from math import floor
import copy

class Heap:
    def __init__(self, elems = []):
        self.__elems = copy.copy(elems)
        for i in range(self.heap_size()//2 - 1, -1, -1):
            self.max_heapify(i)
            
    def __str__(self):
        return str(self.__elems)
            
    def get(self, index):
        '''
        get element from array
        '''
        return self.__elems[index]

    def set(self, index, value):
        '''
        set index
        '''
        self.__elems[index] = value
        
    def parent(self, index):
        '''
        get parent node
        '''
        return self.__elems[floor(index)]

    def left_index(self, index):
        return 2*index
    
    def left_child(self, index):
        '''
        left child
        '''
        return self.__elems[2*index]

    def right_index(self, index):
        return 2*index + 1
    
    def right_child(self, index):
        '''
        right child
        '''
        return self.__elems[2*index+1]

    def heap_size(self):
        '''
        size of the heap
        '''
        return len(self.__elems)
    
    def max_heapify(self, i):
        '''
        maintaining the heap property
        '''
        l = self.left_index(i)
        r = self.right_index(i)
        if l < self.heap_size() and self.get(l) > self.get(i):
            largest = l
        else:
            largest = i
        if r < self.heap_size() and self.get(r) > self.get(largest):
            largest = r
        if largest != i:
            tmp = self.get(i)
            self.set(i, self.get(largest))
            self.set(largest, tmp)
            self.max_heapify(largest)

if __name__=='__main__':
    h = Heap([5,3,2,4,1])
    print(h)
    

            
        
