import math
import sys

################ DO NOT modify this code ######################


class PriorityQueue:
    def __init__(self):
        self.heapArray = [(0, 0)]
        self.currentSize = 0

    def buildHeap(self, alist):
        self.currentSize = len(alist)
        self.heapArray = [(0, 0)]
        for i in alist:
            self.heapArray.append(i)
        i = len(alist) // 2
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapArray[i][0] > self.heapArray[mc][0]:
                tmp = self.heapArray[i]
                self.heapArray[i] = self.heapArray[mc]
                self.heapArray[mc] = tmp
            i = mc

    def minChild(self, i):
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

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i//2][0]:
                tmp = self.heapArray[i//2]
                self.heapArray[i//2] = self.heapArray[i]
                self.heapArray[i] = tmp
            i = i//2

    def add(self, k):
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

    def decreaseKey(self, val, amt):
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
            self.heapArray[myKey] = (amt, self.heapArray[myKey][1])
            self.percUp(myKey)

    def __contains__(self, vtx):
        for pair in self.heapArray:
            if pair[1] == vtx:
                return True
        return False


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.dist = d

    def setPred(self, p):
        self.pred = p

    def setDiscovery(self, dtime):
        self.disc = dtime

    def setFinish(self, ftime):
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

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
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
    # e.g. ['A':'A', 'B':'B', ... 'F':'F']
    parent = {key: key for key in graph.vertList}
    pq.buildHeap([
        # (edgeValue, (key=start, k=end)) e.g. [(0,0), (1,('A', 'B'), (2, 'A', 'C'), ...)]
        (v, (key, k.getId()))
        for key in graph.vertList
        for k, v in graph.vertList[key].connectedTo.items()
        if key < k.getId()
    ])
    kruskal_grpah = Graph()
    while not pq.isEmpty():
        dist = pq.heapArray[1][0]
        newEdge = pq.delMin()

        def findParent(v):
            if parent[v] == v:
                return v
            return findParent(parent[v])
        p0 = findParent(newEdge[0])
        p1 = findParent(newEdge[1])
        if p0 == p1:
            continue
        else:
            parent[p1] = parent[p0]
            kruskal_grpah.addEdge(newEdge[0], newEdge[1], dist)
            kruskal_grpah.addEdge(newEdge[1], newEdge[0], dist)
    return kruskal_grpah


def prim(graph, start_vertex):
    pq = PriorityQueue()
    for v in graph:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    graph.vertList[start_vertex].setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in graph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getWeight(nextVert)
            if nextVert in pq and newCost < nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                # locates adjcent vertices(nextVert) by pq based on the currently selected vertex
                pq.decreaseKey(nextVert, newCost)
    pq.buildHeap([(v.getDistance(), v) for v in graph])
    prim_graph = Graph()
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getWeight(nextVert)
            if newCost == nextVert.getDistance():
                prim_graph.addEdge(currentVert.getId(),
                                   nextVert.getId(), newCost)
                prim_graph.addEdge(
                    nextVert.getId(), currentVert.getId(), newCost)
    return prim_graph


######## Problem 2 #########
class PointVertex:
    def __init__(self, key, x, y, reward):
        self.key = key
        self.x = x
        self.y = y
        self.reward = reward
        self.connectedTo = {}
        self.distance = sys.maxsize
        self.pred = None

    def get_key(self):
        return self.key

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_reward(self):
        return self.reward

    def get_connections(self):
        return self.connectedTo

    def get_distance(self):
        return self.distance

    def get_pred(self):
        return self.pred

    def add_neighbor(self, nbr, weight=0):
        # add if empty, or update weight
        self.connectedTo[nbr] = weight

    def set_distance(self, d):
        self.distance = d
        
    def set_pred(self, p):
        self.pred = p


class PointGraph:
    def __init__(self, thres):
        self.thres = float(thres)
        self.vertList = {}
        self.numVertices = 0

    def get_vertices(self):
        return self.vertList

    def add_vertex(self, vertex):
        self.numVertices = self.numVertices + 1
        self.vertList[vertex.get_key()] = vertex
        if self.numVertices >= 2:
            vlist = list(self.vertList)
            # nested loop e.g. A B, A C, A D, B C, B D, C D (PointVertex Object)
            # operation complexity: n combination 2
            for i in range(len(vlist)):
                for j in range(i+1, len(vlist), 1):
                    src = self.vertList[vlist[i]]
                    dst = self.vertList[vlist[j]]
                    dist = self.get_distance(src, dst)
                    reward = self.cal_reward(src, dst)
                    if dist >= self.thres:  # add_edge if dist < thres
                        continue
                    else:
                        val = dist + reward
                        if reward >= 0:
                            self.add_edge(dst, src, val)
                        if reward <= 0:
                            self.add_edge(src, dst, val)

    def add_edge(self, src, dst, val):
        if src not in self.vertList:
            self.numVertices = self.numVertices + 1
            self.vertList[src.get_key()] = src
        if dst not in self.vertList:
            self.numVertices = self.numVertices + 1
            self.vertList[dst.get_key()] = dst
        src.add_neighbor(dst.get_key(), val)

    def get_distance(self, src, dst):
        # Pythagoras
        return math.sqrt((src.get_x() - dst.get_x())**2 + (src.get_y() - dst.get_y())**2)

    def cal_reward(self, src, dst):
        return src.get_reward() - dst.get_reward()

    def __str__(self):
        string = ''
        for k, v in self.vertList.items():
            string = string + 'Node ' + k + '\n'
            if v.get_connections() != None:
                for ck, cv in v.get_connections().items():
                    string = string + ck + ' : ' + str(cv) + '\n'
        return string

    def __iter__(self):
        return iter(self.vertList.values())


def bellman_ford(graph, start_vertex):
    # Dist(s,v) = Dist(s,u) + weight(u,v)
    # negative cycle return None
    bf = {}
    # start = 0, the rests set to infinite
    for v in graph:
        v.set_distance(sys.maxsize)
        v.set_pred(None)
    graph.vertList[start_vertex.get_key()].set_distance(0)

    # relax
    # u is start, v is destination, w is weight from u to v
    for u in graph:
        for v in u.get_connections().keys():
            if graph.vertList[v].get_distance() > u.get_distance() + u.get_connections()[v]:
                graph.vertList[v].set_distance(u.get_distance() + u.get_connections()[v])
                graph.vertList[v].set_pred(u) 
    # detect nagative cycle(s)
    for u in graph:
        for v in u.get_connections().keys():
            if graph.vertList[v].get_distance() > u.get_distance() + u.get_connections()[v]:
                return None
        # bf to dictionary
        bf[u.get_key()] = graph.vertList[u.get_key()].get_distance()
    print(bf)
    return bf