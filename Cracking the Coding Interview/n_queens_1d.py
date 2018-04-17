#N Queens 1D



def placeQueens(q , board):

      n = len(board)

      for row in range(n):

            if isSafe(q , board , row):
                  board[q] = row
                  #print(q , board)
                  #printBoard(board)

                  if q == n - 1:
                        #print(board)
                        printBoard(board)

                  placeQueens(q + 1 , board)


def isSafe(q , board , row):

      for i in range(q):

            #print(i , q , row)

            if board[i] == row:
                  return False

            if (abs(row - board[i]) == abs(i - q)):
                  return False

      return True

def printBoard(board):

      n = len(board)

      for i in range(n):
            for j in range(n):

                  if j == board[i]:
                        print('Q' , end = ' ')
                  else:
                        print('-' , end = ' ')

            print()
                  

n = 5
board = [-1] * n
placeQueens(0 , board)
