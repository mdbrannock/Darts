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

# Define players' prior distributions
players = {'aric':   kde,
           'daniel': kde,
           'jenn':   kde,
           'keith':  kde,
           'tom':    kde}
