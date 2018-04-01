# -*- coding: utf-8 -*-

class BT(object):
    
    def __init__(self,value):
        self.value = value
        self.left  = None
        self.right = None
        
    def is_leaf(self):
        
        return self.left is None and self.right is None
        
    def insert_left(self,new_node):
        if not self.left:
            self.left = BT(new_node)
        else:
            t = BT(self.left)
            t.left = new_node
            self.left = t
            
    def insert_right (self,new_node):
        if not self.right:
            self.right = BT(new_node)
        else:
            t = BT(self.right)
            t.right = new_node
            self.right = t
    def __repr__(self):
        return '{}'.format(self.value)
        
    
def test_BT():
    
    tree = BT(1)
    tree.insert_left(2)
    tree.insert_right(3)
    
    tree.left().insert_left(4)
    tree.left().insert_right(5)
    
    tree.right().insert_left(6)
    tree.right().insert_right(7)
    
    print tree.right().right()
    
    print tree.right().is_leaf()
    
if __name__ == '__main__':
    test_BT()