#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:35:53 2017

@author: danielbrannock
"""

import numpy as np
import statistics as st
import matplotlib.pyplot as mp

# Define prior distribution for all players
def prior(lam):
    return list(np.random.poisson(lam=lam, size=5))

# Define a game function. Inputs the players and outputs who wins
# Returns the position of each player in the order given
def game(p1, p2, p3, p1_lam, p2_lam, p3_lam):
    
    g = {p1: prior(p1_lam), p2: prior(p2_lam), p3: prior(p3_lam)}
    
    rank = sorted(g.keys(), key = lambda x: g[x])
    outcome = {rank[0]: 1, rank[1]: 2, rank[2]: 3}

    return outcome
        
# Run n iterations of the four games we played
dan = []
tom = []
ari = []

for n in range(100000):
    res = []
    
    # Assign lambdas from prior distribution (normal(15, 3))
    lams = {'dan': round(np.random.normal(15, 3)),
            'tom': round(np.random.normal(15, 3)),
            'ari': round(np.random.normal(15, 3))}
    
    for m in range(3):
        res.append(game('dan', 'tom', 'ari', 
                        lams['dan'], lams['tom'], lams['ari']))
        
    # Record requirements
    if (sorted([res[0]['dan'],
                res[1]['dan'],
                res[2]['dan']]) == [1, 2, 2] and
        sorted([res[0]['tom'],
                res[1]['tom'],
                res[2]['tom']]) == [1, 3, 3] and
        sorted([res[0]['ari'],
                res[1]['ari'],
                res[2]['ari']]) == [1, 2, 3]):
           dan.append(lams['dan'])
           tom.append(lams['tom'])
           ari.append(lams['ari'])
       
# Show mean for each person
print('Daniel Mean:', round(st.mean(dan), 1))
print('Tom Mean:', round(st.mean(tom), 1))
print('Aric Mean:', round(st.mean(ari), 1))
           
# Plot resulting histograms!
n1, bins1, patches1 = mp.hist(dan, max(dan)-min(dan)+1, alpha=0.75)
n2, bins2, patches2 = mp.hist(tom, max(tom)-min(tom)+1, alpha=0.75)
n3, bins3, patches3 = mp.hist(ari, max(ari)-min(ari)+1, alpha=0.75)

mp.show()
