#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 18:08:17 2017

@author: danielbrannock
"""
import matplotlib.pyplot as plt
import numpy as np

# Define a bunch of plots I might want!

# First the histogram of everyone's current distribution
def current_status(players):
    for p in players.keys():
        print(p)
        dist = players[p][-1].sample(5000).reshape(1, -1)[0]
        print(dist.mean())
        n, bins, patches = plt.hist(dist, 30, normed=1, alpha = 0.7, label = p)
        
    plt.legend()

# Plot individual player's progress over time
def history(players, *ps):
    if ps == ():
        ps = tuple(players.keys())
    
    if len(ps) == 1:
        p = players[ps[0]]
        u = [np.mean(p[g].sample(1000).reshape(1,-1)[0]) for g in range(len(p))]
        l = [np.percentile(p[g].sample(1000).reshape(1,-1)[0], 25) for g in range(len(p))]
        h = [np.percentile(p[g].sample(1000).reshape(1,-1)[0], 75) for g in range(len(p))]
        t = list(range(1, len(p)+1))
        
        plt.plot(t, u, label = 'Mean')
        plt.plot(t, l, label = 'Low', ls = 'dashed', c = '#1F77B4')
        plt.plot(t, h, label = 'High', ls = 'dashed', c = '#1F77B4')
        plt.ylabel('Average Turns')
        plt.xlabel('# of Games')        
                   
    else:
        for p in ps:
            q = players[p]
            u = [np.mean(q[g].sample(1000).reshape(1,-1)[0]) for g in range(len(q))]
            t = list(range(1, len(q)+1))
            
            plt.plot(t, u, label = p)
            plt.ylabel('Average Turns')
            plt.xlabel('# of Games')
            plt.legend()
        
    plt.show()
