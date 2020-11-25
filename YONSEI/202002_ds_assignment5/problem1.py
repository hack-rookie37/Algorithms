'''
Student ID:
NAME :
'''
from BinarySearchTree import *


def findTraversal(tree):  # DFS, Pre-order(NLR)
    if isinstance(tree, BinarySearchTree):  # tree가 BST의 instance이면
        tree = tree.root  # tree를 tree의 root node로 assign.  
        # from:  type(tree) == BinarySearchTree.BinarySearchTree
        # to:  type(tree) == BinarySerachTree.TreeNode
    
    '''
    # Pre-order 확인용 key 출력 code
    if isinstance(tree, TreeNode):
        print(tree.key)
    '''
    
    if tree == None:  # 비어있는 자식이면 payload = 0으로 return
        return 0
    payload = tree.payload  # payload -> TreeNode.payload
    left, right = 0, 0 # left, right 
    left += findTraversal(tree.left_child) # sum of leftchilds' payloads
    right += findTraversal(tree.right_child) # sum of rightchilds' payloads
    if left > right: # compare
        payload += left # assign
    else:
        payload += right # assing
    return payload # return


def findGreedy(tree):
    ## CODE HERE ##
    pass
