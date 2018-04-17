#Sort Stack : have all mins at the top


class Stack:

      def __init__(self):

            self.stack = []
            self.size = 0


      def push(self , val):

            self.stack.append(val)
            self.size += 1

            print("Stack contents: " , self.stack)

      def pop(self):

            assert not self.isEmpty(), "Empty Stack"
            self.size -= 1
            return self.stack.pop()

      def peek(self):
            print(self.stack , self.size)
            return self.stack[-1]

      def isEmpty(self):
            return self.size == 0



class SortStack:

      def __init__(self):

            self.orig = Stack()
            self.buff = Stack()


      def push(self , val):
            self.orig.push(val)


      def sortMin(self):

            while not self.orig.isEmpty():
                  tmp = self.orig.pop()

                  print('tmp: ' , tmp)
                  print('buff: ' , self.buff.stack)
                  while not self.buff.isEmpty() and self.buff.peek() > tmp:
                        self.orig.push(self.buff.pop())

                  self.buff.push(tmp)

                  print('Orig: ', self.orig.stack)
                  print('Buff: ', self.buff.stack)
                  
            
            
            
s = SortStack()
s.push(12)
s.push(8)
s.push(5)
s.push(7)
s.push(13)

s.sortMin()
            
