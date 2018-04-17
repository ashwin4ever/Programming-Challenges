# Hacker Rank Practice
# Migratory Birds


def migratoryBirds(n , ar):

      bird = {}

      for i in ar:
            if i in bird:
                  bird[i] += 1
            else:
                  bird[i] = 1

      bird = sorted(bird , key = bird.get , reverse = True)
      
      return bird[0]
      

n = int(input().strip())
ar = list(map(int , input().strip().split(' ')))
result = migratoryBirds(n , ar)
print(result)
