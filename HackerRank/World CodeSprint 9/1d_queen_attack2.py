#Queens attack 1d


def queenAttack(board , qr , qc):

      n = len(board)
      obs = False
      count = 0

      #right
      for i in range(qr + 1 , n):

            print('r: ' ,i)

            if board[i] == 0:
                  count += 1 
                  #board[i] = 'q'

      #left
      for i in range(1 , qr):

             if board[i] == 0:
                  print('l: ' , i)
                  count += 1
                  #board[i] = 'q'

      #check diagonals
      for i in range(1 , n):

            if abs(qr - i) != abs(board[qr] - board[i]):
                  count += 1
                  print(qr , i , board[qr] , board[i])
                  if qr + 1 < n:
                        qr += 1
                        board[qr] = qc

      #print(count)

      return count

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]

board = [0] * (n + 1)

qr,qc = input().strip().split(' ')
qr,qc = [int(qr),int(qc)]

#print(board)
board[qr] = qc
count = 0
#print(board)


for a in range(k):

      r , c = input().split(' ')
      r , c = int(r) , int(c)
      board[r] = c

count = queenAttack(board , qr , qc)


print(count)
      
      
