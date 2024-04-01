class Node:
    def __init__ (self, data):
        self.left = None
        self. right = None
        self.val = data
 
  

def orderofTraversal(root):
       if root:
        orderofTraversal (root.left)
        print(root.val)
        orderofTraversal (root.right)
       

root = Node(48)
root.left = Node(14)
root.right = Node(10)
root.left.left = Node(8)
root.left.right = Node(82)
root.right.right = Node(54)

print("orderofTraversal:")
orderofTraversal(root)