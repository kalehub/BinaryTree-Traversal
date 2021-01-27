
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left= None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def traverse_preOrder(self, root ):
        if root:
            print(root.data)
            self.traverse_preOrder(root.left)
            self.traverse_preOrder(root.right)

    def traverse_inOrder(self, root):
        if root:
            self.traverse_inOrder(root.left)
            print(root.data)
            self.traverse_inOrder(root.right)

    def traverse_postOrder(self, root):
        if root:
            self.traverse_postOrder(root.left)
            self.traverse_postOrder(root.right)
            print(root.data)



if __name__ == '__main__':
    bt = BinaryTree(20)

    bt.root.left = Node(17)
    bt.root.right = Node(18)
    bt.root.left.left = Node(16)
    bt.root.left.right = Node(14)
    bt.root.right.left = Node(10)
    bt.root.right.right = Node(12)

    #bt.traverse_preOrder(bt.root)
    #bt.traverse_inOrder(bt.root)
    bt.traverse_postOrder(bt.root)


