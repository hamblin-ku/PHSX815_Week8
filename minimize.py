# File:     minimize.py
# Author:   Kurt Hamblin
# Description:  Utitlize the Random Class to:
# Simulate dice rolls where the dice weights are sampled from a Rayleigh Distribution

import numpy as np
from scipy.optimize import fmin, fminbound
import matplotlib as mpl
import matplotlib.pyplot as plt
from Random import Random
import matplotlib

# Import my custom matplotlib config and activate it
import my_params
custom_params = my_params.params()
matplotlib.rcParams.update(custom_params)

# Input: X (array-like)
def func(x):
    return x**2 + 10*np.sin(x)


if __name__ == "__main__":

    global_minima = fmin(func, 0)
    local_minima = fminbound(func,0,10)

    print(f'Global Minima at:\t ({global_minima[0]:.3f},{func(global_minima[0]):.3f})')
    print(f'Local Minima at:\t ({local_minima:.3f},{func(local_minima):.3f})')
    
    x = np.arange(-10, 10, 0.1)
    x_minima = np.array( [global_minima[0], local_minima] )
    
    fig, ax = plt.subplots(figsize = (6,6))
    ax.plot(x, func(x), label = r'$f(x)$', c = 'b', zorder = 0)
    ax.scatter(x_minima, func(x_minima), c='r', label = 'Minima', zorder = 1)
    ax.set_xlim([-10,10])
    ax.set_ylabel('f(x)')
    ax.set_xlabel('x')
    
    globmin_text = f'({global_minima[0]:.3f},{func(global_minima[0]):.3f})'
    localmin_text = f'({local_minima:.3f},{func(local_minima):.3f})'
    
    ax.annotate( text = globmin_text , xy = (  global_minima[0], func(global_minima[0])), xytext = (-9, -5) ,arrowprops = dict(facecolor='black', shrink = 0.01, width = 0.5, headwidth = 8), fontsize = 14)
    
    ax.annotate( text = localmin_text , xy = (  local_minima, func(local_minima)), xytext = (1, 25) ,arrowprops = dict(facecolor='black', shrink = 0.01, width = 0.5, headwidth = 8), fontsize = 14)
    
    ax.text(-7.5, 60, r'$f(x) = x^2+10\sin{x}$')
    
    ax.legend()
    
    plt.show()
