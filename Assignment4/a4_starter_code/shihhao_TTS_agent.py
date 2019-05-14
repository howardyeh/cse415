'''shihhao_TTS_agent.py
An agent that plays Toro-Tile Straight,
can use iterative deepening search and minmax algorithm + alpha beta pruning algorithm
in the iterative part, if time is enough it will keep finding deeper solution.

'''

from TTS_State import TTS_State
import time


USE_CUSTOM_STATIC_EVAL_FUNCTION = False

# =======================================
K = 0
whichSide = ''
choosed_location = (0,0)
current_state_static_val = -1000.0
n_states_expanded = 0
n_static_evals_performed = 0
max_depth_reached = 0
n_ab_cutoffs = 0
t0 = 0.0
good_path = []
normal_path = []
use_path = []
state_col = 0
state_row = 0

# =======================================

class MY_TTS_State(TTS_State):
  def static_eval(self):
    if USE_CUSTOM_STATIC_EVAL_FUNCTION:
      return self.custom_static_eval()
    else:
      return self.basic_static_eval()

  def basic_static_eval(self):
    # print(self.board)
    C = 0
    global K
    global whichSide
    global state_row
    global state_col

    count = 0
    count_blank = 0
    
    if whichSide=='W':
      otherSide = 'B'
    elif whichSide=='B':
      otherSide = 'W'


    for i in range(len(self.board)):
      for j in range(len(self.board[0])):
        if self.board[i][j]!='-' and self.board[i][j]!=otherSide:
          # print("detect my spot!!!!!")

          # ===== white side =====
          # ===== count left =====
          if self.board[i][j]==whichSide: count = 1
          elif self.board[i][j]==' ': count_blank = 1 
          ptrj = j+1
          if ptrj>=len(self.board[0]): ptrj = 0

          
          while(self.board[i][ptrj]!='-' and self.board[i][ptrj]!=otherSide and ptrj!=j):
            # print(i, ptrj)
            if self.board[i][ptrj]==whichSide: count += 1
            elif self.board[i][ptrj]==' ': count_blank += 1 

            ptrj+=1
            if ptrj>=len(self.board[0]): ptrj = 0

          if count==2 and count_blank==K-2:
            C+=1

          # ===== count down =====
          if self.board[i][j]==whichSide: count = 1
          elif self.board[i][j]==' ': count_blank = 1 
          ptri = i+1
          if ptri>=len(self.board): ptri = 0

          
          while(self.board[ptri][j]!='-' and self.board[ptri][j]!=otherSide and ptri!=i):
            # print(i, ptrj)
            if self.board[ptri][j]==whichSide: count += 1
            elif self.board[ptri][j]==' ': count_blank += 1 

            ptri+=1
            if ptri>=len(self.board): ptri = 0

          if count==2 and count_blank==K-2:
            C+=1

          # ===== count tilt(left) =====
          if self.board[i][j]==whichSide: count = 1
          elif self.board[i][j]==' ': count_blank = 1 
          ptri = i+1
          ptrj = j+1
          if ptri>=len(self.board): ptri = 0
          if ptrj>=len(self.board[0]): ptrj = 0
          
          while(self.board[ptri][ptrj]!='-' and self.board[ptri][ptrj]!=otherSide and (ptri!=i or ptrj!=j)):
            # print(i, ptrj)
            if self.board[ptri][ptrj]==whichSide: count += 1
            elif self.board[ptri][ptrj]==' ': count_blank += 1 

            ptri+=1
            ptrj+=1
            if ptri>=len(self.board): ptri = 0
            if ptrj>=len(self.board[0]): ptrj = 0

          if count==2 and count_blank==K-2:
            C+=1

          # ===== count tilt(right) =====
          if self.board[i][j]==whichSide: count = 1
          elif self.board[i][j]==' ': count_blank = 1 
          ptri = i+1
          ptrj = j-1
          if ptri>=len(self.board): ptri = 0
          if ptrj<0: ptrj = len(self.board[0])-1
          
          while(self.board[ptri][ptrj]!='-' and self.board[ptri][ptrj]!=otherSide and (ptri!=i or ptrj!=j)):
            # print(i, ptrj)
            if self.board[ptri][ptrj]==whichSide: count += 1
            elif self.board[ptri][ptrj]==' ': count_blank += 1 

            ptri+=1
            ptrj-=1
            if ptri>=len(self.board): ptri = 0
            if ptrj<0: ptrj = len(self.board[0])-1

          if count==2 and count_blank==K-2:
            C+=1


    for i in range(len(self.board)):
      for j in range(len(self.board[0])):
        if self.board[i][j]!='-' and self.board[i][j]!=whichSideotherSide:
          # print("detect my spot!!!!!")

          # ===== black side =====
          # ===== count left =====
          if self.board[i][j]==otherSide: count = 1
          elif self.board[i][j]==' ': count_blank = 1 
          ptrj = j+1
          if ptrj>=len(self.board[0]): ptrj = 0

          
          while(self.board[i][ptrj]!='-' and self.board[i][ptrj]!=whichSide and ptrj!=j):
            # print(i, ptrj)
            if self.board[i][ptrj]==otherSide: count += 1
            elif self.board[i][ptrj]==' ': count_blank += 1 

            ptrj+=1
            if ptrj>=len(self.board[0]): ptrj = 0

          if count==2 and count_blank==K-2:
            C-=1

          # ===== count down =====
          if self.board[i][j]==otherSide: count = 1
          elif self.board[i][j]==' ': count_blank = 1 
          ptri = i+1
          if ptri>=len(self.board): ptri = 0

          
          while(self.board[ptri][j]!='-' and self.board[ptri][j]!=whichSide and ptri!=i):
            # print(i, ptrj)
            if self.board[ptri][j]==otherSide: count += 1
            elif self.board[ptri][j]==' ': count_blank += 1 

            ptri+=1
            if ptri>=len(self.board): ptri = 0

          if count==2 and count_blank==K-2:
            C-=1

          # ===== count tilt(left) =====
          if self.board[i][j]==otherSide: count = 1
          elif self.board[i][j]==' ': count_blank = 1 
          ptri = i+1
          ptrj = j+1
          if ptri>=len(self.board): ptri = 0
          if ptrj>=len(self.board[0]): ptrj = 0
          
          while(self.board[ptri][ptrj]!='-' and self.board[ptri][ptrj]!=whichSide and (ptri!=i or ptrj!=j)):
            # print(i, ptrj)
            if self.board[ptri][ptrj]==otherSide: count += 1
            elif self.board[ptri][ptrj]==' ': count_blank += 1 

            ptri+=1
            ptrj+=1
            if ptri>=len(self.board): ptri = 0
            if ptrj>=len(self.board[0]): ptrj = 0

          if count==2 and count_blank==K-2:
            C-=1

          # ===== count tilt(right) =====
          if self.board[i][j]==otherSide: count = 1
          elif self.board[i][j]==' ': count_blank = 1 
          ptri = i+1
          ptrj = j-1
          if ptri>=len(self.board): ptri = 0
          if ptrj<0: ptrj = len(self.board[0])-1
          
          while(self.board[ptri][ptrj]!='-' and self.board[ptri][ptrj]!=whichSide and (ptri!=i or ptrj!=j)):
            # print(i, ptrj)
            if self.board[ptri][ptrj]==otherSide: count += 1
            elif self.board[ptri][ptrj]==' ': count_blank += 1 

            ptri+=1
            ptrj-=1
            if ptri>=len(self.board): ptri = 0
            if ptrj<0: ptrj = len(self.board[0])-1

          if count==2 and count_blank==K-2:
            C-=1

    # print("the value is = ",C)
    return C

  def custom_static_eval(self):
    C = 0
    global K
    global whichSide
    global state_row
    global state_col

    count = 0
    count_blank = 0
    
    if whichSide=='W':
      otherSide = 'B'
    elif whichSide=='B':
      otherSide = 'W'


    for i in range(len(self.board)):
      for j in range(len(self.board[0])):
        if self.board[i][j]==whichSide:
          C+=self.go_UD(i,j,whichSide,K)
          C+=self.go_LR(i,j,whichSide,K)
          C+=self.go_Lt(i,j,whichSide,K)
          C+=self.go_Rt(i,j,whichSide,K)
        elif self.board[i][j]==otherSide:
          C-=self.go_UD(i,j,otherSide,K)
          C-=self.go_LR(i,j,otherSide,K)
          C-=self.go_Lt(i,j,otherSide,K)
          C-=self.go_Rt(i,j,otherSide,K)

    return C

  def go_UD(self, i, j, whichSide, K):
    pi = i+1
    if pi>len(self.board)-1: pi = 0
    pj = j
    qi = i-1
    if qi<0: qi = len(self.board)-1
    qj = j
    num = 1
    headblock = True
    tailblock = True
    while self.board[pi][pj]==whichSide or self.board[qi][qj]==whichSide:
      if self.board[pi][pj]==whichSide:
        num+=1
        pi+=1
        if pi>len(self.board)-1: pi = 0
      elif self.board[pi][pj]==' ': headblock = False

      if self.board[qi][qj]==whichSide:
        num+=1
        qi-=1
        if qi<0: qi = len(self.board)-1
      elif self.board[pi][pj]==' ': tailblock = False 

      if num==K: break

    if num==K: return 10**K
    elif not headblock and not tailblock: return 10**num
    elif headblock and tailblock: return 0
    else: return 10**(num-1)

  def go_LR(self, i, j, whichSide, K):
    pj = j+1
    if pj>len(self.board[0])-1: pj = 0
    pi = i
    qj = j-1
    if qj<0: qj = len(self.board[0])-1
    qi = i
    num = 1
    headblock = True
    tailblock = True
    while self.board[pi][pj]==whichSide or self.board[qi][qj]==whichSide:
      if self.board[pi][pj]==whichSide:
        num+=1
        pj+=1
        if pj>len(self.board[0])-1: pj = 0
      elif self.board[pi][pj]==' ': headblock = False

      if self.board[qi][qj]==whichSide:
        num+=1
        qj-=1
        if qj<0: qj = len(self.board[0])-1
      elif self.board[pi][pj]==' ': tailblock = False 

      if num==K: break

    if num==K: return 10**K
    elif not headblock and not tailblock: return 10**num
    elif headblock and tailblock: return 0
    else: return 10**(num-1)

  def go_Lt(self, i, j, whichSide, K):
    pj = j+1
    if pj>len(self.board[0])-1: pj = 0
    pi = i+1
    if pi>len(self.board)-1: pi = 0
    qj = j-1
    if qj<0: qj = len(self.board[0])-1
    qi = i-1
    if qi<0: qi = len(self.board)-1
    num = 1
    headblock = True
    tailblock = True
    while self.board[pi][pj]==whichSide or self.board[qi][qj]==whichSide:
      if self.board[pi][pj]==whichSide:
        num+=1
        pi+=1
        pj+=1
        if pi>len(self.board)-1: pi = 0
        if pj>len(self.board[0])-1: pj = 0
      elif self.board[pi][pj]==' ': headblock = False

      if self.board[qi][qj]==whichSide:
        num+=1
        qi-=1
        qj-=1
        if qi<0: qi = len(self.board)-1
        if qj<0: qj = len(self.board[0])-1
      elif self.board[pi][pj]==' ': tailblock = False 

      if num==K: break

    if num==K: return 10**K
    elif not headblock and not tailblock: return 10**num
    elif headblock and tailblock: return 0
    else: return 10**(num-1)

  def go_Rt(self, i, j, whichSide, K):
    pj = j+1
    if pj>len(self.board[0])-1: pj = 0
    pi = i-1
    if pi<0: pi = len(self.board)-1
    qj = j-1
    if qj<0: qj = len(self.board[0])-1
    qi = i+1
    if qi>len(self.board)-1: qi = 0
    num = 1
    headblock = True
    tailblock = True
    while self.board[pi][pj]==whichSide or self.board[qi][qj]==whichSide:
      if self.board[pi][pj]==whichSide:
        num+=1
        pi-=1
        pj+=1
        if pi<0: pi = len(self.board)-1
        if pj>len(self.board[0])-1: pj = 0
      elif self.board[pi][pj]==' ': headblock = False

      if self.board[qi][qj]==whichSide:
        num+=1
        qi+=1
        qj-=1
        if qi>len(self.board)-1: qi = 0
        if qj<0: qj = len(self.board[0])-1
      elif self.board[pi][pj]==' ': tailblock = False 

      if num==K: break

    if num==K: return 10**K
    elif not headblock and not tailblock: return 10**num
    elif headblock and tailblock: return 0
    else: return 10**(num-1)


  def over_or_not(self, Side):
    # ================================
    # return False
    # ================================
    for i in range(len(self.board)):
      for j in range(len(self.board[0])):
        if self.board[i][j]==Side:
                    
          ptrj = j+1
          if ptrj>=len(self.board[0]): ptrj = 0
          count = 1
          while(self.board[i][ptrj]==Side and ptrj!=j):
            # print(i, ptrj)
            ptrj+=1
            if ptrj>=len(self.board[0]): ptrj = 0
            count+=1
          if count==K:
            return True

          ptri = i+1
          if ptri>=len(self.board): ptri = 0
          count = 1
          while(self.board[ptri][j]==Side and ptri!=i):
            ptri+=1
            if ptri>=len(self.board): ptri = 0
            count+=1
          if count==K:
            return True

          ptri = i+1
          ptrj = j+1
          if ptri>=len(self.board): ptri = 0
          if ptrj>=len(self.board[0]): ptrj = 0
          count = 1
          while(self.board[ptri][ptrj]==Side and (ptri!=i or ptrj!=j)):
            ptri+=1
            ptrj+=1
            if ptri>=len(self.board): ptri = 0
            if ptrj>=len(self.board[0]): ptrj = 0
            count+=1
          if count==K:
            return True

          ptri = i+1
          ptrj = j-1
          if ptri>=len(self.board): ptri = 0
          if ptrj<0: ptrj = len(self.board[0])-1
          count = 1
          while(self.board[ptri][ptrj]==Side and (ptri!=i or ptrj!=j)):
            ptri+=1
            ptrj-=1
            if ptri>=len(self.board): ptri = 0
            if ptrj<0: ptrj = len(self.board[0])-1
            count+=1
          if count==K:
            return True
    return False

