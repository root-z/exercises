class BSTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

    def __eq__(self, other):
        return self.value == other.value
        
    def __lt__(self, other):
        return self.value < other.value

class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            self.insertNode(self.root, node)

    def insertNum(self, num):
        self.insert(BSTreeNode(num))
            
    def insertNode(self, root: BSTreeNode, new: BSTreeNode):
        if root < new:
            if root.right is None:
                root.right = new
                new.previous = root
            else:
                self.insertNode(root.right, new)
        else: # new > old, assuming no equal
            if root.left is None:
                root.left = new
                new.previous = root
            else:
                self.insertNode(root.left, new)

    def find(self, num):
        curr = self.root
        while True:
            if curr.value == num:
                return curr
            else if curr.value < num:
                if curr.right is None:
                    raise Error('not found')
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    raise Error('not found')
                else:
                    curr = curr.left

    def delete(self, node):
        if self.root == node:
            self.root = None
        
        curr = self.root
        previous = None
        
        while True:
            if curr < node:
                curr = curr.right
                previous = curr
                left = False
            else if curr > node:
                curr = curr.left
                previous = curr
                left = True
            else:
                if curr.left is None:
                    curr = curr.right
                else if curr.right is None:
                    curr = curr.right
                else: # have both left and right
                    last_left, last_previous = find_last_left(curr.right)
                    if last_left == curr.right:
                        curr.right.left = curr.left
                        curr = curr.right
                    else:
                        last_previous.left = last_left.right
                        last_left.right = curr.right
                        last_left.left = curr.left
                        curr = last_left
                                    
                if left:
                    previous.left = curr
                else:
                    previous.right = curr

def find_last_left(node):
    curr = node
    previous = None
    while True:
        if curr.left is None:
            return (curr, previous)
        else:
            previous = curr
            curr = curr.left
                    
t = BSTree()
t.insertNum(1)
t.insertNum(2)
                
