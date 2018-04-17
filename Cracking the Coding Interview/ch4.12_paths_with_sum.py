#number of paths that sum to a given value


class Tree:

      def __init__(self , val):

            self.data = val
            self.rightChild = None
            self.leftChild = None




     


      def isPathSum(self , node , path , target , currentSum):

            if node is None:
                  return -1

            currentSum += node.data
            path.append(node.data)
            #print(path)

            if node.leftChild is None and node.rightChild is None:
                  if currentSum == target:
                        print('path is found')
                        print(path)
                        return path

            if node.leftChild is not None:
                  self.isPathSum(node.leftChild , path , target , currentSum)

            if node.rightChild is not None:
                  self.isPathSum(node.rightChild , path , target , currentSum)

            path.pop()



T = Tree(26)
T.rightChild = Tree(8)
T.rightChild.rightChild  = Tree(8)
T.leftChild = Tree(10)
T.leftChild.leftChild = Tree(4)
T.leftChild.leftChild.rightChild = Tree(30)
T.leftChild.rightChild = Tree(6)

p = T.isPathSum(T , [] , 42 , 0)
print(p)
