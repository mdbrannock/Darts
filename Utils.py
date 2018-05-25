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
import random
import concurrent.futures as futures
import itertools

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

# Define function that represents a single simulation
def single_simulation(ps):
    lambs = {}
    turns = {}

    # Cycle through each person to get their game performance
    for p in ps:

        # Simulate a true AVERAGE of turns for each person from their prior
        # distribution.
        lambs[p] = abs(players[p][-1].sample(1))

        # From this average generate how many turns it would take them to
        # finish a game from a Poisson distribution. Generating multiple
        # numbers per game to serve as a tie breaker.
        turns[p] = list(np.random.poisson(lambs[p], 10))

    # Record the final position of each player in the simulated game
    result = sorted(turns.keys(), key = lambda x: turns[x])
    s_rank = {}
    for i in range(len(result)):
        s_rank[result[i]] = i
    
    return([s_rank, lambs])
    
# Build new density approximation for each player
def dens_approx(p):
    # Pull out their matching turns to build matching distribution
    md = np.array([x[p][0][0] for x in matching_results]).reshape(-1, 1)

    # Determine the best bandwidth using the same method as in the
    # beginning of the script.
    upper = 1.06*md.std()
    lower = 1.06*md.std()/20
    rng = np.arange(lower, upper, (upper-lower)/10)
    bws = {}

    for bw in rng:
        kde = KernelDensity(bandwidth=bw)
        s = cross_val_score(kde, md, cv=5).mean()
        bws[bw] = s

    fbw = max(bws.keys(), key = lambda x: bws[x])
    return({p: KernelDensity(bandwidth = fbw).fit(md)})

# Define game function. Give it the players in the order they finished the game
def game(players, *ps, **kwargs):
    ranks = {}

    for p in ps:
        # Record what place they got (0 is first place bc python is stupid)
        r = [x for x in range(len(ps)) if ps[x] == p]
        ranks[p] = r[0]
        if p not in players:
            print('Add "' + p + '" to players object with add_player()')
            return

    # Simulate n games
    n = 100000
    if 'n' in kwargs:
        n = int(kwargs['n'])

    # Define function that represents a single simulation
    def single_simulation(ps):
        lambs = {}
        turns = {}
    
        # Cycle through each person to get their game performance
        for p in ps:
    
            # Simulate a true AVERAGE of turns for each person from their prior
            # distribution.
            lambs[p] = abs(players[p][-1].sample(1))
    
            # From this average generate how many turns it would take them to
            # finish a game from a Poisson distribution. Generating multiple
            # numbers per game to serve as a tie breaker.
            turns[p] = list(np.random.poisson(lambs[p], 10))
    
        # Record the final position of each player in the simulated game
        result = sorted(turns.keys(), key = lambda x: turns[x])
        s_rank = {}
        for i in range(len(result)):
            s_rank[result[i]] = i
    
        return([s_rank, lambs])
        
    # Do this by repeating ps n times in a list
    ps_list = itertools.repeat(ps, n)
    games = list(map(single_simulation, ps_list))

    # Pull out the lambdas that match the games that occured
    matching_results = [x[1] for x in games if x[0] == ranks]
    matching_n = len(matching_results)
    print(matching_n, 'matching games, or', 
          round(matching_n/n, 3)*100, 'percent')
    
    # if matching_results is less than 1000, then run the expected number of
    # iterations to get up to 1500 matching game results.
    if matching_n < 1000:
        addl_games = round(((n/matching_n) * (1500 - matching_n)))
        
        print('Too few matching results, running', addl_games, 
              'more simulations')
        
        # Run additional simulations
        ps_list = itertools.repeat(ps, addl_games)
        tmp = map(single_simulation, ps_list)
        games += tmp
            
        matching_results = [x[1] for x in games if x[0] == ranks]
        print('Now', len(matching_results), 'matching games')
        
    # Trying to build a density off of more than 1000 points is computationally
    # expensive and pretty pointless. Sample out 1000 matching games to use for
    # density approximations.
    matching_results = random.sample(matching_results, 1000)
        
    # Calculate density approximation for everyone
    # This could be done in parallel to speed things up a little, but with the
    # 1000 game limit in matching_results, this shouldn't be too slow.
    for p in ps:
        # Pull out their matching turns to build matching distribution
        md = np.array([x[p][0][0] for x in matching_results]).reshape(-1, 1)

        # Determine the best bandwidth using the same method as in the
        # beginning of the script.
        upper = 1.06*md.std()
        lower = 1.06*md.std()/20
        rng = np.arange(lower, upper, (upper-lower)/10)
        bws = {}

        for bw in rng:
            kde = KernelDensity(bandwidth=bw)
            s = cross_val_score(kde, md, cv=5).mean()
            bws[bw] = s

        fbw = max(bws.keys(), key = lambda x: bws[x])
        players[p].append(KernelDensity(bandwidth = fbw).fit(md))
        
# Define function that adds a new player
def add_player(players, p):
    players[p] = [kde]

# Define function that prints the handicap for each player
def handicaps(players, *ps):
    means = {}

    # Pull out expected number of turns for each player
    for p in ps:
        means[p] = players[p][-1].sample(5000).mean()

    # What's the minimum of these averages?
    min_turns = min(means.values())

    # Expected total number of marks for each player in that number of turns
    total_marks = {k: 18 - (18 * min_turns / v) for k, v in means.items()}
    total_marks = {k: round(v, 1) for k, v in total_marks.items()}
    return(total_marks)

# Define function that chooses 6 random darts numbers (no neighbors)
def choosedarts():

    # One copy stays untouched, one has numbers removed
    n_order = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17,
               3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
    n_order2 = n_order

    # Loop that chooses 6 numbers
    chosen = []
    for i in range(6):

        # Choose one number and add it to chosen
        x = random.sample(n_order2, 1)[0]
        chosen.append(x)

        # Find the neighbors that need to be deleted
        x_index = n_order.index(x)
        del_index = [x_index - 1, x_index, (x_index + 1) % 20]
        del_nums = [n_order[j] for j in del_index]

        # Delete neighbors so they won't be sampled next
        n_order2 = [j for j in n_order2 if j not in del_nums]
        
    chosen.sort(reverse = True)

    return(chosen)
