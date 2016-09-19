"""
Implementation of Binary Search Tree.
"""

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
    """
    BST
    """
    def __init__(self):
        self.root = None

    def insert(self, node: BSTreeNode):
        """
        insert a node to the tree
        """
        if self.root is None:
            self.root = node
        else:
            self.insert_node(self.root, node)

    def print_tree(self):
        """
        print the tree
        """
        self.print_subtree(self.root)

    def print_subtree(self, node: BSTreeNode, indent=0):
        """
        class method for printing tree
        """
        if node is not None:
            print(indent*' ' + str(node.value))
            self.print_subtree(node.left, indent+2)
            self.print_subtree(node.right, indent+2)
            
    def insert_num(self, num):
        """
        inserting element to the tree. creates a new node
        """
        self.insert(BSTreeNode(num))
            
    def insert_node(self, root: BSTreeNode, new: BSTreeNode):
        if root < new:
            if root.right is None:
                root.right = new
                new.previous = root
            else:
                self.insert_node(root.right, new)
        else: # new > old, assuming no equal
            if root.left is None:
                root.left = new
                new.previous = root
            else:
                self.insert_node(root.left, new)

    def find(self, num):
        """
        find node that contains the given value
        """
        curr = self.root
        while True:
            if curr.value == num:
                return curr
            elif curr.value < num:
                if curr.right is None:
                    raise Error('not found')
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    raise Error('not found')
                else:
                    curr = curr.left

    def delete(self, node: BSTreeNode):
        """
        delete existing node
        """
        if self.root == node:
            self.root = None
            return
            
        curr = self.root
        previous = None
        
        while True:
            if curr is None:
                raise Error('Not found!')
            
            if curr < node:
                previous = curr
                curr = curr.right
                left = False
            elif curr > node:
                previous = curr
                curr = curr.left
                left = True
            else:
                if curr.left is None:
                    curr = curr.right
                elif curr.right is None:
                    curr = curr.left
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
                break
                    
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


if __name__ == '__main__':
    t = BSTree()
    t.insert_num(1)
    t.insert_num(2)
    t.print_tree()
    x = t.find(2)
    print(x.value)
    t.delete(x)
    t.print_tree()
