#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 18:27:52 2017

@author: mdbrannock
"""
import pickle as pickle
import os

# Change working directory
os.chdir('/Users/danielbrannock/Documents/Projects/Darts')

# Import Density.py
import Density as ds

# Import MyPlots.py
import MyPlots as myplt

# Initialize players dictionary
#players = {}

# Initialize all the players
#ds.add_player(players, 'aric')
#ds.add_player(players, 'daniel')
#ds.add_player(players, 'jenn')
#ds.add_player(players, 'keith')
#ds.add_player(players, 'tom')

# Import players
players = pickle.load(open('data/players.obj', 'rb'))

# Record of games that have passed and already been included in players.obj
#ds.game(players, 'tom', 'daniel', 'aric')
#ds.game(players, 'aric', 'daniel', 'tom')
#ds.game(players, 'daniel', 'aric', 'tom')
#ds.game(players, 'daniel', 'tom')
#ds.game(players, 'daniel', 'tom', 'keith', 'aric', 'jenn', n=50000)
#ds.game(players, 'daniel', 'tom', 'aric')
#ds.game(players, 'tom', 'daniel', 'aric')
#ds.game(players, 'daniel', 'tom', 'aric')
#ds.game(players, 'daniel', 'tom', 'keith')
#ds.game(players, 'tom', 'daniel', 'jenn', 'keith')
#ds.game(players, 'daniel', 'aric', 'keith')
#ds.game(players, 'daniel', 'keith')
#ds.game(players, 'tom', 'daniel')
#ds.game(players, 'daniel', 'keith', 'tom', 'aric', 'jenn', n=50000)
#ds.game(players, 'tom', 'keith')
#ds.game(players, 'daniel', 'tom', 'aric', 'keith')
#ds.game(players, 'daniel', 'tom', 'keith', 'jenn')
#ds.game(players, 'daniel', 'keith')
#ds.game(players, 'daniel', 'tom', 'keith', 'jenn')
#ds.game(players, 'tom', 'daniel', 'keith')
#ds.game(players, 'aric', 'daniel', 'keith')

# Save the final dictionary object with all the players' densities
pickle.dump(players, open('data/players.obj', 'wb'))

# Plot current state of player distributions
myplt.current_status(players)

# Plot an individual's progress over time
myplt.history(players, 'tom')
