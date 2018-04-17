# Hacker Rank Practice
# Grading STudents


# Function compute grades
def solve(grades):
      result = []
      next_five = 0
      for g in grades:

            if g < 38:
                  result.append(g)

            else:
                  for i in range(g , 101):
                        if i % 5 == 0:
                              if i - g < 3:
                                    result.append(i)
                                    break
                              else:
                                    result.append(g)
                                    break

      return result
                                    
      
n = int(input().strip())
grades = []

for g in range(n):

      points = int(input().strip())
      grades.append(points)

result = solve(grades)
print("\n".join(map(str , result)))
