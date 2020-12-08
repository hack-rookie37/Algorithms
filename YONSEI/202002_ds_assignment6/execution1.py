#execution code

from assignment6 import Graph, kruskal, prim

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
'''
'''
remain_alphabets = ['B', 'D', 'E']
for alpha in remain_alphabets:
    print(alpha, 'is connected to')
    for k, v in g_mst2.vertList[alpha].connectedTo.items():
        print(k.getId(), ':', v)
    print('-' * 20)
'''
'''
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
