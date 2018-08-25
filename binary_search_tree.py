class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.inorder_list = []

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is None:
            return None
        else:
            self._print_tree(current_node.left)
            print current_node.value
            self._print_tree(current_node.right)

    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)
        else:
            return []

    def _inorder(self, current_node):
        if current_node is not None:
            self._inorder(current_node.left)
            self.inorder_list.append(current_node.value)
            self._inorder(current_node.right)

    def minDiff(self):
        ans = 4343
        for i in range(1, len(self.inorder_list)):
            ans = min(ans, self.inorder_list[i] - self.inorder_list[i-1])
        return ans

bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)

bst.insert(3)

# bst.print_tree()
bst.insert(5)

print "*" * 10

bst.print_tree()
bst.inorder()
print bst.inorder_list
print bst.minDiff()
