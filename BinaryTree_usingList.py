# -*- coding: utf-8 -*-

'''
    Binary Tree = A Binary Tree are tree data structure where each node has at least two nodes , left child and right child.
    The degree of every node is maximum two.
    A Tree with n nodes has exactly n-1 bracnhes or degree.
    
    Graph = A graph is an abstract network , consisting of nodes (V) connected by edges (E) 
    G = (V,E)
    
    Example , 
    Some graph can be simply  represented by the node set V = {a,b,c,d}
    edge set = E = {(a,b),(b,c),(c,d),(d,a)}
    
    uniderected = If a graph has a no direction .
    
    Degree in a Node = The number of unidirected edges incident on a node is called degree . 
    isolated = A Zero degree graphs are called isolated.
    
    Path = A path in G is a subgraph where the edges connect the nodes in a sequence , without revisitng the node .
    
    Walk = A walk is an alternative sequence of nodes and edges that allows modes and edges to be visited multiple times.
    
    cycle = A cycle is a like a path except that the last edge links the last node the first.
    
    length = The length of a path or walk is the value given by its edge count.
    
    traversal = A traversal is a walk through all the connected components of a graph.
    
    Forest = A forest is a cycle-free graph.
    
'''

def BinaryTree(r):
    return [r,[],[]]
    
def insertLeft(root , newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
    
    
def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
    
def getRootVal(root):
    return root[0]
    
def setRootVal(root,newVal):
    root[0] = newVal
    
def getLeftChild(root):
    return root[1]
    
def getRightChild(root):
    return root[2]
    
def main():
    r = BinaryTree(3)
    insertLeft(r,4)
    insertLeft(r,5)
    insertRight(r,6)
    insertRight(r,7)
    print getRootVal(r)
    print getLeftChild(r)
    print getRightChild(r)
    
if __name__ == '__main__':
    main()



