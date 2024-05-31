import numpy as np
import matplotlib.pyplot as plt

# Parâmetros

# Frequência de amostragem
Fs = 1000 
# Duração do sinal (segundos)
T = 4 
# Número de amostras
N = Fs * T 

# Tempo
t = np.linspace(0, T, N, endpoint=False)


def generate_emg_signal(t, num_pulses=60):
    '''Gerar sinal EMG básico: uma série de pulsos gaussianos.

    :param t: série de tempo.
    :param num_pulses: quantidade de pulsos gaussianos.

    :return: sinal EMG.
    '''
    signal = np.zeros_like(t)

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

emg_signal = generate_emg_signal(t)

# Normalizar o sinal
# emg_signal = (emg_signal - np.mean(emg_signal)) / np.std(emg_signal)

plt.figure(figsize=(15, 8))
plt.plot(t, emg_signal)
plt.title('Sinal EMG simulado')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')

plt.show()