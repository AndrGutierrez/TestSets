class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.sdata: list[int]=[]
        self.root= TreeNode(tree_data[0])
        self.tree_data = tree_data
        for item in tree_data[1:]:
            found = False
            j = 0
            current_node= self.root
            while not found:
                if item <= current_node.data:
                    if current_node.left == None:
                        current_node.left = TreeNode(item, None, None)
                        found = True
                    else:
                        current_node = current_node.left 
                        continue
                else:
                    if current_node.right == None:
                        current_node.right = TreeNode(item, None, None)
                        found = True
                    else: 
                        current_node = current_node.right
                j+=1

        pass

    def data(self) :
        return self.root

    def append(self, node):
        if node.left is not None:
            self.append(node.left)
        self.sdata.append(node.data)
        if node.right is not None:
            self.append(node.right)

    def sorted_data(self):
        # stop = False
        # current_node = self.data()
        self.append(self.data())
        # print(self.sdata)
        return self.sdata
        # izquierda -> raiz -> derecha, recursivamente
        pass
