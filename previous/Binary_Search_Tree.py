# -*- coding: utf-8 -*-

class Node(object):
    
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self,data):
        
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                    
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                    
        else:
            self.data = data
            
    def find(self,val):
        
        if val < self.data:
            if self.left is None:
                return str(val)+" Not Found in the Binary Tree"
            return self.left.find(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + "Not Found"
            return self.right.find(val)
            
        else:
            print "{} found ".format(self.data)
            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print self.data
        if self.right:
            self.right.PrintTree()
            
root = Node(12)
root.insert(5)
root.insert(14)
root.insert(10)
root.PrintTree()

print root.find(3)
print root.find(5)