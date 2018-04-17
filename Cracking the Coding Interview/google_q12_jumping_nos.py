#Jumping numbers

class Queue:

      def __init__(self):

            self.q = []

      def isEmpty(self):
            return self.q == []

      def enqueue(self , val):
            self.q.append(val)

      def dequeue(self):
            return self.q.pop(0)




def jumpingNum(i , num):

      qu = Queue()

      qu.enqueue(i)

      while not qu.isEmpty():

            x = qu.dequeue()

            if x <= num:

                  print(str(x) , end = ' ')

                  lastDigit = x % 10

                  if lastDigit == 0:
                        t = (x * 10) + (lastDigit + 1)
                        print(t)
                        qu.enqueue(t)

                  elif lastDigit == 9:
                        
                        t = (x * 10) + (lastDigit - 1)
                        print(t)
                        qu.enqueue(t)

                  else:
                        qu.enqueue((x * 10) + (lastDigit - 1))
                        qu.enqueue((x * 10) + (lastDigit + 1))
                  
    


n = 120

for i in range(1 , 10):
      jumpingNum(i , n)
