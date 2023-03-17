

from termcolor import colored

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.red=True
        self.left=None
        self.right = None
        self.parent=None

class RBTree :
    def __init__(self) -> None:
        self.root=None

    def search(self, key):
        current_node = self.root
        while current_node is not None and key != current_node.key:
            if key<current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node
    
    def insert (self, key):
        node_to_insert = Node(key)
        if self.root==None:
            node_to_insert.red=False
            self.root=node_to_insert
            print (f'root is {self.root} with Red (T) or Black (F) color {self.root.red}')
            return
        last_node=self.root
        while last_node is not None:
            potential_parent=last_node
            if node_to_insert.key <last_node.key:
                last_node=last_node.left
            else:
                last_node=last_node.right
        node_to_insert.parent=potential_parent
        print (f'New node is {node_to_insert.key} with parent {node_to_insert.parent}')
        if node_to_insert.key<node_to_insert.parent.key:
            node_to_insert.parent.left=node_to_insert
        else:
            node_to_insert.parent.right=node_to_insert
        node_to_insert.left=None
        node_to_insert.right=None
        self.fix(node_to_insert)

    def fix (self, node):
        try:
            while node.parent.red is True and node is not self.root:
                if node.parent == node.parent.parent.left:
                    uncle = node.parent.parent.right
                    if uncle.red:
                        node.parent.red = False
                        uncle.red = False
                        node.parent.parent.red = True
                        node = node.parent.parent
                    else:
                        if node == node.parent.right:
                            node = node.parent
                else:
                    try:
                        uncle=node.parent.parent.left
                        if uncle.red :
                            node.parent.red=False
                            uncle.red = False
                            node.parent.parent.red = True
                    except AttributeError:
                        print("error")
                        break
            self.root.red = False
        except AttributeError:
            print('error')

    def del_node(self, key):
        current_node=self.search(key)
        if current_node==None:
            return
        if current_node.parent==None:
            if current_node==self.root:
                self.root=None
            return
        if current_node.parent.left == current_node:
            current_node.parent = None
        else:
            current_node.parent = None






