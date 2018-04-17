#Climbing the Leaderboard

num_players = int(input())

player_scores = [int(x) for x in input().split(' ')]
player_scores.sort(reverse = True)

alice_level = int(input())

alice_scores = [int(x) for x in input().split(' ')]
alice_scores.sort()

leaderBoard = []

def assign_player_rank(playerScores):
      leaderBoard = []
      temp = playerScores[0];
      prevRank = 1
      for i in range(len(playerScores)):

            if temp == playerScores[i]:
                  leaderBoard.append(prevRank)
            else:
                  prevRank += 1
                  leaderBoard.append(prevRank)
            temp = playerScores[i]

      leaderBoard.sort()
      return leaderBoard



def get_alice_ranking(level , aliceScores , cur_rank , player_scores):

      max_rank = max(cur_rank)
      alice_rank = []
      #print(cur_rank)
      idx = []
      rank = 0
      for i in range(level):
            
            if aliceScores[i] < min(player_scores):
                  alice_rank.append(max_rank + 1)
                  idx.append(aliceScores[i])
                  #aliceScores.pop(i)
                  
            elif aliceScores[i] > max(player_scores):
                  alice_rank.append(min(cur_rank))
                  idx.append(aliceScores[i])
                  #aliceScores.pop(i)


      #print(aliceScores)
      #print(idx)
      for i in idx:
            aliceScores.remove(i)

      for i in range(len(aliceScores)):
            
            for j in range(len(player_scores)):
                  
                  if aliceScores[i] > player_scores[j]:
                        #print(rank , 
                        rank = cur_rank[j]
                        #cur_rank[j] = cur_rank[j] + 1
                        #print(rank , aliceScores[i] , cur_rank[j] , player_scores[j] , j)
                        break
                  
                  elif aliceScores[i] < player_scores[j]:
                        rank = cur_rank[j] + 1
                        
                  elif aliceScores[i] == player_scores[j]:
                        rank = cur_rank[j]
                        #print(rank , aliceScores[i] , cur_rank[j] , player_scores[j] , j)
                        break
                  
            alice_rank.append(rank)

      alice_rank.sort(reverse = True)
            
      return alice_rank

      
            
#print(assign_player_rank(player_scores))

cur_rank = assign_player_rank(player_scores)

ar = get_alice_ranking(alice_level , alice_scores , cur_rank , player_scores)

for a in ar:
      print(a)
      
