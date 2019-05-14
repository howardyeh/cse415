''' IDDFS.py
by Shih-Hao Yeh

Assignment 2, in CSE 415, Winter 2019.

This file contains my implementation of Iterative Deepening DF search algorithm
for problem solving.
'''

import sys

if sys.argv==[''] or len(sys.argv)<2:
 # import EightPuzzle as Problem
  import TowersOfHanoi.TowersOfHanoi as Problem
  # import FarmerFox.shihhao_Farmer_Fox as Problem
  # import Missionaries.Missionaries as Problem
else:
  import importlib
  Problem = importlib.import_module(sys.argv[1])

print("\nWelcome to IDDFS")
COUNT = None
BACKLINKS = {}

def runDFS():
  initial_state = Problem.CREATE_INITIAL_STATE()
  print("Initial State:")
  print(initial_state)
  global COUNT, BACKLINKS, MAX_OPEN_LENGTH
  COUNT = 0
  BACKLINKS = {}
  MAX_OPEN_LENGTH = 0
  IterativeDFS(initial_state)
  print(str(COUNT)+" states expanded.")
  print('MAX_OPEN_LENGTH = '+str(MAX_OPEN_LENGTH))

def IterativeDFS(initial_state):
  global COUNT, BACKLINKS, MAX_OPEN_LENGTH
  depth = 1
  temp_depth = 0

  while 1:
    depth = depth + 1
    print('Start with depth ',depth, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  # STEP 1. Put the start state on a list OPEN
    OPEN = [initial_state]
    CLOSED = []
    #################################################
    # add this inside the loop for different depth
    BACKLINKS = {}
    #################################################
    BACKLINKS[initial_state] = None

  # STEP 2. If OPEN is empty, output “DONE” and stop.
    while OPEN != []:
      report(OPEN, CLOSED, COUNT)
      if len(OPEN)>MAX_OPEN_LENGTH: MAX_OPEN_LENGTH = len(OPEN)

  # STEP 3. Select the first state on OPEN and call it S.
  #         Delete S from OPEN.
  #         Put S on CLOSED.
  #         If S is a goal state, output its description
      S = OPEN.pop(0)
      CLOSED.append(S)

      if Problem.GOAL_TEST(S):
        print(Problem.GOAL_MESSAGE_FUNCTION(S))
        path = backtrace(S)
        print('Length of solution path found: '+str(len(path)-1)+' edges')
        return
      COUNT += 1

####################################################################
# modify from ItrDFS.py

  # STEP 4. Generate the list L of successors of S and delete 
  #         from L those states already appearing on CLOSED.
      temp_depth = len(backtrace(S))
      print('temp_depth = ',temp_depth)
      if temp_depth < depth-1:
        L = []
        for op in Problem.OPERATORS:
          if op.precond(S):
            new_state = op.state_transf(S)
            if not (new_state in CLOSED):
              L.append(new_state)
              BACKLINKS[new_state] = S

      elif temp_depth == depth-1:
        L = []
        for op in Problem.OPERATORS:
          if op.precond(S):
            new_state = op.state_transf(S)
            if not (new_state in CLOSED) and (Problem.GOAL_TEST(new_state)):
              L.append(new_state)
              BACKLINKS[new_state] = S

      else:
        print('this state reach limit depth!')
        continue
####################################################################

  # STEP 5. Delete from OPEN any members of OPEN that occur on L.
  #         Insert all members of L at the front of OPEN.
      for s2 in L:
        for i in range(len(OPEN)):
          if (s2 == OPEN[i]):
            del OPEN[i]; break

      OPEN = L + OPEN
      print_state_list("OPEN", OPEN)
  # STEP 6. Go to Step 2.

def print_state_list(name, lst):
  ###############################################
  # modify from ItrDFS.py
  print(name+" is now: ",end='')
  if len(lst)!=0:
    for s in lst[:-1]:
      print(str(s),end=', ')
    print(str(lst[-1]))
  else:
    print('empty')
  ###############################################

def backtrace(S):
  global BACKLINKS
  path = []
  while S:
    path.append(S)
    S = BACKLINKS[S]
  path.reverse()
  print("Solution path: ")
  for s in path:
    print(s)
  return path    
  
def report(open, closed, count):
  print("len(OPEN)="+str(len(open)), end='; ')
  print("len(CLOSED)="+str(len(closed)), end='; ')
  print("COUNT = "+str(count))

if __name__=='__main__':
  runDFS()

