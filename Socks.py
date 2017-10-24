#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:35:53 2017

@author: danielbrannock
"""

import numpy as np

# Define prior distribution for all players
def prior():
    lam = round(np.random.normal(15, 3))
    a = np.random.poisson(lam)
    b = np.random.poisson(lam)
    c = np.random.poisson(lam)
    d = np.random.poisson(lam)
    e = np.random.poisson(lam)
    
    return [a, b, c, d, e, lam]

# Define a game function. Inputs the players and outputs who wins
# Returns the position of each player in the order given
def game():
    p1 = prior()
    p2 = prior()
    p3 = prior()
    
    if p1 < p2:
        if p1 < p3:
            p1p = 1
            if p2 < p3:
                p2p = 2
                p3p = 3
            else:
                p2p = 3
                p3p = 2
        else:
            p1p = 2
            p2p = 3
            p3p = 1
    else:
        if p2 < p3:
            p2p = 1
            if p1 < p3:
                p1p = 2
                p3p = 3
            else:
                p1p = 3
                p3p = 2

    return [p1[5], p2[5], p3[5], p1p, p2p, p3p]
            
        
# Run n iterations of the four games we played
    
