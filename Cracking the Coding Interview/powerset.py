#print power set



def powerSet(arr):

      n = len(arr)

      num_sets = 1 << n
      print(num_sets)

      res = []
      temp = ''

      for i in range(num_sets):
            temp = ''

            for j in range(n):

                  #check if bit is set
                  if (i & (1 << j)):
                        temp += arr[j]
                        

                  
            print(temp , ' ' , end = '') 

                        
                  
            

      print(res)

powerSet(['a' , 'b' , 'c' , 'd' , 'e'])
            
