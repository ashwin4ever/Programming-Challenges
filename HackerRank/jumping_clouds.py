#Jumping over the clouds




n , k = map(int , input().split(' '))

c = list(map(int , input().strip().split(' ')))

print(100 - sum(1 + 2 * c[i] for i in range(0 , n , k)))


      

      


