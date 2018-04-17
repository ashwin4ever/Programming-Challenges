#Simple Iterator


class yrange:

      def __init__(self , n):

            self.l = 0
            self.h = n


      def __iter__(self):
            return self


      def next(self):

            if self.l < self.h:
                  i = self.l
                  self.l += 1
                  return i
            else:
                  raise StopIteration()
