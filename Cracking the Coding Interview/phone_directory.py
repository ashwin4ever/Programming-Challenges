#Phone Directory




class Trie:

      def __init__(self):

            self.root = {}
            #self.leaf = False


      def add(self , name):

            node = self.root

            for c in name:
                  if c not in node:
                        node[c] = {}

                  node = node[c]
                  


      def find(self , key):

            node = self.root

            for k in key:
                  if k not in node.keys():
                        return None
                  node = node[k]

            return node

      def listNames(self , names):

            sub_node = self.find(names)

            #print(sub_node.keys())

            #for k in sub_node.keys():
                  #print(sub_node[k])

            printNames(sub_node , names)

def printNames(sub_node , names):

      #print(sub_node.keys())

      
      for n in sub_node.keys():
            #if not sub_node.get(n):
            printNames(sub_node[n] , names + n)
            
      temp = sub_node.keys()
      if len(temp) == 0:
            print(names)


T = Trie()
T.add("Joe")
T.add("James")
T.add("Samantha")
T.add("Sam ")
T.listNames("J")
T.listNames("S")
