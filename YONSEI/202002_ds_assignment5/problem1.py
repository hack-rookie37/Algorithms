'''
Student ID: 60162161
NAME : 이정훈
'''
from BinarySearchTree import *


def findTraversal(tree):  # DFS, Pre-order(NLR)
    if isinstance(tree, BinarySearchTree):  # tree가 BST의 instance이면
        tree = tree.root  # tree를 tree의 root node로 assign.
        # from:  type(tree) == BinarySearchTree.BinarySearchTree
        # to:  type(tree) == BinarySerachTree.TreeNode

    '''
    # Check Pre-order
    if isinstance(tree, TreeNode):
        print(tree.key)
    '''

    if tree == None:  # Base case) null node
        return 0
    payload = tree.payload  # payload -> TreeNode.payload
    left, right = 0, 0  # left, right
    left += findTraversal(tree.left_child)  # sum of leftchilds' payloads
    right += findTraversal(tree.right_child)  # sum of rightchilds' payloads
    if left > right:  # compare
        payload += left  # assign
    else:
        payload += right  # assing
    return payload  # return


def findGreedy(tree):
    if isinstance(tree, BinarySearchTree): # tree가 BST의 instance이면
        tree = tree.root # tree를 tree의 root node로 assign.
        # from:  type(tree) == BinarySearchTree.BinarySearchTree
        # to:  type(tree) == BinarySerachTree.TreeNode

    '''
    # seems never touch basecase
    # because check child nodes if null
    if tree == None: # Base case) null node
        print('touch')
        return 0
    '''
    
    payload = tree.payload # payload -> TreeNode.payload
    if tree.left_child == None and tree.right_child == None: # Both childs are null
        return payload # return payload itself
    elif tree.left_child == None: # left is null
        payload += findGreedy(tree.right_child) # goto right
    elif tree.right_child == None: # right is null
        payload += findGreedy(tree.left_child) # goto left
    else:
        if tree.left_child.payload > tree.right_child.payload: # compare and decide where to go find
            payload += findGreedy(tree.left_child) # goto left
        else:
            payload += findGreedy(tree.right_child) # goto right
    return payload
