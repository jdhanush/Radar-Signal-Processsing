import numpy as np
import matplotlib.pyplot as plt

"""
This code will demonstrate you time-revarsal of digital signal
"""


#############################################################################################
x = np.array([1, 2, 4, 5, 6, 9, 12])   # this is the original signal
n = np.array([-2, -1, 0, 1, 2, 3, 4])  # this is the initial discrete time-axis



#############################################################################################
#  x[::-1] reverses the array
x_reversed = x[::-1]            # this is the time-reveresed signal
n_reversed = -n[::-1]           # this is the reversed time axis
# time axis is both reversal of order and change of sign 



#############################################################################################
# plotting section
plt.plot(n, x, '.-', c = 'b', label='orginal signal:  x[n]', alpha=0.6)
plt.plot(n_reversed, x_reversed, '.-', c='red', label='time reversed signal:  x[-n]', alpha=0.6)
plt.title('Demo of time reversal of signal')
plt.legend()
plt.grid(True)