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
    if tree == None: # Basecase. (Just in case)
        return 0
    
    #tree is instance of TreeNode
    payload = tree.payload
    left, right = 0, 0  # sum of payloads of left children, right children
    if tree.has_left_child():
        left += findTraversal(tree.left_child)  # addition
    if tree.has_right_child():
        right += findTraversal(tree.right_child)  # addition
    if left > right:  # compare and assign bigger one
        payload += left
    else:
        payload += right  
    return payload  # return final payload


def findGreedy(tree):
    if isinstance(tree, BinarySearchTree): # tree가 BST의 instance이면
        tree = tree.root # tree를 tree의 root node로 assign.
        # from:  type(tree) == BinarySearchTree.BinarySearchTree
        # to:  type(tree) == BinarySerachTree.TreeNode
    
    if tree == None: # Basecase. (Just in case)
        return 0
    
    payload = tree.payload # payload -> TreeNode.payload
    if not tree.has_any_children(): # Both childs are null
        return payload # return payload itself
    elif not tree.has_left_child(): # left is null
        payload += findGreedy(tree.right_child) # goto right
    elif not tree.has_right_child(): # right is null
        payload += findGreedy(tree.left_child) # goto left
    else:
        if tree.left_child.payload > tree.right_child.payload: # compare and decide where to go find
            payload += findGreedy(tree.left_child) # goto left
        else:
            payload += findGreedy(tree.right_child) # goto right
    return payload
