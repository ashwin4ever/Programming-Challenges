#Implement Queue using Stacks


class QueueStack:

      def __init__(self):

            self.s1 = []
            self.s2 = []
            self.size = 0


      def enqueue_stack(self , val):

            self.s1.append(val)
            self.size += 1

            print("Queue pushed: " , self.s1)

      def deque_stack(self):

            assert not self.s1 == [] ,"Empty stacks"

            while self.size > 1:
                  d = self.s1[-1]
                  del self.s1[-1]
                  self.s2.append(d)
                  self.size -= 1

            print(self.s1 , self.s2)
            pop = self.s1[-1]
            del self.s1[-1]

            while len(self.s2) > 0:
                  print(self.s2[-1])
                  self.enqueue_stack(self.s2[-1])
                  del self.s2[-1]


            print("Queue: " , self.s1)

            return pop

            
q = QueueStack()
q.enqueue_stack(1)
q.enqueue_stack(2)
q.enqueue_stack(3)
q.enqueue_stack(4)
print('Popped: ' , q.deque_stack())
