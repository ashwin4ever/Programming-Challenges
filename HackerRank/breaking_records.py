# Hacker Rank Practice
# Breaking the Records


def getRecords(s):

      min_s = s[0]
      max_s = s[0]
      min_c = 0
      max_c = 0

      for i in s[1 : ]:
            if i < min_s:
                  min_s = i
                  min_c += 1

            if i > max_s:
                  max_s = i
                  max_c += 1

      return [max_c , min_c]


n = int(input().strip())
s = list(map(int , input().strip().split(' ')))

result = getRecords(s)
print(' '.join(map(str , result)))
