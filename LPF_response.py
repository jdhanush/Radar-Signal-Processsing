import numpy as np
from scipy import signal
import matplotlib.pyplot as plt



#############################################################################################
num_taps = 51 # it helps to use an odd number of taps
cut_off = 3000 # Hz
sample_rate = 32000 # Hz



#############################################################################################
# create our low pass filter
h = signal.firwin(num_taps, cut_off, fs=sample_rate)
max_val = round(np.max(h),3)
h = h/max_val




#############################################################################################
#freq domain
nfft = 1024
freq_axis = np.arange(-sample_rate/2, sample_rate/2, sample_rate/nfft)
h_freq = np.fft.fftshift(np.fft.fft(h, nfft))
magnitude_h = np.abs(h_freq/nfft)
h_abs = magnitude_h ** 2
h_dB = 10 * np.log10(h_abs)




#############################################################################################
# plot the impulse response
figure, axes = plt.subplots(2, 1, figsize=(20,12))

axes[0].plot(h, '.-', c='k', label='Implulse response of LPF')
axes[0].grid(True)
axes[0].legend()

axes[1].plot(freq_axis, h_dB, c='b', label='Frequency response of LPF')
axes[1].grid(True)
axes[1].legend()
