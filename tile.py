# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:40:33 2021

@author: gomes
"""

def permutations_gen(L):
    if len(L) == 1:
        yield [L[0]]
        return
    for subPermutation in permutations_gen(L[:-1]):
        for i in range(len(L)):
            yield subPermutation[:i] +[L[-1]] +subPermutation[i:]

class Board:
    def __init__(self):
        self.states = []
        for s in permutations_gen(list(reversed(range(9)))):
            self.states.append(tuple(s))
        self.init_values()
        
    def init_values(self):
        self.value = {}
        for state in self.states:
            self.value[state] = 0
    
    def neighbors(self, state):
        neighbors = []
        i = state.index(0)
        #Top neighbor
        if i >= 3:
            s = list(state)
            s[i-3], s[i] = s[i], s[i-3]
            neighbors.append(tuple(s))
        #Bottom neighbor
        if i<=5:
            s = list(state)
            s[i+3], s[i] = s[i], s[i+3]
            neighbors.append(tuple(s))
        #Left neighboor
        if i%3 != 0:
            s = list(state)
            s[i-1], s[i] = s[i], s[i-1]
            neighbors.append(tuple(s))
        #Right neighboor
        if i%3 != 2:
            s = list(state)
            s[i+1], s[i] = s[i], s[i+1]
            neighbors.append(tuple(s))
        return neighbors
        
    
    def argmax(self, list_states):
        v_max,a_max = None, None
        for state in list_states:
            if a_max is None or v_max<self.value[state]:
                a_max = state
                v_max = self.value[state]
        return a_max
    
    def value_iterator(self, iterations=1):
        for i in range(iterations):
            for state in self.states[1:]:
                #self.states[0] = s_T
                arrows=[-1+self.value[new_state] for new_state in self.neighbors(state)]
                self.value[state]=max(arrows)
    
    def policy(self, state):
        return self.argmax(self.neighbors(state))
    
    def find_T(self, state, printing=False):
        path = [state]
        if printing:
            print(state)
        while(state != self.states[0]):
            state = self.policy(state)
            path.append(state)
            if printing:
                print(state)
        return path
    
    def save_value(self, saving_file):
        file = open(saving_file, 'w')
        for state, value in self.value.items():
            file.write(f"{state}:{value}\n")
        file.close()
    
    def init_saved_values(self, saved_values):
        self.value = {}
        file = open(saved_values)
        for line in file:
            state_str, value_str = line.split(':')
            value = int(value_str)
            state_list = []
            for char in state_str:
                try:
                    state_list.append(int(char))
                except ValueError:
                    continue
            state = tuple(state_list)
            self.value[state] = value
        file.close()