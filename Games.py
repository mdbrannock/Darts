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

# Import Utils.py
import Utils as ut

# Import MyPlots.py
import MyPlots as myplt

# Initialize players dictionary
#players = {}

# Initialize all the players
#ut.add_player(players, 'aric')
#ut.add_player(players, 'daniel')
#ut.add_player(players, 'jenn')
#ut.add_player(players, 'keith')
#ut.add_player(players, 'tom')
#ut.add_player(players, 'alex')
#ut.add_player(players, 'kim')
#ut.add_player(players, 'john')
#ut.add_player(players, 'brandon')

# Import players
players = pickle.load(open('data/players.obj', 'rb'))

# Get handicaps for next game
print(ut.handicaps(players, 'kim', 'jenn', 'keith', 'tom', 'daniel', 'aric'))

# Choose numbers
print(ut.choosedarts())

# Record of games that have passed and already been included in players.obj
#ut.game(players, 'tom', 'daniel', 'aric')
#ut.game(players, 'aric', 'daniel', 'tom')
#ut.game(players, 'daniel', 'aric', 'tom')
#ut.game(players, 'daniel', 'tom')
#ut.game(players, 'daniel', 'tom', 'keith', 'aric', 'jenn')
#ut.game(players, 'daniel', 'tom', 'aric')
#ut.game(players, 'tom', 'daniel', 'aric')
#ut.game(players, 'daniel', 'tom', 'aric')
#ut.game(players, 'daniel', 'tom', 'keith')
#ut.game(players, 'tom', 'daniel', 'jenn', 'keith')
#ut.game(players, 'daniel', 'aric', 'keith')
#ut.game(players, 'daniel', 'keith')
#ut.game(players, 'tom', 'daniel')
#ut.game(players, 'daniel', 'keith', 'tom', 'aric', 'jenn')
#ut.game(players, 'tom', 'keith')
#ut.game(players, 'daniel', 'tom', 'aric', 'keith')
#ut.game(players, 'daniel', 'tom', 'keith', 'jenn')
#ut.game(players, 'daniel', 'keith')
#ut.game(players, 'daniel', 'tom', 'keith', 'jenn')
#ut.game(players, 'tom', 'daniel', 'keith')
#ut.game(players, 'aric', 'daniel', 'keith')
#ut.game(players, 'daniel', 'tom', 'aric')
#ut.game(players, 'daniel', 'aric', 'tom')
#ut.game(players, 'daniel', 'tom', 'aric')
#ut.game(players, 'tom', 'aric', 'daniel')
#ut.game(players, 'daniel', 'tom', 'keith')
#ut.game(players, 'daniel', 'tom', 'keith')
#ut.game(players, 'aric', 'tom', 'daniel', 'keith', 'jenn')
#ut.game(players, 'daniel', 'tom', 'keith')
#ut.game(players, 'aric', 'daniel', 'keith', 'tom')
#ut.game(players, 'daniel', 'tom', 'jenn', 'keith')
#ut.game(players, 'daniel', 'aric', 'tom', 'jenn', 'keith')
#ut.game(players, 'daniel', 'tom', 'aric', 'keith', 'jenn', 'alex')
#ut.game(players, 'tom', 'daniel', 'aric', 'keith')
#ut.game(players, 'daniel', 'tom')
#ut.game(players, 'daniel', 'tom', 'keith', 'jenn')

# New record of games, these include handicaps
#ut.game(players, 'daniel', 'keith', 'aric', 'jenn')
#ut.game(players, 'daniel', 'tom', 'keith', 'jenn', 'kim')
#ut.game(players, 'tom', 'daniel', 'aric', 'keith', 'jenn', 'kim')
#ut.game(players, 'tom', 'daniel', 'aric', 'kim', 'keith', 'jenn')
#ut.game(players, 'aric', 'daniel', 'kim', 'jenn')
#ut.game(players, 'daniel', 'keith')
#ut.game(players, 'aric', 'daniel', 'tom')
#ut.game(players, 'daniel', 'tom', 'keith', 'aric')
#ut.game(players, 'daniel', 'tom', 'aric', 'keith')
#ut.game(players, 'aric', 'tom', 'daniel', 'keith', 'kim')
#ut.game(players, 'daniel', 'keith', 'aric', 'tom', 'jenn')
#ut.game(players, 'tom', 'keith', 'kim')
#ut.game(players, 'jenn', 'tom', 'keith', 'kim')
#ut.game(players, 'daniel', 'kim', 'tom')
#ut.game(players, 'tom', 'daniel', 'kim', 'jenn', 'keith')
#ut.game(players, 'tom', 'kim', 'daniel', 'aric', 'keith', 'jenn')
#ut.game(players, 'tom', 'jenn', 'aric', 'kim', 'daniel', 'keith')
#ut.game(players, 'daniel', 'keith', 'jenn', 'kim')
#ut.game(players, 'keith', 'daniel', 'tom', 'jenn', 'kim')
#ut.game(players, 'daniel', 'keith', 'aric', 'tom', 'jenn', 'kim')
#ut.game(players, 'daniel', 'tom', 'kim', 'keith', 'aric')
#ut.game(players, 'aric', 'tom', 'daniel')
#ut.game(players, 'daniel', 'keith', 'kim', 'jenn', 'tom', 'john')
## Brandon/Alex removed from following game; too many players. Alex, Jenn, Brandon.
#ut.game(players, 'daniel', 'keith', 'aric', 'kim', 'tom', 'jenn')
#ut.game(players, 'daniel', 'tom', 'jenn', 'keith')
#ut.game(players, 'tom', 'daniel', 'aric', 'jenn', 'keith')
#ut.game(players, 'aric', 'tom', 'keith', 'kim', 'daniel', 'jenn')
#ut.game(players, 'daniel', 'tom', 'kim', 'jenn')
#ut.game(players, 'tom', 'daniel', 'aric', 'kim', 'keith', 'jenn')
#ut.game(players, 'jenn', 'daniel', 'tom', 'aric', 'keith')
#ut.game(players, 'daniel', 'kim', 'tom', 'aric', 'jenn')
#ut.game(players, 'aric', 'daniel', 'tom', 'jenn', 'keith', 'kim')
#ut.game(players, 'aric', 'tom', 'kim')
#ut.game(players, 'daniel', 'keith', 'tom', 'kim')
#ut.game(players, 'kim', 'tom', 'aric', 'daniel', 'jenn')
#ut.game(players, 'aric', 'daniel', 'tom', 'keith', 'kim', 'jenn')
#ut.game(players, 'tom', 'daniel', 'keith')
#ut.game(players, 'daniel', 'tom', 'jenn', 'keith', 'kim')
#ut.game(players, 'daniel', 'keith', 'tom', 'kim', 'jenn')
#ut.game(players, 'kim', 'keith', 'tom', 'jenn', 'daniel')
#ut.game(players, 'daniel', 'kim', 'keith')
#ut.game(players, 'tom', 'daniel', 'kim', 'aric', 'keith')
#ut.game(players, 'daniel', 'tom', 'kim')

# Plot current state of player distributions
myplt.current_status(players, min_games = 5)

# Plot an individual's progress over time
myplt.history(players)
myplt.history(players, 'tom', 'daniel', 'aric')
myplt.history(players, 'kim', 'keith')

# Save the final dictionary object with all the players' densities
pickle.dump(players, open('data/players.obj', 'wb'))
