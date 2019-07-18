# -*- coding: utf-8 -*-

class Node(object):
    
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
    def PrintTree(self):
        print self.data 
        
def main():
    root = Node(10)
    root.PrintTree()
    
if __name__ == '__main__':
    main()