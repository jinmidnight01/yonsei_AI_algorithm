# 휴리스틱 함수
def h(s) :
  ###### Part1 ######
  global rows, cols, blank
  v = 0
  for i in range(rows):
    for j in range(cols):
      v += abs(i - ((s[i][j] - 1) // cols))
      v += abs(j - (s[i][j] - 1) % cols)
  return v
  ###### Part1 end ######

# 리스트의 리스트인 state전체를 하나의 정수로 표현하는 함수
def int_encoded_state(state):
  global rows, cols
  c = 0
  for i in range(rows):
    for j in range(cols):
      c = c * (rows * cols + 1) + state[i][j]
  return c

# 목표하는 상태인지 확인하는 함수
def is_goal(state):
  ###### Part2 ######
  for i in range(rows):
    for j in range(cols):
      if state[i][j] == cols * i + j + 1:
        return False
  return True
  ###### Part2 end ######

# 현재 상태인 state에서 (bi + di, bj + dj)에 위치한 타일을
# 빈칸인 (bi, bj) 위치로 움직인 후의 상태를 리턴하는 함수
def state_after_move(state, bi, bj, di, dj):
  global rows, cols, blank
  # state_next : state 배열에서 타일을 이동시키고 난 뒤의 배열
  state_next = [[state[i][j] for j in range(cols)] for i in range(rows)]
  state_next[bi + di][bj + dj] = blank
  return state_next

# 행과 열의 수를 입력받음
rows, cols = map(int, input().split())

# 보드의 초기 상태를 입력받음
blank = rows * cols
s_init = list()
for i in range(rows):
  s_init.append(list(map(int, input().split())))
  
num_steps = -1
X = set()
Q = list()
h_root = h(s_init)
f_root = h_root
Q.append((f_root, 0, h_root, s_init))

####### Part3 #######
while len(Q) > 0:
####### Part3 end #######

 ###### Part4 ######
  min_idx = 0
  min_f = Q[0][0]
  for i in range(1, len(Q)):
    if Q[i][0] < min_f:
      min_idx = i
      min_f = Q[i][0]
  _, g_n, h_n, s = Q.pop(min_idx)
  ###### Part4 end ######
  
  if is_goal(s):
    ###### Part5 ######
    num_steps = g_n
    ###### Part5 end ######
    break
  
  if int_encoded_state(s) not in X: # s를 표현하는 정수가 X에 들어있지 않다면
    bi, bj = -1, -1
    for i in range(rows):
     for j in range(cols):
       if s[i][j] == blank:
         bi, bj = i, j
         break

    ###### Part6 ######
    X.add(int_encoded_state(s))
    g_nprime = g_n + 1
    for (di, dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
      s_nprime = state_after_move(s, bi, bj, di, dj)
      h_nprime = h(s_nprime)
      f_nprime = g_nprime + h_nprime
      Q.append((f_nprime, g_nprime, h_nprime, s_nprime))
    ###### Part6 end ######

print(num_steps)