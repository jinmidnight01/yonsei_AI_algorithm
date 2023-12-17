# Q1: -40
game_board = ['O','X','O',
              'X',' ',' ',
              ' ','X',' ']

price_board = [10, 10, 10,
              10, 10, 10,
              10, 10, 10]


# # Q2: -5
# game_board = ['X',' ',' ',
#               ' ','O',' ',
#               ' ',' ',' ']

# price_board = [10, 10, 10,
#               10, 10, 10,
#               10, 10, 10]


# # Q3: -8
# game_board = ['O','X',' ',
#               'X','O',' ',
#               'X',' ',' ']

# price_board = [2, 2, 10,
#               1, 4, 5,
#               3, 5, 16]


# # Q4: 1
# game_board = [' ',' ',' ',
#               ' ',' ',' ',
#               ' ',' ',' ']

# price_board = [2, 2, 10,
#               1, 4, 5,
#               3, 5, 16]


# # Q5: 11
# game_board = ['X','O',' ',
#               'X',' ','X',
#               'O',' ','O']

# price_board = [2, 2, 10,
#               2, 36, 2,
#               2, 4, 2]


# # Q6: 8
# game_board = [' ',' ',' ',
#               'X',' ',' ',
#               ' ',' ',' ']

# price_board = [2, 2, 10,
#               2, 36, 2,
#               2, 4, 2]


# # Q7: 113
# game_board = [' ',' ',' ',
#               ' ',' ','O',
#               ' ','X',' ']

# price_board = [52, 34, 61,
#               13, 29, 76,
#               45, 81, 3]


# # Q8: -13
# game_board = [' ',' ',' ',
#               ' ',' ',' ',
#               ' ',' ','X']

# price_board = [52, 34, 61,
#               13, 29, 76,
#               45, 81, 3]


# # Q9: -10
# game_board = [' ',' ','X',
#               ' ','O',' ',
#               ' ',' ',' ']

# price_board = [95, 59, 36,
#               76, 85, 43,
#               48, 34, 72]


# # Q10: -5
# game_board = [' ',' ',' ',
#               ' ',' ',' ',
#               ' ',' ',' ']

# price_board = [95, 59, 36,
#               76, 85, 43,
#               48, 34, 72]

###################################################################
import math

def empty_cells(board):
  cells = []
  for x, cell in enumerate(board):
    if cell == ' ':
      cells.append(x)
  return cells

def valid_move(x):
  return x in empty_cells(game_board)

def move(x, player):
  if valid_move(x):
    game_board[x] = player
    return True
  return False

def draw(board):
  for i, cell in enumerate(board):
    if i % 3 == 0:
      print('\n---------------')
    print('|', cell, '|', end='')
  print('\n---------------\n')

def evaluate_MAX(board):
  X_pos = [i for i, value in enumerate(board) if value == 'X']
  X_cost = sum([price_board[i] for i in X_pos])
  O_pos = [i for i, value in enumerate(board) if value == 'O']
  O_cost = sum([price_board[i] for i in O_pos])
  if check_win(board, 'X'):
    score = (X_cost + O_cost) - X_cost
  elif check_win(board, 'O'):
    score = 0 - X_cost
  else:
    score = ((X_cost + O_cost) / 2) - X_cost
  return score

def check_win(board, player):
  win_cof = [
    [board[0], board[1], board[2]],
    [board[3], board[4], board[5]],
    [board[6], board[7], board[8]],
    [board[0], board[3], board[6]],
    [board[1], board[4], board[7]],
    [board[2], board[5], board[8]],
    [board[0], board[4], board[8]],
    [board[2], board[4], board[6]]
  ]
  return [player, player, player] in win_cof

def game_over(board):
  return check_win(board, 'X') or check_win(board, 'O') or len(empty_cells(board)) == 0

def minimax(board, depth, maxPlayer):
  pos = -1
  if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
    return -1, evaluate_MAX(board)
  
  if maxPlayer:
    value = -math.inf
    for p in empty_cells(board):
      board[p] = 'X'
      x, score = minimax(board, depth - 1, False)
      board[p] = ' '
      if score > value:
        value = score
        pos = p
  else:
    value = math.inf
    for p in empty_cells(board):
      board[p] = 'O'
      x, score = minimax(board, depth - 1, True)
      board[p] = ' '
      if score < value:
        value = score
        pos = p
  return pos, value

maxPlayer = 'X'
minPlayer = 'O'

if game_board.count(' ') % 2 == 1:
  starting_player = maxPlayer
else:
  starting_player = minPlayer

print('\n초기 보드')
if starting_player == minPlayer:
  draw(game_board)
  print('\nMIN 차례 (O)')
  i, _ = minimax(game_board, 9, False)
  move(i, minPlayer)

draw(game_board)
while True:
  if len(empty_cells(game_board)) == 0 or game_over(game_board):
    break
  
  print('\nMAX 차례 (X)')
  player_move, _ = minimax(game_board, 9, True)
  move(player_move, maxPlayer)
  draw(game_board)
  
  i, _ = minimax(game_board, 9, False)
  if i == -1:
    break
  print('\nMIN 차례 (O)')
  move(i, minPlayer)
  draw(game_board)

if check_win(game_board, 'X'):
  print('\n게임 결과: X 승리!')
elif check_win(game_board, 'O'):
  print('\n게임 결과: O 승리!')
else:
  print('\n게임 결과: 비겼습니다!')
print('MAX 점수:', evaluate_MAX(game_board))
draw(game_board)