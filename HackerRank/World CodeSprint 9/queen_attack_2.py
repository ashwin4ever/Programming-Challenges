#Queens attack 2



def makeBoard(n):

      board = [[0 for c in range(0 , n + 1)] for r in range(0 , n + 1)]

      return board


def queenAttack(board , n , qr , qc):

      #q = (4 , 4)
      count = 0
      obs = False

      #bottom
      if qr != n:
            j = qc
            for i in range(qr + 1 , n + 1):

                  if board[i][j] != 'x':
                        count += 1
                        #board[i][j] = 'q'
                  else:
                        obs = True
                        break

      #top
      for i in range(qr - 1 , 0 , -1):

            if board[i][qc] != 'x':
                  count += 1
                  #board[i][qc] = 'q'
            else:
                  obs = True
                  break

      #right
      for j in range(qc + 1 , n + 1):
            #print(qr , j , end = ' ')
            if board[qr][j] != 'x':
                  count += 1
                  #board[qr][j] = 'q'
            else:
                  obs = True
                  break

      #left
      for j in range(qc - 1 , 0 , -1):
            #print(qr , j , end = ' ')
            if board[qr][j] != 'x':
                  count += 1
                  #board[qr][j] = 'q'
            else:
                  obs = True
                  break
            

      #upper right diag
      i , j = qr - 1 , qc + 1

      while (i >= 1 and j <= n):

            if board[i][j] != 'x':
                  count += 1
                  #board[i][j] = 'q'
            else:
                  obs = True
                  break
            i -= 1
            j += 1
      

      #upper left diag
      i , j = qr - 1 , qc - 1

      while (i >= 1 and j >= 1):

            if board[i][j] != 'x':
                  count += 1
                  #board[i][j] = 'q'
            else:
                  obs = True
                  break
            i -= 1
            j -= 1


      #bottom left diag
      i , j = qr + 1 , qc - 1

      while (i <= n and j >= 1):

            if board[i][j] != 'x':
                  count += 1
                  #board[i][j] = 'q'
            else:
                  obs = True
                  break
            i += 1
            j -= 1

      #bottom right diag
      i , j = qr + 1 , qc + 1

      while (i <= n and j <= n):

            if board[i][j] != 'x':
                  count += 1
                  #board[i][j] = 'q'
            else:
                  obs = True
                  break
            i += 1
            j += 1
      
            
      return count


def printBoard(board):

      n = len(board)

      for i in range(1 , n):
            for j in range(1 , n):
                  print(board[i][j] , end = '  ')

            print()

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]

qr,qc = input().strip().split(' ')
qr,qc = [int(qr),int(qc)]

board = makeBoard(n)


#printBoard(board)
#board[3][5] = -1
board[qr][qc] = 'Q'

#printBoard(board)

for a0 in range(k):
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    board[r][c] = 'x'
    
if k == 0 and qr == qc:
      print(3 * (n - 1))

else:
      print(queenAttack(board , n , qr , qc))

#print()
#printBoard(board)
                  
                  

      

      
            

      
