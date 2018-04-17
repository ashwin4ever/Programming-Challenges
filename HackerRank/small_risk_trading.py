#Small Risk Trading



n , k = [int(x) for x in input().split(' ')]

p = [float(x) for x in input().strip().split(' ')]
x = [float(x) for x in input().strip().split(' ')]
y = [float(x) for x in input().strip().split(' ')]

l = zip(p , x , y)

stocks = [x for x in l]

loss = []
min_loss = {}
min_temp = 99999999.00
max_temp = 0.00
max_profit = {}

idx = []

for i in range(n):
      min_l = (1 - stocks[i][0]) * stocks[i][2]
      if min_l < 0:
            idx.append(i)
      else:
            loss.append(min_l)

#print(loss)

if len(idx) != 0:
      for i in idx:
            p.pop(i)
            x.pop(i)
            y.pop(i)

new_stocks = [x for x in zip(p , x , loss)]
ns = []
#new_stocks.sort()
#print(new_stocks)

for i in range(n):
      calc = (new_stocks[i][0] * new_stocks[i][1]) - new_stocks[i][2]
      ns.append(calc)
#print('\n')
#print('ns: ' , ns)
result = list(filter(lambda x : x > 0.0 , ns))
result.sort(reverse = True)
#print('\n')
#print('result: ' , result)

if len(result) == 1:
      print(format(round(result[0] , 2) , ".2f"))
else:
      if k == 1:
            print(format(round(max(result[0 : k]) , 2) , '.2f'))
      else:
            print(format(round(sum(result[0 : k]) , 2) , '.2f'))
      
      

#print(loss)