def take_turn(current_state, last_utterance, time_limit):

    # ===========================================
    global choosed_location
    global t0
    # ===========================================
    t0 =time.time()

    # Compute the new state for a move.
    # Start by copying the current state.
    new_state = MY_TTS_State(current_state.board)

    # Fix up whose turn it will be.
    who = current_state.whose_turn
    new_who = 'B'  
    if who=='B': new_who = 'W'  
    new_state.whose_turn = new_who
    
    # Place a new tile
    # location = _find_next_vacancy(new_state.board)
    # if location==False: return [[False, current_state], "I don't have any moves!"]

    # ============================================

    results = parameterized_minimax(
       current_state=new_state,
       use_iterative_deepening_and_time = True,
       max_ply=6,
       use_default_move_ordering = False,
       alpha_beta=True, 
       time_limit=time_limit,
       use_custom_static_eval_function=True)
    # new_state.board[location[0]][location[1]] = who
    new_state.board[choosed_location[0]][choosed_location[1]] = who

    # Construct a representation of the move that goes from the
    # currentState to the newState.
    # move = location
    move = choosed_location

    # ============================================

    # Make up a new remark
    # new_utterance = "I'll think harder in some future game. Here's my move"
    new_utterance = find_utterance()

    return [[move, new_state], new_utterance]

