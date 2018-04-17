#Grading students



n = int(input().strip())

res = []


def get5(num):

      while num % 5:
            num += 1

      return num


for i in range(n):

      grade = int(input().strip())

      if grade < 38:
            res.append(grade)

      else:
            mul = get5(grade)

            diff = mul - grade

            if diff < 3:
                  res.append(mul)
            else:
                  res.append(grade)



for g in res:
      print(g)

      
