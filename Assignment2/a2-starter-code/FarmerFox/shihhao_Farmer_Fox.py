''' shihhao_Farmer_Fox.py
by Shih-Hao Yeh

Assignment 2, in CSE 415, Winter 2019.

This file contains my problem formulation for the problem of the Farmer, Fox, Chicken and Grain
'''
#<METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Farmer Fox Chicken Grain"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Shih-Hao Yeh']
PROBLEM_CREATION_DATE = "20-JAN-2019"
PROBLEM_DESC=\
'''This formulation of the Farmer Fox Chicken Grain problem uses generic
Python 3 constructs and has been tested with Python 3.6.
It is designed to work according to the QUIET2 tools interface.
'''
#</METADATA>

#<COMMON_DATA>

#</COMMON_DATA>

#<COMMON_CODE>
class State:
  def __init__(self, d):
    self.d = d

  def __eq__(self,s2):
    for p in ['Side0','Side1']:
      if self.d[p] != s2.d[p]: return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    txt = "["
    for side in ['Side0','Side1']:
      txt += str(self.d[side]) + " ,"
    return txt[:-2]+"]"

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State({})
    for side in ['Side0', 'Side1']:
      news.d[side]=self.d[side][:]
    return news

  def can_move(self,Animal,From,To):
    '''Tests whether it's legal to move a disk in state s
       from the From peg to the To peg.'''
    try:
      pf=self.d[From] # peg disk goes from
      pt=self.d[To]   # peg disk goes to
      if Animal=='Farmer':
        if 'Farmer' not in pf: return False
        pf.remove(Animal)
      else:
        if 'Farmer' not in pf: return False
        if Animal not in pf: return False
        pf.remove(Animal)
        pf.remove('Farmer')
      # print(pf)
      # if pt == ['Chicken', 'Farmer', 'Fox', 'Grain']: return False
      if set(pf) == set(['Fox', 'Chicken']): 
        if Animal=='Farmer':
          pf.append(Animal)
        else:
          pf.append(Animal)
          pf.append('Farmer')
        pf.sort()
        return False # Fox will eat the chicken
      if set(pf) == set(['Chicken', 'Grain']): 
        if Animal=='Farmer':
          pf.append(Animal)
        else:
          pf.append(Animal)
          pf.append('Farmer')
        pf.sort()
        return False # Chicken will eat the Grain

      if Animal=='Farmer':
        if pt == []:
          pf.append(Animal)
          pf.sort()
          return False
        else:
          pf.append(Animal)
      else:
        pf.append(Animal)
        pf.append('Farmer')
      pf.sort()
      return True # If no situation mentioned above, it is a permitted move.

    except (Exception) as e:
      print(e)


  def move(self,Animal,From,To):
    '''Assuming it's legal to make the move, this computes
       the new state resulting from moving the topmost disk
       from the From peg to the To peg.'''
    news = self.copy() # start with a deep copy.
    pf=self.d[From] # peg disk goes from.
    pt=self.d[To]
    news.d[From]=pf[:]
    news.d[To] = pt[:]
    if Animal=='Farmer':
      news.d[From].remove(Animal)
      news.d[From].sort()
      news.d[To].append(Animal)
      news.d[To].sort()
    else:
      news.d[From].remove(Animal)
      news.d[From].remove('Farmer')
      news.d[From].sort()
      news.d[To].append(Animal)
      news.d[To].append('Farmer')
      news.d[To].sort()
    return news # return new state

  
def goal_test(s):
  '''If the first two pegs are empty, then s is a goal state.'''
  return s.d['Side0']==[]

def goal_message(s):
  return "You are brilliant!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

#</COMMON_CODE>



#<INITIAL_STATE>
INITIAL_DICT = {'Side0': ['Chicken','Farmer','Fox','Grain'], 'Side1':[] }
CREATE_INITIAL_STATE = lambda: State(INITIAL_DICT)
#DUMMY_STATE =  {'peg1':[], 'peg2':[], 'peg3':[] }
#</INITIAL_STATE>



#<OPERATORS>
peg_combinations = [( a, 'Side'+str(b),'Side'+str(c)) for (a,b,c) in
                    [('Fox',0,1),('Chicken',0,1),('Grain',0,1),('Farmer',0,1),('Fox',1,0),('Chicken',1,0),('Grain',1,0),('Farmer',1,0)]]

OPERATORS = [Operator("Move "+p+" from "+q+" to "+r,
                      lambda s,p1=p,q1=q,r1=r: s.can_move(p1,q1,r1),
                      # The default value construct is needed
                      # here to capture the values of p&q separately
                      # in each iteration of the list comp. iteration.
                      lambda s,p1=p,q1=q,r1=r: s.move(p1,q1,r1) )
             for (p,q,r) in peg_combinations]

#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

