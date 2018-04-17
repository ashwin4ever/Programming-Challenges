#Find longest path in a tree


class Tree:

      def __init__(self , val):
            self.data = val
            self.right = None
            self.left = None


      def height(self , node):

            if node is None:
                  return 0

            return max(self.height(node.left) , self.height(node.right)) + 1


      def diameter(self , node):


            if node is None:
                  return 0


            #get height
            lh = self.height(node.left)
            rh = self.height(node.right)

            #get diameter
            ld = self.diameter(node.left)
            rd = self.diameter(node.right)

            print(ld , rd)

            return max(lh + rh + 1 , max(ld , rd))
      

      def diameterOps(self , node):

            if node is None:
                  return 0 , 0

            lh , ld = self.diameterOps(node.left)
            rh , rd = self.diameterOps(node.right)

            height = max(lh , rh) + 1

            rootD = lh + rh + 1

            print(ld , rd , rootD)

            finalD = max(ld , rd , rootD)

            return finalD , height


            

            


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)

print(root.diameter(root))
print(root.diameterOps(root))
