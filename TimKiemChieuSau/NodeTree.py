from collections import defaultdict
from webbrowser import get
class NodeTree:
    "Node tree bieu dein moi code voi ten"
    def __init__(self,name='',cost=0,parent=None) -> None:
        self.name=name
        self.cost=cost
        self.parent=parent
    def display(self):
        print(str(self.name)+'\t')
    def  getName(self):
        return str(self.name)
    def __eq__(self, other):
        return self.name==other.name
    def __lt__(self, other):
        return self.cost<other.cost
    
from collections import defaultdict
from math import fabs
from pty import CHILD
from webbrowser import get
from NodeTree import *
from queue import Empty, PriorityQueue
class TreeSearch:
    def __init__(self, data=defaultdict(list)):
        self.data=data
    def CreateTree(self):
        self.data['A']=[NodeTree('B',1),NodeTree('C',1),NodeTree('D',1)]
        self.data['B'] = [NodeTree('E', 1), NodeTree('F', 1)]
        self.data['C'] = [NodeTree('G', 1), NodeTree('H', 1)]
        self.data['D'] = [NodeTree('I', 1), NodeTree('J', 1)]
        self.data['F'] = [NodeTree('K', 1), NodeTree('L', 1), NodeTree('M', 1)]
        self.data['H'] = [NodeTree('N', 1), NodeTree('O', 1)]
    def printPath(self, path=[]):
        '''Chuỗi thể hiển đường đi'''
        strpath='Đường đi từ {0} đến {1}: '. format(path[0].name,
    path[len(path)-1].name)
        for n in path:
            strpath+='{0} -> '.format(n.name)
        strpath=strpath[:len(strpath)-3]
        return strpath
    def checkInList(self,v,path):
        return v in path
    def BFS(self,start=NodeTree(),end=NodeTree()):
            lst=PriorityQueue()
            path=[]
            kt=False
            lst.put(start)
            while not lst.empty():
                t=lst.get()
                path.append(t)
                if t==end:
                    kt=True
                    break
                for v in self.data[t.name]:
                    if not self.checkInList(v,path) and not self.checkInList(v,lst.queue):
                        v.parent=t
                        lst.put(v)
            return kt,path

# a=NodeTree()
# a.CreateTree()


