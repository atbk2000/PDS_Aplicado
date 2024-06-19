import numpy as np

def wgn(level, N):
    '''Gera ruído WGN (White Gaussian Noise).

    :param level: nível do ruído.
    :param N: quantidade de amostras.

    :return: ruído WGN.
    '''
    return level * np.random.randn(N)


def pli(amplitude, N):
    '''Gera ruído PLI (Power Line Interference).
    Ruído de 60 Hz.
    
    :param amplitude: amplitude do sinal de ruído.
    :param N: quantidade de amostras (vetor).

    :return: ruído PLI
    '''
    return amplitude * np.sin(2 * np.pi * 60 * N)


def bw(amplitude, N):
    '''Gera ruído BW (Baseline Wander).
    Ruído de baixa frequência.
    
    :param amplitude: amplitude do sinal de ruído.
    :param N: quantidade de amostras (vetor).

    :return: ruído BW
    '''
    freq_bw = 0.5
    return amplitude * np.sin(2 * np.pi * freq_bw * N)