

def attackQueen(board , qr , qc):

      n = len(board)
      count = 0

      #up/left
      for i in range(1 , qr):

            if board[i] == 0:
                  count += 1

      #down/right
      for i in range(qr + 1 , n):

            if board[i] == 0:
                  count += 1




      #upper right diag
      i , j = qr - 1 , qc + 1

      while (i > = 1 and j <= n):

            if 




      return count




n,k = input().strip().split(' ')
n,k = [int(n),int(k)]

board = [0] * (n + 1)

qr,qc = input().strip().split(' ')
qr,qc = [int(qr),int(qc)]

board[qr] = qc

for a in range(k):

      r , c = input().split(' ')
      r , c = int(r) , int(c)
      board[r] = c


count = attackQueen(board , qr , qc)
print(count)
