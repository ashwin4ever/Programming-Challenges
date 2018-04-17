#Modular Exponentiation for large numbers


a = 450
b = 768
c = 517


def modExp(a , b , c):


      res = 1

      while b:

            if b & 1:
                  res = res * a

            b = b >> 1 #b = b / 2
            a = a * a

      print(res % c)


modExp(a , b , c)
