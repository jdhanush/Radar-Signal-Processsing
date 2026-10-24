import numpy as np
import matplotlib.pyplot as plt

"""
This code will demonstrate you  amplitudes-scaling of digital signal
"""

#############################################################################################
x = np.array([1, 2, 3, 4, 4, 4,4, 4, 3, 2, 1])   # this is the original signal
n = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])  # this is the initial discrete time-axis

scaling_factor1 = 2.0
x_scaled1 = x * scaling_factor1

scaling_factor2 = 3.0
x_scaled2 = x * scaling_factor2

#############################################################################################
# plotting section
plt.plot(n, x, '.-', c = 'b', label='orginal signal:  x[n]', alpha=0.6)
plt.plot(n, x_scaled1, '.-', c='red', label='scaled signal:  2*x[n]', alpha=0.6)
plt.plot(n, x_scaled2, '.-', c='green', label='scaled signal:  3*x[n]', alpha=0.6)
plt.title('Demo of amplitude-scaled signal')
plt.legend()
plt.xlabel("time axis")
plt.ylabel("amplitude axis")
plt.grid(True)