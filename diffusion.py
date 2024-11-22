#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:55:11 2024

@author: isaacthompson
"""

import numpy as np
import matplotlib.pyplot as plt

def random_walks(n, num_walkers):
    # Initialize positions
    x = np.zeros((num_walkers, n + 1))
    y = np.zeros((num_walkers, n + 1))
    
    for i in range(1, n + 1):  # Start from step 1
        steps = np.random.choice([0, 1], size=num_walkers)  # Choose axis: 0 for x, 1 for y
        directions = np.random.choice([-1, 1], size=num_walkers)  # Choose direction
        x[:, i] = x[:, i - 1] + (steps == 0) * directions  # Update x-axis only if steps == 0
        y[:, i] = y[:, i - 1] + (steps == 1) * directions  # Update y-axis only if steps == 1
        
    return x, y

n = 500
num_walkers = 500

x, y = random_walks(n, num_walkers)

# Compute <x_n^2>
#mean_squared_displacement = np.mean(x**2 + y**2, axis=0)

# Plot results
plt.figure(figsize=(10, 6))
plt.scatter(x,y, color="red")
plt.xlabel("Position in x")
plt.ylabel("Position in y")
plt.title("Diffusion of 500 random particles (n=500)")
plt.grid()
plt.xlim(-60, 60)
plt.ylim(-60, 60)
plt.show()
