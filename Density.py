# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:17:31 2017

@author: mdbrannock
"""

# Second Attempt. Using density approximations to build iterative posterior
# distributions.
import numpy as np
from sklearn.neighbors.kde import KernelDensity
from sklearn.model_selection import cross_val_score

# Define dictionary with starting prior distribution for every player.
# The original prior will just be a normal distribution [u, s]. However, to
# keep the formatting consistent, it would be nice to have the type of object
# be the same for the first prior as all the other priors. As a result, we'll
# build a density approximation of a normal distribution and use that.

# Build density approximation using scikit learn:
# http://scikit-learn.org/stable/modules/cross_validation.html

# Use CV to get best bandwidth. Use kde.score() as the evualation metric.
X = np.array(np.random.normal(15, 3, 1000)).reshape(-1, 1)
upper = 1.06*X.std()
lower = 1.06*X.std()/20
rng = np.arange(lower, upper, (upper-lower)/20)
bws = {}

for bw in rng:
    kde = KernelDensity(bandwidth=bw)
    s = cross_val_score(kde, X, cv=5).mean()
    bws[bw] = s
    
fbw = max(bws.keys(), key = lambda x: bws[x])
kde = KernelDensity(bandwidth = fbw).fit(X)

# Define empty players dictionary
players = {}

# Define game function. Give it the players in the order they finished the game
def game(players, *ps):
    ranks = {}
    
    for p in ps:
        # Record what place they got (0 is first place bc python is stupid)
        r = [x for x in range(len(ps)) if ps[x] == p]
        ranks[p] = r[0]
        if p not in players:
            print('Add "' + p + '" to players object with add_player()')
            return
    
    # Simulate n games
    games = []
    for n in range(10000):
        lambs = {}
        turns = {}
        
        # Cycle through each person to get their game performance
        for p in ps:

            # Simulate a true AVERAGE of turns for each person from their prior 
            # distribution.
            lambs[p] = abs(players[p].sample(1))
            
            # From this average generate how many turns it would take them to
            # finish a game from a Poisson distribution. Generating multiple
            # numbers per game to serve as a tie breaker.
            turns[p] = list(np.random.poisson(lambs[p], 10))
            
        # Record the final position of each player in the simulated game
        result = sorted(turns.keys(), key = lambda x: turns[x])
        s_rank = {}
        for i in range(len(result)):
            s_rank[result[i]] = i
        games.append([s_rank, lambs])
        
    # Pull out the lambdas that match the games that occured
    matching_results = [x[1] for x in games if x[0] == ranks]
    
    # Build new density approximation for each player
    for p in ps:
        # Pull out their matching turns to build matching distribution
        md = np.array([x[p][0][0] for x in matching_results]).reshape(-1, 1)
    
        # Determine the best bandwidth using the same method as in the
        # beginning of the script.
        upper = 1.06*md.std()
        lower = 1.06*md.std()/20
        rng = np.arange(lower, upper, (upper-lower)/20)
        bws = {}
        
        for bw in rng:
            kde = KernelDensity(bandwidth=bw)
            s = cross_val_score(kde, md, cv=5).mean()
            bws[bw] = s
            
        fbw = max(bws.keys(), key = lambda x: bws[x])
        players[p] = KernelDensity(bandwidth = fbw).fit(md)
    
    return players
        
# Define function that adds a new player
def add_player(players, p):
    players[p] = kde
