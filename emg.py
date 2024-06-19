import numpy as np

def generate_emg_signal(t, num_pulses=60):
    '''Gerar sinal EMG básico: uma série de pulsos gaussianos.

    :param t: série de tempo.
    :param num_pulses: quantidade de pulsos gaussianos.

    :return: sinal EMG.
    '''
    signal = np.zeros_like(t)

    # Duração do sinal EMG
    T = max(t)

    for i in range(num_pulses):
        pulse_time = np.random.uniform(0, T)
        pulse_width = np.random.uniform(0.005, 0.009)
        pulse_height = np.random.uniform(0.05, 0.5)
        pulse = pulse_height * np.exp(-((t - pulse_time)**2) / (2 * (pulse_width**2)))
        if i % 2 == 0:
            signal += pulse
        else:
            signal -= pulse

    return signal