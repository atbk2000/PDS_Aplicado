import numpy as np

def calculate_energy(signal):
    '''Calcula a energia de um sinal.

    :param signal: sinal.

    :return: energia do sinal.
    '''
    return np.sum(np.square(signal))

def calculate_snr(signal, noise):
    '''Calcula a SNR entre o sinal e o ruído.

    :param signal: sinal.
    :param noise: ruído.

    :return: SNR em dB.
    '''
    signal_energy = calculate_energy(signal)
    noise_energy = calculate_energy(noise)
    return 10 * np.log10(signal_energy/noise_energy)