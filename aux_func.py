# data analysis 
import numpy as np
import matplotlib.pyplot as plt

def plot_hist(dataset):
    x1 = dataset[:,0]
    x2 = dataset[:,1]
    x3 = dataset[:,2]
    x4 = dataset[:,3]
    x5 = dataset[:,4]
    x6 = dataset[:,5]
    x7 = dataset[:,6]
    x8 = dataset[:,7]
    x9 = dataset[:,8]

    fig, axs = plt.subplots(3, 4)                        
    axs[0, 0].hist(x1, 10, density=True, facecolor='g', alpha=0.75)               
    axs[0, 0].set_title('Par 1')
    
    axs[0, 1].hist(x2, 10, density=True, facecolor='g', alpha=0.75)               
    axs[0, 1].set_title('Par 2')
    
    axs[0, 2].hist(x3, 10, density=True, facecolor='g', alpha=0.75)               
    axs[0, 2].set_title('Par 3')
    
    axs[0, 3].hist(x4, 10, density=True, facecolor='g', alpha=0.75)                   
    axs[0, 3].set_title('Par 4')
    
    axs[1, 0].hist(x5, 10, density=True, facecolor='g', alpha=0.75)                   
    axs[1, 0].set_title('Par 5')
    
    axs[1, 1].hist(x6, 10, density=True, facecolor='g', alpha=0.75)              
    axs[1, 1].set_title('Par 6')
    
    axs[1, 2].hist(x7, 10, density=True, facecolor='g', alpha=0.75)               
    axs[1, 2].set_title('Par 7')
    
    axs[1, 3].hist(x8, 10, density=True, facecolor='g', alpha=0.75)               
    axs[1, 3].set_title('Par 8')
    
    axs[2, 0].hist(x9, 2, density=True, facecolor='g', alpha=0.75)               
    axs[2, 0].set_title('BinClass')
    
    plt.tight_layout()
    plt.show()
