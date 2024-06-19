import energy
import noises
import numpy as np
from graphics import *
from filter import *
from emg import generate_emg_signal


# Frequência de amostragem
fs = 1000 
# Duração do sinal (segundos)
T = 4 
# Número de amostras
N = fs * T 
# Tempo
t = np.linspace(0, T, N, endpoint=False)

emg_signal = generate_emg_signal(t)

# Sinal EMG limpo
#plot_graphic(t, emg_signal, 'Sinal EMG simulado')

# Ruídos
wgn = noises.wgn(0.007, N)
pli = noises.pli(0.007, t)
bw = noises.bw(0.015, t)
noise = wgn + pli + bw

# Sinal EMG com ruídos
noisy_emg = emg_signal + noise
SNR = energy.calculate_snr(emg_signal, noise)
print(f'SNR: {SNR:.2f} dB')
#plot_graphic(t, noisy_emg, 'EMG com ruído')

# Decompondo o sinal
imfs, imfs_freq, freqs = vmd_decomposition(noisy_emg, fs, 8)

plot_graphics([4, 2], freqs, imfs_freq, 'IMFs no domínio da frequência',
              'IMF')