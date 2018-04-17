#Implementation of Stack in Python

class Stack:

      #create empty stack
      def __init__(self ):
            self.stack = list()

      #returns true if stack is empty
      def isEmpty(self):
            return len(self) == 0

      #returns the num of items in stack
      def __len__(self):
            return len(self.stack)

      #returns the top of the stack without removing
      def peek(self):
            assert not self.isEmpty() , "Cannot peak empty stack"
            return self.stack[-1]

      #removes and returns the top element from stack
      def pop(self):
            assert not self.isEmpty() , "Cannot pop empty stack"
            return self.stack.pop()

      def push(self , val):
            return self.stack.append(val)



s = Stack()
print(s.isEmpty())

print(s.push(1) , s.peek())
      
