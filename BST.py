# based upon https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm

class Node:

    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    # Insert method to create nodes
    def insert(self, key, value):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key, value)
                else:
                    self.left.insert(key, value)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key, value)
                else:
                    self.right.insert(key, value)
        else:
            self.key = key
            self.value = value

    # find method to get the node with a certain key
    def find(self, key):
        if key < self.key:
            if self.left is None:
                return False
            return self.left.find(key)
        elif key > self.key:
            if self.right is None:
                return False
            return self.right.find(key)
        else:
            return self

    # findval method to get the value associated with a certain key
    def findval(self, key, False_return):
        node = self.find(key)
        if node:
            return node.value
        else:
            return False_return

    # update method to change the value associated with a key
    def update(self, key, value):
        node = self.find(key)
        if node:
            node.value = value
        else:
            self.insert(key, value)

    # returns highest value in the tree
    def max_val(self):
        if self.right is None:
            return self.value
        else:
            return self.right.max_val()
