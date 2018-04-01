# -*- coding: utf-8 -*-


class SimpleTree(object):
    def __init__(self,value=None,children=None):
        self.children = children or []
        self.value = value
        
    def __repr__(self,level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
        
        
def main():
    st = SimpleTree('a',[SimpleTree('b',[SimpleTree('1'),SimpleTree('2')]),SimpleTree('c',[SimpleTree('3'),SimpleTree('4')] ) ])
    print st
    
if __name__ == '__main__':
    main()