def _find_next_vacancy(b):
    for i in range(len(b)):
      for j in range(len(b[0])):
        if b[i][j]==' ': return (i,j)
    return False

def moniker():
    return "A-Fool" # Return your agent's short nickname here.

def who_am_i():
    return """My name is A-Fool, created by Shih-Hao Yeh. \
I am a idiot."""

def get_ready(initial_state, k, who_i_play, player2Nickname):
    # do any prep, like eval pre-calculation, here.
    global K
    global whichSide
    global good_path
    global normal_path
    global state_col
    global state_row
    K = k
    whichSide = who_i_play
    state_row = len(initial_state.board)
    state_col = len(initial_state.board[0])

    for i in range(len(initial_state.board)):
      for j in range(len(initial_state.board[0])):
        normal_path.append([i,j])

    # print(len(normal_path))

    countdash = 0
    for k in range(9):
      for i in range(len(initial_state.board)):
        for j in range(len(initial_state.board[0])):
          for p in range(i-1, i+2):
            for q in range(j-1, j+2):
              if p<0: p = len(initial_state.board)-1
              if q<0: q = len(initial_state.board[0])-1
              if p>len(initial_state.board)-1: p = 0
              if q>len(initial_state.board[0])-1: q = 0
              if initial_state.board[p][q]=='-':
                countdash+=1
          if countdash==k:
            good_path.append([i,j])
          countdash = 0

    # print(len(good_path))

    return "OK"

