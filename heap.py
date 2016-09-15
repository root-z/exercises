from math import floor

class heap:
    def __init__(self, elems = []):
        self.__elems = elems

    def get(index):
        return self.__elems[index]

    def parent(index):
        return self.__elems[floor(index)]

    def left(index):
        return self.__elems[2*index]

    def right(index):
        return self.__elems[2*index+1]
