import numpy as np
from scipy.fft import fft, ifft
signal = np.array([1, 2, 3, 4, 5])
print("Fourier Transform:\n", fft(signal))
print("Inverse Fourier Transform:\n", ifft(signal))
