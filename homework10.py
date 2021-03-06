# File:     minimize.py
# Author:   Kurt Hamblin
# Description:  Utitlize the Random Class to:
# Simulate dice rolls where the dice weights are sampled from a Rayleigh Distribution

import numpy as np
from scipy import optimize
import matplotlib as mpl
import matplotlib.pyplot as plt
from Random import Random
import matplotlib

# Import my custom matplotlib config and activate it
import my_params
custom_params = my_params.params()
matplotlib.rcParams.update(custom_params)

# Input: X (array-like)
def func(params):
    x = params[0]
    y = params[1]
    
    return (x-1)**2 + (y+3)**2


if __name__ == "__main__":

    global_minima = optimize.minimize(func, x0 = [0,0])

    print(global_minima.x)
    print(f'Global Minima at:\t ({global_minima.x[0]:.3f},{global_minima.x[1]:.3f},{func([global_minima.x[0],global_minima.x[1]]):.3f})')

    
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    
    X, Y = np.meshgrid(x,y)

     
    Z = func([X,Y])
    fig, ax = plt.subplots(figsize = (6,6),subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none', alpha = 0.5, label = 'f(x,y)')
    ax.scatter(global_minima.x[0],global_minima.x[0], func([global_minima.x[0],global_minima.x[1]]) , c = 'r', label = 'Minima')


    ax.set_zlabel('f(x,y)',fontsize = 20)
    ax.set_xlabel('x', fontsize = 20)
    ax.set_ylabel('y',fontsize = 20)

    surf._facecolors2d = surf._facecolor3d
    surf._edgecolors2d = surf._edgecolor3d

    ax.legend()

    
    plt.show()