# The following is a skeleton for the function called parameterized_minimax,
# which should be a top-level function in each agent file.
# A tester or an autograder may do something like
# import ABC_TTS_agent as player, call get_ready(),
# and then it will be able to call tryout using something like this:
# results = player.parameterized_minimax(**kwargs)

def parameterized_minimax(
       current_state=None,
       use_iterative_deepening_and_time = False,
       max_ply=2,
       use_default_move_ordering = False,
       alpha_beta=False, 
       time_limit=1.0,
       use_custom_static_eval_function=False):

  # All students, add code to replace these default
  # values with correct values from your agent (either here or below).
  # =====================================================================
  global choosed_location
  global USE_CUSTOM_STATIC_EVAL_FUNCTION
  global current_state_static_val
  global n_states_expanded
  global n_static_evals_performed
  global max_depth_reached
  global n_ab_cutoffs
  global t0
  global good_path
  global normal_path
  global use_path
  t0 = time.time()

  if use_default_move_ordering: 
    use_path = normal_path
  else: 
    use_path = good_path
  # =====================================================================

  USE_CUSTOM_STATIC_EVAL_FUNCTION = use_custom_static_eval_function
  current_state_static_val = -1000.0
  n_states_expanded = 0
  n_static_evals_performed = 0
  max_depth_reached = 0
  n_ab_cutoffs = 0

  # STUDENTS: You may create the rest of the body of this function here.
  if use_iterative_deepening_and_time:

    test_depth = 1
    while(test_depth<=max_ply):
      # print("iter to max_depth = ", test_depth)
      temp_result, temp_step = recursive(current_state, test_depth, 0, whichSide, whichSide, -1000000000, 1000000000, alpha_beta, time_limit)
      if temp_result==None: break
      else:
        current_state_static_val = temp_result
        choosed_location = temp_step
      test_depth += 1
  else:
    current_state_static_val, choosed_location = recursive(current_state, max_ply, 0, whichSide, whichSide, -1000000000, 1000000000, alpha_beta, time_limit)



  # Prepare to return the results, don't change the order of the results
  results = []
  results.append(current_state_static_val)
  results.append(n_states_expanded)
  results.append(n_static_evals_performed)
  results.append(max_depth_reached)
  results.append(n_ab_cutoffs)
  # Actually return the list of all results...
  print(results)
  return(results)


