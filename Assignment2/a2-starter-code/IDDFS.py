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

print("\nWelcome to ItrDFS")
COUNT = None
BACKLINKS = {}
end_state = Problem.CREATE_INITIAL_STATE()

def runDFS():
  initial_state = Problem.CREATE_INITIAL_STATE()
  print("Initial State:")
  print(initial_state)
  global COUNT, BACKLINKS, MAX_OPEN_LENGTH, end_state
  COUNT = 0
  BACKLINKS = {}
  MAX_OPEN_LENGTH = 0
  found = False
  for depth in range (1,50):
    print('depth = ', depth)
    found = IterativeDFS(initial_state, depth)
    if found:
      break
  path = backtrace(end_state)
  print('Length of solution path found: '+str(len(path)-1)+' edges')
  print(str(COUNT)+" states expanded.")
  print('MAX_OPEN_LENGTH = '+str(MAX_OPEN_LENGTH))

def IterativeDFS(initial_state, depth):
  global COUNT, BACKLINKS, MAX_OPEN_LENGTH, end_state

# STEP 1. Put the start state on a list OPEN
  OPEN = [initial_state]
  CLOSED = []
  BACKLINKS[initial_state] = None
  found = None

# STEP 2. If OPEN is empty, output “DONE” and stop.
  while OPEN != []:
    # report(OPEN, CLOSED, COUNT)
    if len(OPEN)>MAX_OPEN_LENGTH: MAX_OPEN_LENGTH = len(OPEN)

# STEP 3. Select the first state on OPEN and call it S.
#         Delete S from OPEN.
#         Put S on CLOSED.
#         If S is a goal state, output its description
    S = OPEN.pop(0)
    CLOSED.append(S)

    if depth==0 and Problem.GOAL_TEST(S):
      print(Problem.GOAL_MESSAGE_FUNCTION(S))
      end_state = S
      return True

    elif depth > 0:
      COUNT += 1

      # STEP 4. Generate the list L of successors of S and delete 
      #         from L those states already appearing on CLOSED.

      for op in Problem.OPERATORS:
        if op.precond(S):
          new_state = op.state_transf(S)
          if not (new_state in CLOSED):
            found = IterativeDFS(new_state, depth-1)
            if found:
              BACKLINKS[new_state] = S
              return True
      return False

    else:
      return False

def print_state_list(name, lst):
  print(name+" is now: ",end='')
  for s in lst[:-1]:
    print(str(s),end=', ')
  print(str(lst[-1]))

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

