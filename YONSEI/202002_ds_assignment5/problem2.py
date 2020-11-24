'''
Student ID:
NAME: 
'''


### Do Not Distrub TreeNode Class
class TreeNode:
    def __init__(self, data, parent = None):
        self.data = [data]
        self.parent = parent
        self.child = []
    
    def __len__(self):
        return len(self.data)
    
    def __lt__(self, node):
        return self.data[0] < node.data[0]

    def _isLeaf(self):
        return len(self.child) == 0


    
class TwoThreeTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def printTree(self):
        print('\n'+'-'*20+'Print Tree'+'-'*20)
        tmp_list = [self.root]
        while 1:
            child_list = tmp_list.copy() 
            tmp_list = []
            for child in child_list:
                print(child.data, end = ' ')
                tmp_list.extend(child.child)
            print()
            if len(tmp_list) == 0:
                break
        print('-'*50)
    
    def insert(self, item):
        print("Insert: " + str(item))
        ## CODE HERE ##
        pass

    
    def add(self, current_node, new_node):
        ## CODE HERE ##
        pass
        
    def split(self, current_node):
        print("Split: " + str(current_node.data))
        ## CODE HERE ##
        pass
        
    def find(self, item):
        ## CODE HERE ##
        pass