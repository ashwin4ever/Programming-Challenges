#Check if a tree is balanced

import math

class Tree:

      def __init__(self , val):

            self.data = val
            self.rightChild = None
            self.leftChild = None



      def findHeight(self , node):

            if node is None:
                  return -1
            
            else:
                  return max(self.findHeight(node.leftChild) , self.findHeight(node.rightChild)) + 1




      def isBalanced(self , node):

            if node is None:
                  return False

            leftHeight = self.findHeight(node.leftChild)
            rightHeight = self.findHeight(node.rightChild)

            print(leftHeight , rightHeight)

            if abs(leftHeight - rightHeight) > 1:
                  print('Not balanced')
                  return False

            return True



root = Tree(1)
root.leftChild = Tree(2)
root.rightChild = Tree(3)
root.leftChild.leftChild = Tree(4)
root.leftChild.rightChild = Tree(5)
root.leftChild.leftChild.leftChild = Tree(8)

print(root.isBalanced(root))

      
