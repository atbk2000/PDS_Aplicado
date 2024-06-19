import numpy as np
from vmdpy import VMD


def get_fft(signals, fs):
    '''Executa a transformada rápida de Fourier dos sinais e calcula os
    módulos das ffts.

    :param signals: sinais no domínio do tempo.
    :param fs: frequência de amostragem.

    :return ffts, freqs: módulos das ffts e respectivas frequências.
    '''
    ffts, freqs = [], []
    # Faixa de frequência de interesse
    max_frequency = 500
    # Frequências correspondentes
    frequencies = np.fft.fftfreq(len(signals[0]), d=1/fs)
    # Filtrar para obter apenas as frequências positivas
    positive_frequencies = frequencies[:len(frequencies)//2]
    filtered_indices = positive_frequencies <= max_frequency
    for i in range(len(signals)):
        # FFT da série temporal
        fft_values = np.fft.fft(signals[i])
        positive_fft_values = fft_values[:len(fft_values)//2]
        ffts.append(positive_fft_values[filtered_indices])

    freqs = positive_frequencies[filtered_indices]

    return ffts, freqs


def vmd_decomposition(function, fs, K):
    """Executa a decomposição VMD (Variational Mode Decomposition)
    para a geração das IMFs (Intrinsic Mode functions).

    :param function: função a ser decomposta.
    :param fs: frequência de amostragem.
    :param K: número de modos do VMD.

    :return imf, imf_freq, freqs: IMFs no domínio do tempo, da frequência
    e respectivas frequências.
    """

    # Sample parameters for VMD  
    alpha = 2000       # moderate bandwidth constraint  
    tau = 0.           # noise-tolerance (no strict fidelity enforcement)
    DC = 0             # no DC part imposed  
    init = 1           # initialize omegas uniformly  
    tol = 1e-7         # tolerance

    # Executa código VMD 
    imf, imf_hat, omega = VMD(function, alpha, tau, K, DC, init, tol)

    imf_freq, freqs = get_fft(imf, fs)

    return imf, imf_freq, freqs 
