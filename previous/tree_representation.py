# -*- coding: utf-8 -*-

Tree = ['a',['b',['1','2']],['c',['3','4']]]

print "Root Node ==> ",Tree[0] # The Root Node
print "First Child Node ==> ",Tree[1][0] # Child Node
print "Second Child Node ==>",Tree[2][0] # Second Child Node

print "Two child Node of Parent Node {0}".format(Tree[1][0])
print "{0} {1}".format(Tree[1][1][0],Tree[1][1][1])

print "Two Child Node of Parent Node {0}".format(Tree[2][0])
print "{0} {1}".format(Tree[2][1][0],Tree[2][1][1])