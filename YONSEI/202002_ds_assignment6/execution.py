#execution code

from assignment6 import Graph, kruskal, prim, PointVertex, PointGraph, bellman_ford

# problem 1
g = Graph()

g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addVertex('F')

g.addEdge('A', 'B', 1)
g.addEdge('B', 'A', 1)
g.addEdge('A', 'C', 2)
g.addEdge('C', 'A', 2)
g.addEdge('B', 'C', 3)
g.addEdge('C', 'B', 3)
g.addEdge('C', 'D', 4)
g.addEdge('D', 'C', 4)
g.addEdge('C', 'E', 5)
g.addEdge('E', 'C', 5)
g.addEdge('C', 'F', 6)
g.addEdge('F', 'C', 6)
g.addEdge('D', 'E', 7)
g.addEdge('E', 'D', 7)
g.addEdge('E', 'F', 8)
g.addEdge('F', 'E', 8)

g_mst = kruskal(g)
g_mst2 = prim(g, 'A')

alphabets = ['A', 'C', 'F']
for alpha in alphabets:
    print(alpha, 'is connected to')
    for k, v in g_mst.vertList[alpha].connectedTo.items():
        print(k.getId(), ':', v)
    print('-' * 20)

remain_alphabets = ['B', 'D', 'E']
for alpha in remain_alphabets:
    print(alpha, 'is connected to')
    for k, v in g_mst2.vertList[alpha].connectedTo.items():
        print(k.getId(), ':', v)
    print('-' * 20)

'''
A is connected to
B : 1
C : 2
--------------------
C is connected to
A : 2
D : 4
E : 5
F : 6
--------------------
F is connected to
C : 6
--------------------
B is connected to
A : 1
--------------------
D is connected to
C : 4
--------------------
E is connected to
C : 5
--------------------
'''


# problem 2
a = PointVertex('A', 0, 0, 0)
b = PointVertex('B', 6, 0, 1)
c = PointVertex('C', 0, 5, 2)
d = PointVertex('D', 0, 7, 3)

g = PointGraph(7)
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)

print(g)
print('-' * 20)
g.add_edge(b, c, -4)
print(g)

'''
a = PointVertex('A', 0, 0, 0)
b = PointVertex('B', 6, 0, 1)
c = PointVertex('C', 0, 5, 2)
d = PointVertex('D', 0, 7, 3)

g = PointGraph(7)
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)

print(g)
print('-' * 20)
g.add_edge(b, c, -4)
print(g)
'''
