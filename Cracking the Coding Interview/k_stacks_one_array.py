#Implement k stacks in one array


class KStacks():

      def __init__(self , k , n):

            self.top = [-1] * n

            #self.next = [0] * n
            self.next = [x + 1 for x in range(n - 1)]
            
            self.next.append(-1)
            print(self.next)

            self.arr = [0] * n
            self.free = 0

      def isFull(self):
            return self.free == -1

      def isEmpty(self , sn):
            return self.top[sn] == -1

      def push(self , data , sn):

            assert not self.isFull() , "Stack is full"

            i = self.free

            self.free = self.next[i]

            self.next[i] = self.top[sn]
            self.top[sn] = i

            self.arr[i] = data

            print('free: ' , self.free)


      def pop(self , sn):

            assert not self.isEmpty(sn) , "Stack {} is empty ".format(sn)

            i = self.top[sn]

            self.top[sn] = self.next[i]

            self.next[i] = self.free

            print('Pop free: ' , self.free)

            self.free = i

            return self.arr[i]


ks = KStacks(5 , 5)

ks.push(1 , 1)
ks.push(1 , 2)
ks.push(1 , 3)
ks.push(1 , 4)
ks.push(2 , 1)
ks.push(3 , 1)
print(ks.pop(1))
            

            
