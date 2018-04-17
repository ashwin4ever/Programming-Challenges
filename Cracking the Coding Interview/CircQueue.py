#implement circular queue


import Array


class Queue:

      def __init__(self , maxSize):

            self.count = 0
            self.front = 0
            self.back = maxSize - 1
            self.qArr = Array.Array(maxSize)

      def isEmpty(self):
            return self.count == 0

      def isFull(self):
            return self.count == len(self.qArr)

      def __len__(self):
            return self.count

      #add element
      def enqueue(self , data):

            assert not self.isFull() , "Cannot add"

            maxSize = len(self.qArr)

            self.back = (self.back + 1) % maxSize
            self.qArr[self.back] = data
            self.count += 1
            

      #remove element
      def dequeue(self):
            assert not self.isEmpty() , "Queue is empty"

            item = self.qArr[self.front]
            maxSize = len(self.qArr)

            self.front = (self.front + 1) % maxSize
            self.count -= 1
            return item


q = Queue(5)
print(len(q))
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(len(q))
print(q.dequeue())
