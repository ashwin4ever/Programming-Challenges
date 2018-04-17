#Trie

from collections import defaultdict

class TrieNode():

      def __init__(self , key = None):

            self.children = defaultdict(str)
            self.isLeaf = False

            if key:
                  self.children[key] = None


class Trie:

      def __init__(self , trieNode):

            self.root = trieNode

      def insert(self , val):

            r = self.root
            print(r.children)
            print(val)

            for v in val:
                  if v not in r.children:
                        r.children[v] = TrieNode()

                  r = r.children[v]

            r.isLeaf = True

      def search(self , val):

            r = self.root

            for v in val:
                  if v in r.children:
                        r = r.children[v]
                        print(r)
                  else:
                        return False

            return True if r.isLeaf else False


string = ["abhi", "ram", "abhishek", "abhish"]

node = TrieNode()
trie = Trie(node)

for s in string:
      trie.insert(s)

print(trie.search('abhi'))
                        