def recursive(current_state, max_depth, depth, W_or_B, me_W_or_B, Max, Min, alpha_beta, time_limit):

  # ===========================================
  # global choosed_location
  global n_states_expanded
  global n_static_evals_performed
  global max_depth_reached
  global n_ab_cutoffs
  global t0
  global use_path
  global K
  # ===========================================
  
  if (time.time()-t0) > (time_limit - 0.02): return None, None

  n_states_expanded += 1

  # print("into recursive. depth = ", depth)
  if depth == max_depth:
    max_depth_reached = depth
    n_static_evals_performed += 1
    return current_state.static_eval(), (0,0)

  score = 0
  MinMax_step = (1,1)

  temp_state = MY_TTS_State(current_state.board)

  for [i,j] in use_path:
    if temp_state.board[i][j]==' ':
      # print(i,j)
      if me_W_or_B == 'W':

        if W_or_B == 'W':
          temp_state.board[i][j] = 'W'
          if not temp_state.over_or_not('W'):
            score, _ = recursive(temp_state, max_depth, depth+1, 'B', me_W_or_B, Max, Min, alpha_beta, time_limit)
            if score==None: return None, None
          else:
            return 10**K, (i,j)

          if score > Max:
            Max = score
            MinMax_step = (i,j)
            if alpha_beta and Max>=Min:
              n_ab_cutoffs += 1
              return Max, MinMax_step

        elif W_or_B == 'B':
          temp_state.board[i][j] = 'B'
          if not temp_state.over_or_not('B'):
            score, _ = recursive(temp_state, max_depth, depth+1, 'W', me_W_or_B, Max, Min, alpha_beta, time_limit)
            if score==None: return None, None
          else:
            return -10**K, (i,j)

          if score < Min:
            Min = score
            MinMax_step = (i,j)
            if alpha_beta and Max>=Min:
              n_ab_cutoffs += 1
              return Min, MinMax_step

      elif me_W_or_B == 'B':

        if W_or_B == 'W':
          temp_state.board[i][j] = 'W'
          if not temp_state.over_or_not('W'):
            score, _ = recursive(temp_state, max_depth, depth+1, 'B', me_W_or_B, Max, Min, alpha_beta, time_limit)
            if score==None: return None, None
          else:
            return -10**K, (i,j)

          if score < Min:
            Min = score
            MinMax_step = (i,j)
            if alpha_beta and Max>=Min:
              n_ab_cutoffs += 1
              return Min, MinMax_step

        elif W_or_B == 'B':
          temp_state.board[i][j] = 'B'
          if not temp_state.over_or_not('B'):
            score, _ = recursive(temp_state, max_depth, depth+1, 'W', me_W_or_B, Max, Min, alpha_beta, time_limit)
            if score==None: return None, None
          else:
            return 10**K, (i,j)

          if score > Max:
            Max = score
            MinMax_step = (i,j)
            if alpha_beta and Max>=Min:
              n_ab_cutoffs += 1
              return Max, MinMax_step

      temp_state.board[i][j] = ' '

  # choosed_location = MinMax_step
  if me_W_or_B == 'W':
    if W_or_B == 'W':
      return Max, MinMax_step
    elif W_or_B == 'B':
      return Min, MinMax_step
  elif me_W_or_B == 'B':
    if W_or_B == 'W':
      return Min, MinMax_step
    elif W_or_B == 'B':
      return Max, MinMax_step


utterance_winning_list = ["Is there a better step?",
                          "You don't know a fool can be so good huh?",
                          "HaHa I am about to win I guess. Am I?",
                          "I am on the white side right?",
                          "So...I am on the black side?",
                          "Let's see who is fool now?",
                          "I think GO is more easier than this game...",
                          "I can beat AlphaGo with this step.",
                          "Is AlphaGo a man or a woman?",
                          "I don't know what I am doing right now. I am just hungry.",
                          "Why we can only use white and black? I want purple!",
                          "I just want to eat and sleep..."
                          ]
utterance_losing_list = []
index = -1


def find_utterance():
  global utterance_winning_list
  global index
  index+=1
  return utterance_winning_list[index%12]