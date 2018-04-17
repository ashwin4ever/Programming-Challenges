#viral Advertising


n = int(input())

m = 5
ppl = 0
temp = 0

for i in range(n):

      if i == 0:
            ppl = (m // 2)
            temp = ppl
            m = temp * 3
      else:
            temp = (m // 2)
            ppl += temp
            m = temp * 3
            
                

      #print(ppl , m)


print(ppl)
      
      
