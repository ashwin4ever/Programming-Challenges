#Stack Linked List


class StackList:

      def __init__(self):

            self.top = None
            self.size = 0

      #return true if stack is empty
      def isEmpty(self):
            return self.top is None

      #returns the num items
      def __len__(self):
            return self.size

      #return top elem of stack without removing
      def peek(self):
            assert not self.isEmpty() , "Cannot peek empty stack"

            return self.top.data

      #removes and return top element
      def pop(self):
            
            assert not self.isEmpty() , "Connot pop empy stack"
            node = self.top
            self.top = self.top.next
            self.size -= 1
            return node.data

      #push an item onto top of stack
      def push(self , val):
            self.top = Node(val , self.top)
            self.size += 1

      def traverse(self):

            cur = self.top

            while cur is not None:
                  print(cur.data)
                  cur = cur.next
            





class Node:
      
      def __init__(self , data , link):
            self.data = data
            self.next = link
            

s = StackList()
s.push(1)
s.push(2)
s.push(3)
s.traverse()
print('peek: ' ,s.peek())
print('popped: ' ,s.pop())
