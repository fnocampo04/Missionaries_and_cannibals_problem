# -*- coding: utf-8 -*-
"""Missionaries and cannibals problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GJ7uvRUvikdN8yvrlUz7Ht7CGj7a_pIK

#Missionaries and cannibals problem
"""

# M Missionaries left
# C Cannibals on the right
# B=1 Boat Left
# B=0 Boat Right

import itertools as it

def movs(p): # Generate possible moves for arbitrary p
  mp=[]
  for i in range(p+1):
    mp.append(i)
  m1=[]
  for i in it.product(mp,mp):
    i = list(i)
    if sum(i)<=p and sum(i)!=0:
      m1.append(i)
  for i in m1:
    i.append(1)
  return(m1)


def validate(state):
    [M,C] = [M_original,C_original]
    if(state[0]>M or state[1]>C or state[2]>1 or state[0]<0 or state[1]<0 or state[2]<0 or (0 < state[0] < state[1]) or (0 < (M - state[0]) < (C - state[1]))): # Check the conditions
        return False
    else:
        return True

def generate_next_states(M, C, B):
    moves = movs(P) # Load the possible moves according to p
    valid_states = [] # Initialize the list of valid states empty
    for i in moves: # For each possible move
        if(B==1):next_state = [e1 - e2 for (e1, e2) in zip([M, C, B], i)] # If the boat is to the left, perform the subtraction movement Ex: (3,3,1)->(1,3,0)
        else:next_state = [e1 + e2 for (e1, e2) in zip([M, C, B], i)] # If the boat is to the right, make the move in sum Ex: (3,1,0)->(3,2,1)
        if (validate(next_state)):
            valid_states.append(next_state) # If the next state is valid it is added to the list of valid states
    return valid_states # Return the list of states that were valid

solutions = []

def solve(M, C, B, visited):
    if([M,C,B]==[0,0,0]):# Everyone crossed
        solutions.append(visited + [[0, 0, 0]]) # Solution found added
        return True
    elif([M,C,B] in visited):  #Avoid infinite loop
        return False
    else:
        visited.append([M, C, B])
        if(B==1): # The boat is on the left
            for i in generate_next_states(M, C, B):
                solve(i[0], i[1], i[2], visited[:])
        else: # The boat is on the right
            for i in generate_next_states(M, C, B):
                solve(i[0], i[1], i[2], visited[:])



M,C = 0, 1
while M<C:M,C,P=int(input('Enter the number of missionaries(M>=C): ')),int(input('Enter the number of cannibals(C<M): ')),int(input('Enter the capacity of the boat: '))
[M_original,C_original]=[M,C]
solve(M, C, 1, [])


solutions.sort()
for i in solutions:
    print(i)