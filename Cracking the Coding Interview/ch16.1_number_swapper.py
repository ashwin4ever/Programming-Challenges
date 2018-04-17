#16.1 Number swapper



def swap(a , b):

      b = a + b
      a = b - a
      b = b - a



      print('a: ' , a , 'b: ' , b)


def swapBits(a , b):

      a = a ^ b
      b = a ^ b
      a = a ^ b

      print('a: ' , a , 'b: ' , b)
      


a , b = 3 , 4
print('a: ' , a , 'b: ' , b)
swap(a , b)
swapBits(a , b)
