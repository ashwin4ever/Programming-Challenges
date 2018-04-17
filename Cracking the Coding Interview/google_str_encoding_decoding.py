#String encoding decoding



def encode(arr , sep):

      n = len(arr)

      res = ''

      'hello world'

      for s in arr:

            res += s + sep

      res = res[0 : len(res) - 1]

      return res

def decode(s , sep , res):

      print(s)

      if sep not in s:
            res.append(s)
            return res

      idx = s.index(sep)
      
      res.append(s[0: idx])

      return decode(s[idx + 1 : ] , sep , res)
      

      

arr = ['hello' , 'world' , 'abchdjdhjkd']
sep = '-'
#print(encode(arr , '-'))
s = encode(arr , sep)
print(s)
res = decode(s , sep , [])
print(res)
