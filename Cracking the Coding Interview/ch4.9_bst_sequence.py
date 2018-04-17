#BST Sequence


class Tree:

      def __init__(self , val):

            self.data = val
            self.leftChild = None
            self.rightChild = None


      def bstSequence(self , root):

            if root is None:
                  return None

            print(root.data , ' ' , end = '')

            self.bstSequence(root.leftChild)
            self.bstSequence(root.rightChild)



t = Tree(2)
t.leftChild = Tree(1)
t.rightChild = Tree(3)
t.bstSequence(t)
