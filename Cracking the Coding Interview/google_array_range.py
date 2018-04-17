#Array range



class Stack:

      def __init__(self):

            self.stack = list()

      def isEmpty(self):
            return self.stack == []

      def peek(self):

            assert not self.isEmpty() , "Cannot peek from empty stack"
            return self.stack[-1]

      def pop(self):
            assert not self.isEmpty() , "Cannot pop from empty stack"
            return self.stack.pop()

      def push(self , val):
            self.stack.append(val)




def overLapStack(arr):

      #[(2, 6), (3, 5), (7, 25), (20, 23)]
      # {{1,3}, {2,4}, {5,7}, {6,8} }

      arr.sort()
      stack = Stack()

      stack.push(arr[0])

      

      for i in range(1 , len(arr)):

            print(stack.stack)
            top = stack.peek()

            if arr[i][0] < top[1]:
                  temp = stack.pop()
                  stack.push((temp[0] , arr[i][1]))

            elif top[1] < arr[i][0]:
                  stack.push(arr[i])
                  
           

      print(stack.stack)
            

def overLapBF(arr):

      less = arr[0]
      new_arr = []

      for i in range(0 , len(arr) + 1):

            for j in range(i + 1 , len(arr)):

                  if arr[i][1] >= arr[j][1]:
                        new_arr.append((arr[i]))

      print(new_arr)


      


#arr = [(2, 6), (3, 5), (7, 21), (20, 21)]
#arr = [(1, 3), (2, 4), (5, 7), (6, 8)]
arr = [[1,3], [2,4], [5,7], [6,8]]
overLapStack(arr)
