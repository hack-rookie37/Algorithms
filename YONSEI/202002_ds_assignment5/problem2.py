'''
Student ID:
NAME: 
'''
# Do Not Distrub TreeNode Class
class TreeNode:
    def __init__(self, data, parent=None):
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

###################################################
    def printTree(self):
        print('\n'+'-'*20+'Print Tree'+'-'*20)
        tmp_list = [self.root]
        while 1:
            child_list = tmp_list.copy()
            tmp_list = []
            for child in child_list:
                print(child.data, end=' ')
                tmp_list.extend(child.child)
            print()
            if len(tmp_list) == 0:
                break
        print('-'*50)
###################################################

    def insert(self, item):  # find location to add Node
        print("Insert: " + str(item))
        new_node = TreeNode(item)
        if self.root:
            cur_node = self.root
            
            while True:
                if cur_node._isLeaf():
                    self.add(cur_node, new_node)
                    break
                else:
                    if new_node < cur_node:
                        cur_node = cur_node.child[0]
                        continue
                    else:
                        cur_node = cur_node.child[1]
                        continue
        else:
            self.root = new_node
            self.size = 1
        

    def add(self, current_node, new_node):
        current_node.data.append(new_node.data[0])
        current_node.data.sort()
        self.check(current_node)

    def split(self, current_node):
        print("Split: " + str(current_node.data))        
        
        split_node = TreeNode(current_node.data[1], current_node.parent)
        left_node = TreeNode(current_node.data[0], split_node)
        right_node = TreeNode(current_node.data[2], split_node)
        split_node.child.append(left_node)
        split_node.child.append(right_node)        
        if current_node.parent == None:
            current_node.parent = split_node
            self.root = current_node.parent
        else:
            current_node.parent.data.append(split_node.data[0])
            current_node.parent.data.sort()
            current_node.parent.child.remove(current_node)
            current_node.parent.child.append(left_node)
            current_node.parent.child.append(right_node)
        
        self.size = self.size + 1

    def check(self, current_node):
        if len(current_node) > 2:
            self.split(current_node)
    
    def find(self, item):
        ## CODE HERE ##
        pass
