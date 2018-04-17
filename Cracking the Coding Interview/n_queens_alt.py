#N Queens opt


def placeQueens(q , n , board):


      for r in range(n):

            if canPlace(q , r , board):
                  board[q] = r

                  if q == n - 1:
                        print('Queens: ' , board)

                  placeQueens(q + 1 , n , board)


def canPlace(q , r , board):

      #board[row] = col
      #board[0] = 1 means at 0th row queen is at 1st col

      for i in range(q):

            if (board[i] == r
                or
                abs(i - q) == abs(board[i] - r)
                ):
                  return False

      return True

            
n = 6
board = [0] * n

placeQueens(0 , n , board)
