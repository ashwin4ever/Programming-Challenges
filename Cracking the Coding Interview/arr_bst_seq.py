#Find all possible
#binary trees with given Inorder Traversal



class Tree:

      def __init__(self , val = None):

            self.data = val
            self.rightChild = None
            self.leftChild = None

      def preOrder(self , node):

            if node is not None:
                  print(node.data)
                  print(node.leftChild)
                  print(node.rightChild)

      def generateTrees(self , arr , start , end):

            trees = []

            if start > end:
                  return None

            for i in range(start , end + 1):
                  print(i)

                  left = self.generateTrees(arr , start , i - 1)
                  right = self.generateTrees(arr , i + 1 , end)
                  print(left , right)
                  for l in left:
                              
                        for r in right:
                              t = Tree(arr[i])

                              t.leftChild = l
                              t.rightChild = r

                              trees.append(t)
            return trees



arr = [4 , 5, 7]
n = len(arr)
t = Tree()
print(t.generateTrees(arr , 0 , n - 1))
            
