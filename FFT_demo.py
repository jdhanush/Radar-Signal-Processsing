import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt



#############################################################################################
fc = 50
relative_samp_rate = 8
Fs = relative_samp_rate * fc
Ts = 1/Fs
nfft = 256
time_axis = Ts * np.arange(nfft)

no_of_cycles = 20
time_window = no_of_cycles/fc
no_of_samples = int(time_window * Fs)



#############################################################################################
#signal_timedomain = 1*np.sin(2 * np.pi * fc * time_axis) + 2*np.sin(2 * np.pi * fc/2 * time_axis) 
signal_timedomain = 2.5 * np.exp(1j* 2 * np.pi * fc * time_axis)
#signal_timedomain = 1*np.exp(1j* 2 * np.pi * f * time_axis) + 2*np.exp(1j* 2 * np.pi * f/2 * time_axis) - 0.5

true_noise_std = 1
signal_timedomain = signal_timedomain + 2*(rd.normal(0, true_noise_std, size=len(time_axis)) + 1j* rd.normal(0, true_noise_std, size=len(time_axis)) ) 



#############################################################################################
# Frequency Domain (FFT)
complex_fftpoints = np.fft.fftshift(np.fft.fft(signal_timedomain, nfft))
magnitude_complex_fftpoints =  np.abs(complex_fftpoints/nfft)
PSD_Abs = magnitude_complex_fftpoints**2
PSD_dB = 10 * np.log10(PSD_Abs)
freq_axis = np.arange(-Fs/2, Fs/2, Fs/nfft)

# IFFT
signal_ifft = np.fft.ifft(PSD_Abs)




#############################################################################################
# Plotting Section
figure, axes = plt.subplots(3,1, figsize=(20, 15))

# Time Domain
axes[0].plot(time_axis[:no_of_samples], signal_timedomain.real[:no_of_samples])  
axes[0].grid(True)
axes[0].set_title("Time Domain")

# Frequency Domain (Abs)
axes[1].plot(freq_axis, magnitude_complex_fftpoints)  
axes[1].grid(True)
axes[1].set_title("Freq Domain (Abs)")

# Frequency Domain (log)
axes[2].plot(freq_axis, PSD_dB)  
axes[2].grid(True)
axes[2].set_title("Freq Domain (dB)")
#plt.grid(True)

# # Inverse Fourier Transform
# axes[2].plot(time_axis[:no_of_samples], signal_ifft.real[:no_of_samples])  
# axes[2].grid(True)
# axes[2].set_title("IFFT Time Domain")
# #plt.grid(True)



