# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:17:31 2017

@author: mdbrannock
"""

# Second Attempt. Using density approximations to build iterative posterior
# distributions.
import numpy as np
from sklearn.neighbors.kde import KernelDensity
from sklearn.grid_search import GridSearchCV

# Define dictionary with starting prior distribution for every player.
# The original prior will just be a normal distribution [u, s]. However, to
# keep the formatting consistent, it would be nice to have the type of object
# be the same for the first prior as all the other priors. As a result, we'll
# build a density approximation of a normal distribution and use that.

# Build density approximation using scikit learn:
# https://jakevdp.github.io/blog/2013/12/01/kernel-density-estimation/
# Well, nevermind, that's deprecated. New version:
# http://scikit-learn.org/stable/modules/cross_validation.html

# Use CV to get best bandwidth. Use kde.score() as the evualation metric.
X = np.array(np.random.normal(15, 3, 100))[:, np.newaxis]
kde = KernelDensity(bandwidth=0.2).fit(X)



# Define players
players = {'aric':   [15, 3],
           'daniel': [15, 3],
           'jenn':   [15, 3],
           'keith':  [15, 3],
           'tom':    [15, 3]}