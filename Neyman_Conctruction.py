# File:     Neyman_Construction.py
# Author:   Kurt Hamblin
# Description:  Demonstrate Neyman Construction

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from Random import Random
import matplotlib

# Import my custom matplotlib config and activate it
import my_params
custom_params = my_params.params()
matplotlib.rcParams.update(custom_params)

# sample data with rayleigh dist
def sample_data(Nexp, Nmeas):
    rand = Random()
    
    
    mu_true_arr = np.array([])
    mu_meas_arr = np.array([])
    
    for i in range(-100, 100):
        mu_true = i/10.
        
        for j in range(Nexp):
            mu_meas = 0
            
            for k in range(Nmeas):
                mu_meas += rand.Rayleigh(mu_true) / Nmeas
            mu_true_arr = np.append(mu_true_arr, mu_true)
            mu_meas_arr = np.append(mu_meas_arr, mu_meas)
        print(f'i number: {i}')
    np.savetxt('x_meas.txt', mu_meas_arr)
    np.savetxt('x_true.txt', mu_true_arr)



# main function for this Python code
if __name__ == "__main__":

    Nexp = 10**3
    Nmeas = 1
    
    # sample the data to plot; only need to run once
    # sample_data(Nexp, Nmeas)

    x_meas = np.loadtxt('x_meas.txt')
    x_true_plot = np.loadtxt('x_true.txt')
    
    #print(f'Efficiency: {eff:.4f}%')
    fig, ax = plt.subplots(figsize = (10,7))
    ax.set_ylabel(r'$\mu_{meas}$')
    ax.set_xlabel(r'$\mu_{true}$')
    
    y_bins = np.linspace(np.min(x_meas), np.max(x_meas), 50)
    x_bins = np.linspace(-10, 10, 50)
    
    hist = ax.hist2d(x = x_true_plot, y = x_meas, bins = [30,100] , density = False, alpha = 1.0, cmap='Blues')
    cbar = plt.colorbar(hist[3], fraction=0.046, pad=0.04, ax = ax)

    cbar.set_label('Counts')

    
    ax.set_xlim([-10,10])
    ax.set_ylim([-10, 10])
    
    plt.show()
