# -*- coding: utf-8 -*-

# A deque is a doble-ended queue , which can roughly be seen as an union of stack and queue

class Dqeue(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
        
    def addFront(self,item):
        self.items.append(item)
        
    def addRead(self,item):
        self.items.insert(0,item)
        
    def removeFront(self):
        return self.items.pop()
        
    def removeRear(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
        
    def __repr__(self):
        return '{}'.format(self.items)
        
    def elements(self):
        print "Elements in the dqeue"
        for element in self.items:
            print element
        
def main():
    dq = Dqeue()
    dq.addFront(1)
    dq.addFront(23)
    dq.addRead(30)
    dq.elements()
    dq.removeFront()
    dq.removeRear()
    dq.elements()
    
    
if __name__ == '__main__':
    main()