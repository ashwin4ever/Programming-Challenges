# Compare the Triplets

'''
Alice and Bob each created one problem for HackerRank.
A reviewer rates the two challenges, awarding
points on a scale from to for three categories:
problem clarity, originality, and difficulty.

We define the rating for Alice's challenge
to be the triplet , and the rating for Bob's
challenge to be the triplet .

Your task is to find their comparison scores
by comparing with , with , and with .

    If , then Alice is awarded point.
    If , then Bob is awarded point.
    If , then neither person receives a point.

Given and , can you compare the two challenges
and print their respective comparison points?
'''

#get alice's values
a0 , a1 , a2 = map(int , (input().split(' ')))
aliceSum = 0

#get bob's values
b0 , b1 , b2 = map(int , (input().split(' ')))
bobSum = 0

if a0 > b0:
      aliceSum += 1
elif a0 == b0:
      pass
else:
      bobSum += 1

if a1 > b1:
      aliceSum += 1
elif a1 == b1:
      pass
else:
      bobSum += 1
if a2 > b2:
      aliceSum += 1
elif a2 == b2:
      pass
else:
      bobSum += 1

print(aliceSum , bobSum)
