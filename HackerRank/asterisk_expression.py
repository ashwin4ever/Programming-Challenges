#Asterisk Expressions

# -- 3*2**3**2*5
# -- 10100100101
# - 4*5**3

import sys

n = int(input())


expL = []

for i in range(n):
      s = input()
      expL.append(s)

for i in expL:
      exp = i

      num_digits = sum(int(d.isdigit()) for d in exp)
      num_chars = exp.count('*')

      dig = 1
      e = 1
      temp_e = 1
      ast_count = 0
      found_digit = False
      yes_digit = False
      temp_e2 = 1
      q = 1


      
      if exp[0] == '*' or exp[len(exp) - 1] == '*':
            print('Syntax Error')
            found_digit = False
            

      if num_chars == 0 and num_digits != 0:
            print(int(exp) % 1000000007)
            found_digit = False
            q = 0
      
      if num_chars != 0 and num_digits == 0:
            print('Syntax Error')
            found_digit = False
            q = 0
      
      if exp[0] != '*' and exp[len(exp) - 1] != '*':
            if exp.count('*') == 2:
                  print(pow(int(exp[0 : exp.find('*')]) , int(exp[exp.find('**') + 2 : ]) , 1000000007))
                  #print(pow(int(exp[0]) , int(exp[len(exp) - 1]) , 1000000007))
                  #found_digit = True
                  q = 0
                  continue
                  #break

            if exp.count('*') == 1:
                  print((int(exp[0 : exp.find('*')]) * int(exp[exp.find('*') + 1 : ])) % 1000000007)
                  #found_digit = True
                  q = 0
                  #break
                  continue

            for i in range(1 , len(exp) - 1):

                  #print(exp[i])
                  if(exp[i].isdigit()) and q != 0:
                        #print(exp[i])
                        found_digit = True
                        break
                        #q = 0

                  else:
                        found_digit = False
                        

            if not found_digit:
                  print('Syntax Error')
                  found_digit = False

      

      if found_digit and q != 0:
      
            for i in range(0 , len(exp)):
            
            # - 4*5**3
            # -- 3*2**3**2*5
            # 473289473297432***432794324392
                  if i == 0:
                        dig *= int(exp[0])
                  #print(dig , i)
                  if i + 1 < len(exp) and i - 1 >= 0 and i + 2 < len(exp):
                        #print('exp: ' , exp[i] , i)
                        if exp[i] == '*' and exp[i + 1] == '*' and exp[i + 2] == '*':
                              print('Syntax Error')
                              found_digit = False
                              break
                        if exp[i] == '*' and exp[i + 1] == '*':
                              if ast_count >= 1:
                                    e = int(exp[i + 2])
                                    #temp_e2 = int(exp[i - 1]) ** int(exp[i + 2])
                                    temp_e2 = pow(int(exp[i - 1]) , int(exp[i + 2]) , 1000000007)
                                    ast_count += 1
                                    i = i + 2
                              else:
                                    e = pow(int(exp[i - 1]) , int(exp[i + 2]) , 1000000007)
                                    ast_count += 1
                                    i = i + 2
                                    temp_e = e
                                    e = 1
                              
                         
                  elif exp[i].isdigit() and i != 0 and ast_count >= 2:
                  
                        #print('is digit: ' ,exp[i] , i)
                        dig *= int(exp[i])
                        yes_digit = True
            if ast_count == 1:
                  dig = 1
       


      #print(dig , e , temp_e , temp_e2)
      if found_digit and q!= 0:
            if num_chars % 2 == 0 and yes_digit:
                  print((dig * pow(temp_e , e , 1000000007)))
            elif num_chars % 2 != 0 and yes_digit:
                  print((temp_e * temp_e2))
            elif num_chars % 2 != 0 and not yes_digit:
                  print((int(exp[0]) * temp_e))
            else:
                  print((1 * temp_e))

                        
                  
            
                  
                  
