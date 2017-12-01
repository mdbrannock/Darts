#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 18:27:52 2017

@author: mdbrannock
"""
import pickle as pickle
import matplotlib.pyplot as plt
import os

# Change working directory
os.chdir('/Users/danielbrannock/Documents/Projects/Darts')

# Import Density.py
import Density as ds

# Initialize players dictionary
players = {}

# Initialize all the players
ds.add_player(players, 'aric')
ds.add_player(players, 'daniel')
ds.add_player(players, 'jenn')
ds.add_player(players, 'keith')
ds.add_player(players, 'tom')

# Import players
players = pickle.load(open('data/players.obj', 'rb'))

# Record of games that have passed and already been included in players.obj
#players = ds.game(players, 'tom', 'daniel', 'aric')
#players = ds.game(players, 'aric', 'daniel', 'tom')
#players = ds.game(players, 'daniel', 'aric', 'tom')
#players = ds.game(players, 'daniel', 'tom')
#players = ds.game(players, 'daniel', 'tom', 'keith', 'aric', 'jenn')
#players = ds.game(players, 'daniel', 'tom', 'aric')
#players = ds.game(players, 'tom', 'daniel', 'aric')
#players = ds.game(players, 'daniel', 'tom', 'aric')
#players = ds.game(players, 'daniel', 'tom', 'keith')
#players = ds.game(players, 'tom', 'daniel', 'jenn', 'keith')
#players = ds.game(players, 'daniel', 'aric', 'keith')
#players = ds.game(players, 'daniel', 'keith')
#players = ds.game(players, 'tom', 'daniel')
players = ds.game(players, 'daniel', 'keith', 'tom', 'aric', 'jenn')

# Plot current state of player distributions
for p in players.keys():
    print(p)
    dist = players[p].sample(5000).reshape(1, -1)[0]
    print(dist.mean())
    n, bins, patches = plt.hist(dist, 30, normed=1, alpha = 0.7, label = p)
    l = plt.plot(bins)
    plt.axis([3, 30, 0, 0.3])
    
plt.legend()

# Save the final dictionary object with all the players' densities
pickle.dump(players, open('data/players.obj', 'wb'))
