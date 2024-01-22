#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:21:45 2024

@author: katherine
"""


import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns

n_experiments = 1000
heads_count = np.random.binomial(5, 0.5, n_experiments)


heads, event_count = np.unique(heads_count, return_counts=True)

heads

event_count

event_proba = event_count/n_experiments

plt.bar(heads, event_proba, color='mediumpurple')
plt.xlabel('Heads flips (out of 5 tosses)')
_ = plt.ylabel('Event probability')