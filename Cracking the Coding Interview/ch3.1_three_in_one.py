#Three in One: Describe how you could use a
#single array to implement three stacks.


class TwoStack:

      def __init__(self , n):

            self.size = n
            self.arr = [None] * n
            self.top1 = -1
            self.top2 = self.size

      def isEmpty1(self):
            return self.top1 == -1

      def isEmpty2(self):
            return self.top2 == self.size

      def push1(self , val):

            assert self.top1 < self.top2 - 1 , "No space in Stack 1"
            self.top1 += 1
            self.arr[self.top1] = val

      def push2(self , val):
            assert self.top1 <= self.top2 - 1, "Not enough space"

            self.top2 -= 1
            self.arr[self.top2] = val

      def pop(self , stackNum):

            if stackNum == 1:
                  assert not self.isEmpty1() , "Stack 1 is empty"
                  d = self.arr[self.top1]
                  self.top1 -= 1
                  return d
            elif stackNum == 2:
                  assert not self.isEmpty2() , "Stack 2 is empty"
                  d = self.arr[sel.top2]
                  self.top2 += 1
                  return d


t = TwoStack(5)
t.push1(1)
t.push1(2)
t.push1(3)
t.push1(4)
t.push2(3)
print(t.pop(1))
