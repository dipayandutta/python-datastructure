# -*- coding: utf-8 -*-

from collections import Counter

class Node(object):
    def __init__(self,value=None,next=None):
        self.value = value
        self.next  = next
        
class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def addNode(self,value):
        node = Node(value)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
        self.tail = node
        self.length += 1
        
    def printList(self):
        node = self.head
        while node:
            print node.value
            node = node.next
            
    def deleteNode(self,index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i += 1
        if i == index:
            if not prev:
                self.head = node.next
            else:
                prev.next = node.next
                
            self.length -= 1
    def removeDuplicate(self):
        prev = None
        node = self.head
        aux_dict = Counter()
        while node:
            value_here = node.value
            if aux_dict[value_here] == 0:
                aux_dict[value_here] = 1
            else:
                if prev == None:
                    self.head = node.next
                else:
                    prev.next = node.next
                self.length -= 1
            prev = node
            node = node.next
            
    def remove_dup_no_buf(self):
        node = self.hea
        while node:
            pivot = node.value
            pointer = node.next
            prev = node 
            while pointer:
                value_here = pointer.value
                if value_here == pivot:
                    prev.next = pointer.next
                    self.length -= 1
                prev = pointer
                pointer = pointer.next
            node =node.next 
            

def main():
    ll = LinkList()
    for i in range(1,10):
        ll.addNode(i)
        ll.addNode(i+1)
    print "Link list with duplicates"
    ll.printList()
    print "Length with duplicate items: ",ll.length
    ll.removeDuplicate()
    ll.printList()
    
if __name__ == '__main__':
    main()