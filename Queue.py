# -*- coding: utf-8 -*-

class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
        
    def peek(self):
        if not self.isEmpty():
            print self.items[-1]
        else:
            raise Exception ("Queue is empty")
            
    def size(self):
        print "Length of the queue{0}".format(len(self.items))
        
    def elements(self):
        print "Elements of the queue"
        for element in self.items:
            print element
            
def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(10)
    
    queue.size()
    queue.elements()
    
    queue.peek()
    
    
if __name__ == '__main__':
    main()