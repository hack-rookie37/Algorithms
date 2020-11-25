from BinarySearchTree import *
from problem1 import findTraversal, findGreedy

my_tree = BinarySearchTree()

my_tree[17] = 5
my_tree[35] = 8
my_tree[2] = 7
my_tree[11] = 2
my_tree[29] = 5
my_tree[38] = 2
my_tree[9] = 3
my_tree[16] = 1
my_tree[7] = 2
my_tree[8] = 1

#print_tree(my_tree)
'''
Total Nodes :  10
(Root) [17]:5
      1-(R) [35]:8
           2-(R) [38]:2
           2-(L) [29]:5
      1-(L) [ 2]:7
           2-(R) [11]:2
                3-(R) [16]:1
                3-(L) [ 9]:3
                     4-(L) [ 7]:2
                          5-(R) [ 8]:1
'''

print('Traversal Serach: %d' % (findTraversal(my_tree)))
#print('Greedy Serach: %d' % (findGreedy(my_tree)))