#16.10 Living People


from collections import defaultdict

class Person:

      def __init__(self , by , dy):

            self.birth = by
            self.death = dy




def getMaxYear(people):

      record = defaultdict(int)

      for p in people:
            record[p.birth] += 1
            record[p.death + 1] -= 1

            
      print(record)
      maxYear = sorted(record , key = record.get , reverse = True)[0]

      print(maxYear)
      
      
      



p1 = Person(10 , 18)
p2 = Person(10 , 17)
p3 = Person(12 , 18)
p4 = Person(15 , 20)
p5 = Person(10 , 18)
p6 = Person(18 , 21)
people = [p1 , p2 , p3 , p4 , p5 , p6]

getMaxYear(people)

#print(people[0].birth)
