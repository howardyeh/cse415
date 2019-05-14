'''
shihhao_EightPuzzleWithManhattan.py
This file augments EightPuzzle.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is the Manhattan distance, or

'''

from EightPuzzle import *

compare = [[0,1,2],[3,4,5],[6,7,8]]

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def h(s):
  count = 0
  for i in range(3):
    for j in range(3):
      if s.b[i][j]==0:
        continue
      else:
        x,y = index_2d(compare, s.b[i][j])
        count += (abs(x-i)+abs(y-j))
  return count

# A simple test:
#print(h('Nantes'))
