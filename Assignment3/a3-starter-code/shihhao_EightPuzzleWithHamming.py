'''
shihhao_EightPuzzleWithHamming.py
This file augments EightPuzzle.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is the hamming distance, or

'''

from EightPuzzle import *


def h(s):
  count = 0
  for i in range(3):
    for j in range(3):
      if i==0 and j==0:
        continue
      else:
        if s.b[i][j]!=(3*i+j):
          count+=1
  return count

# A simple test:
#print(h('Nantes'))
