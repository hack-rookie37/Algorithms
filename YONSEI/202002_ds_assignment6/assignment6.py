import math, sys

################ DO NOT modify this code ######################
class PriorityQueue:
    def __init__(self):
        self.heapArray = [(0,0)]
        self.currentSize = 0

    def buildHeap(self,alist):
        self.currentSize = len(alist)
        self.heapArray = [(0,0)]
        for i in alist:
            self.heapArray.append(i)
        i = len(alist) // 2            
        while (i > 0):
            self.percDown(i)
            i = i - 1
                        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapArray[i][0] > self.heapArray[mc][0]:
                tmp = self.heapArray[i]
                self.heapArray[i] = self.heapArray[mc]
                self.heapArray[mc] = tmp
            i = mc
                
    def minChild(self,i):
        if i*2 > self.currentSize:
            return -1
        else:
            if i*2 + 1 > self.currentSize:
                return i*2
            else:
                if self.heapArray[i*2][0] < self.heapArray[i*2+1][0]:
                    return i*2
                else:
                    return i*2+1

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i//2][0]:
                tmp = self.heapArray[i//2]
                self.heapArray[i//2] = self.heapArray[i]
                self.heapArray[i] = tmp
            i = i//2
 
    def add(self,k):
        self.heapArray.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapArray.pop()
        self.percDown(1)
        return retval
        
    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

    def decreaseKey(self,val,amt):
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heapArray[myKey] = (amt,self.heapArray[myKey][1])
            self.percUp(myKey)
            
    def __contains__(self,vtx):
        for pair in self.heapArray:
            if pair[1] == vtx:
                return True
        return False

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id
    
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])    

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
##################################################################

######## Problem 1 #########
def kruskal(graph):
    pq = PriorityQueue()
    kruskal_graph = Graph()
    parent = {(k,k) for k in graph}
    
    pq.buildHeap(
        []
    )
        
    #print(pq.heapArray)
    return graph
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

def prim(graph, start_vertex):
    pq = PriorityQueue()
    prim_graph = Graph()
    graph.vertList[start_vertex].setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in graph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
          newCost = currentVert.getWeight(nextVert)
          if nextVert in pq and newCost < nextVert.getDistance():
              prim_graph.addEdge(currentVert.getId(), nextVert.getId(), newCost)
              prim_graph.addEdge(nextVert.getId(), currentVert.getId(), newCost)
              nextVert.setPred(currentVert)
              nextVert.setDistance(newCost)
              pq.decreaseKey(nextVert,newCost)
    return prim_graph
    
    
    
    
    
    
    
    
    
    
    
    
    
    

######## Problem 2 #########
class PointVertex:
    
    
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class PointGraph:
    
    
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def bellman_ford(graph, start_vertex):
    
    
    
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

