from inspect import stack
from os import lstat, system
from queue import PriorityQueue
from collections import defaultdict
from tabnanny import check
from turtle import pos


class NodeTree:
    def __init__(self, name=' ', cost=0,depth=0, parent=None):
        self.name = name
        self.cost = cost
        self.parent=parent
        self.depth = 0
        
    def display(self):
        print(str(self.name)+'\t')
    def getName(self):
        return str(self.name)
    def __eq__(self, other):
        return self.name==other.name
    def __lt__(self, other):
        return self.cost<other.cost


class TreeSearch:
    def __init__(self, data=defaultdict(list)):
        self.data = data

    def CreateTree(self):
        self.data['A'] = [NodeTree('B', 1,1), NodeTree('C', 1,1), NodeTree('D', 1,1)]
        self.data['B'] = [NodeTree('E', 1,2), NodeTree('F', 1,2)]
        self.data['C'] = [NodeTree('G', 1,2), NodeTree('H', 1,2)]
        self.data['D'] = [NodeTree('I', 1,2), NodeTree('J', 1,2)]
        self.data['F'] = [NodeTree('K', 1,3), NodeTree('L', 1,3), NodeTree('M', 1,3)]
        self.data['H'] = [NodeTree('N', 1,3), NodeTree('O', 1,3)]

    def printPath(self, path=[]):
        strpath = 'Đường đi từ {0} đến {1}: '. format(path[0].name,
                                                      path[len(path)-1].name)
        for n in path:
            strpath += '{0} ->'.format(n.name)
        strpath = strpath[:len(strpath)-3]
        return strpath
    
    def checkInList(self,v,path):
        return v in path

    def BFS(self, start=NodeTree(), end=NodeTree()):
        lst = []
        path = []
        kt = False
        lst.append(start)
        while len(lst)>0:
            t = lst.pop(0)
            path.append(t)

            if t == end:
                kt = True
                break
            for v in self.data[t.name]:
                if not self.checkInList(v, path) and not self.checkInList(v, lst):
                    v.parent = t
                    lst.append(v)
        return kt, path
    
    
    def DFS(self,start = NodeTree(),end = NodeTree()):
        lst=[]
        path=[]
        lst.append(start)
        kt= True
        while True:
            if len(lst) == 0:
                kt = False
                break
            t = lst.pop(0)
            path.append(t)
            if t == end:
                kt=True
                break
            pos = 0
            for v in self.data[t.name]:
                if not self.checkInList(v, path) and not self.checkInList(v, lst):
                    v.parent = t
                    lst.insert(pos,v)
                    pos +=1
        return kt,path
    
    def DFS_Limitted(self, start=NodeTree(), end=NodeTree(), maxDepth=0):
        lst=[]
        path=[]
        lst.append(start)
        # depth = 0
        kt =False
        while True:
            if len(lst) == 0:
                kt=False
                print('Len stack =0')
                break
            t=lst.pop(0)
            path.append(t)
            
            if t==end:
                kt=True
                break
            pos = 0
            if t.depth < maxDepth:
                for v in self.data[t.name]:
                    if v not in path and v not in lst:
                        if v.depth < maxDepth:
                            v.parent = t
                            lst.insert(pos, v)
                            pos +=1
                    t.depth+=1
            else:
                kt=False
                print('depth={0}'.format(depth))
                break
        return kt, path
    
    def printTree(self):
        print('Đường đi từ A đến O: ')
        for node in self.data:
            str = node + ': '
            for leaf in self.data[node]:
                str += '{0} -> '.format(leaf.name)
            str=str[:len(str)-3]
            print(str)
            
tree = TreeSearch()
tree.CreateTree()

ans = True
while ans:
    print ("""
    ===========================
    1.Tìm kiếm theo chiều rộng
    2.Tìm kiếm theo chiều sâu
    3.Tìm kiếm sâu dần
    4.Thoát
    ===========================
    """)
    ans=input("Chon chuc nang: ") 
    if ans=="1": 
        system('cls')
        print("\nTìm kiếm theo chiều rộng")
        print("=============================")
        print("Cấu trúc của cây: ")
        tree.printTree()
        print("=============================")
        start = input('Nhập đỉnh bắt đầu: ')   
        end = input('Nhập đỉnh kết thúc: ')
        kt, path = tree.BFS(start = NodeTree(start), end = NodeTree(end))
        if kt:
            print(tree.printPath(path))
        else:
            print('Không tìm thấy!')
    elif ans=="2":
        system('cls')
        print("\nTìm kiếm theo chiều sâu")
        print("=============================")
        print("Cấu trúc của cây: ")
        tree.printTree()
        print("=============================")
        start = input('Nhập đỉnh bắt đầu: ')   
        end = input('Nhập đỉnh kết thúc: ')
        kt, path = tree.DFS(start = NodeTree(start), end = NodeTree(end))
        if kt:
            print(tree.printPath(path))
        else:
            print('Không tìm thấy!')
    elif ans=="3":
        system('cls')
        print("\nTìm kiếm sâu dần")
        print("=============================")
        print("Cấu trúc của cây: ")
        tree.printTree()
        print("=============================")
        start = input('Nhập đỉnh bắt đầu: ')   
        end = input('Nhập đỉnh kết thúc: ')
        depth = int(input('Nhập giới hạn độ sâu: '))
        kt, path = tree.DFS_Limitted(start = NodeTree(start), end = NodeTree(end), maxDepth = depth)
        if kt:
            print(tree.printPath(path))
        else:
            print('Không tìm thấy!')
    elif ans=="4":
        print("\n Thoát chương trình") 
        exit()
    else:
        print("\n Not Valid Choice Try again") 

