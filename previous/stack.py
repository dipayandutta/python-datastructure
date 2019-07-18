# -*- coding: utf-8 -*-

class Stack(list):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def push(self,items):
        self.items.append(items)
        
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise Exception ('Stack is Empty')
    
    def peek(self):
        print "Last Entered Element in stack"
        print self.items[-1]
        
    def size(self):
        print "Current Size of the stack"
        print len(self.items)
        
    def elements(self):
        print "Items in the Stack"
        for element in self.items:
            print element
        
def main():
    stack = Stack()
    stack.push(12)
    stack.push(13)
    stack.push(14)
    stack.elements()
    stack.size()
    stack.peek()
    stack.pop()
    stack.size()
    stack.peek()
    
if __name__ == '__main__':
    main()