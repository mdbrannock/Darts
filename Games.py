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
import Utils as ut

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
#ds.add_player(players, 'alex')
#ds.add_player(players, 'kim')

# Import players
players = pickle.load(open('data/players.obj', 'rb'))

# Get handicaps for next game
ds.handicaps(players, 'daniel', 'kim', 'jenn', 'aric', 'keith', 'tom')

# Choose numbers
ut.choosedarts()

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
#ds.game(players, 'daniel', 'tom', 'aric')
#ds.game(players, 'daniel', 'aric', 'tom')
#ds.game(players, 'daniel', 'tom', 'aric')
#ds.game(players, 'tom', 'aric', 'daniel')
#ds.game(players, 'daniel', 'tom', 'keith')
#ds.game(players, 'daniel', 'tom', 'keith')
#ds.game(players, 'aric', 'tom', 'daniel', 'keith', 'jenn', n=50000)
#ds.game(players, 'daniel', 'tom', 'keith')
#ds.game(players, 'aric', 'daniel', 'keith', 'tom', n=50000)
#ds.game(players, 'daniel', 'tom', 'jenn', 'keith')
#ds.game(players, 'daniel', 'aric', 'tom', 'jenn', 'keith', n=50000)
#ds.game(players, 'daniel', 'tom', 'aric', 'keith', 'jenn', 'alex', n=100000)
#ds.game(players, 'tom', 'daniel', 'aric', 'keith')
#ds.game(players, 'daniel', 'tom')
#ds.game(players, 'daniel', 'tom', 'keith', 'jenn')

# New record of games, these include handicaps
#ds.game(players, 'daniel', 'keith', 'aric', 'jenn', n=50000)
#ds.game(players, 'daniel', 'tom', 'keith', 'jenn', 'kim', n=50000)
#ds.game(players, 'tom', 'daniel', 'aric', 'keith', 'jenn', 'kim', n=100000)
#ut.game(players, 'tom', 'daniel', 'aric', 'kim', 'keith', 'jenn')
#ut.game(players, 'aric', 'daniel', 'kim', 'jenn')
#ut.game(players, 'daniel', 'keith')
#ut.game(players, 'aric', 'daniel', 'tom')
#ut.game(players, 'daniel', 'tom', 'keith', 'aric')
#ut.game(players, 'daniel', 'tom', 'aric', 'keith')
#ut.game(players, 'aric', 'tom', 'daniel', 'keith', 'kim')
#ut.game(players, 'daniel', 'keith', 'aric', 'tom', 'jenn')

# Plot current state of player distributions
myplt.current_status(players)

# Plot an individual's progress over time
myplt.history(players)
myplt.history(players, 'daniel')

# Save the final dictionary object with all the players' densities
pickle.dump(players, open('data/players.obj', 'wb'))
