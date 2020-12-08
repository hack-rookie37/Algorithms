#execution code

from assignment6 import PointVertex, PointGraph, bellman_ford

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
Node A
B : 5.00
C : 3.00
Node B
Node C
D : 1.00
Node D

--------------------
Node A
B : 5.00
C : 3.00
Node B
C : -4.00
Node C
D : 1.00
Node D
'''

bellman_ford(g, a)
'''
{'A': 0, 'B': 5.0, 'C': 1.0, 'D': 2.0}
'''
