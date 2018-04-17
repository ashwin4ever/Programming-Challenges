#find celebrity



class Stack:

      def __init__(self):

            self.stack = list()

      def isEmpty(self):
            return self.stack == []

      def top(self):

            return self.stack[-1]

      def pop(self):
            return self.stack.pop()

      def push(self , val):
            self.stack.append(val)



def knows(a , b):
      data = [[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]

      return data[a][b]
      

def findCelebrity(n):

      s = Stack()

      for i in range(n):
            s.push(i)


      a = s.top()
      s.pop()

      b = s.top()
      s.pop()

      while len(s.stack) > 1:

            if knows(a , b):
                  a = s.top()
                  s.pop()
            else:
                  b = s.top()
                  s.pop()

      c = s.top()
      s.pop()

      if knows(c , b):
            c = b

      if knows(c , a):
            c = a


      for i in range(n):

            if ((i != c) and (knows(c , i) or not knows(i , c))):
                  return -1

      return c
            
            
            
data = [[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]

print(findCelebrity(4))
