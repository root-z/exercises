from math import floor

class heap:
    def __init__(self, elems = []):
        self.__elems = elems

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

    def left(self, index):
        '''
        left child
        '''
        return self.__elems[2*index]

    def right(self, index):
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
        l = left(i)
        r = right(i)
        if l <= self.heap_size() and self.get(l) > self.get(i):
            largest = l
        else:
            largest = i
        if r <= self.heap_size() and self.get(r) > self.get(largest):
            largest = r
        if largest != i:
            tmp = self.get(i)
            self.set(i, self.get(largest))
            self.set(largest, tmp)
            self.max_heapify(largest)


            
        
