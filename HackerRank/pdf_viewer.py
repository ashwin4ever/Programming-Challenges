# Designer PDF Viewer



n = [int(x) for x in input().split(' ') if int(x) <= 7]

word = [n[ord(x) - ord('a')] for x in input()]
#print(word)
print(len(word) * max(word))


