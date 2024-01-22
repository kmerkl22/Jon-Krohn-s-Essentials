#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:04:34 2024

@author: katherine
"""

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns

ns = np.array([2,4,8,16,32,64,128,256,512,1024,2048,4096])
np.random.seed(42)

np.random.binomial(1,0.5)

heads_count = [np.random.binomial(n,0.5) for n in ns]

heads_count

proportion_heads = heads_count/ns
proportion_heads

fig, ax = plt.subplots()
plt.xlabel('Number of coin flips in experiment')
plt.ylabel('Proportion of flips that are heads')
plt.axhline(0.5, color='orange')
_ = ax.scatter(ns, proportion_heads)

