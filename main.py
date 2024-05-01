import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage.transform import radon

def fourier2D(imagem):
    '''
    Faz a transformada de Fourier de 2 dimensões de uma imagem.
    Retorna o espectro de magnitudes.
    '''
    # Aplicar a Transformada de Fourier 2D
    transformada = np.fft.fft2(imagem)

    # Deslocar a transformada para que as baixas frequências fiquem no centro
    transformada_deslocada = np.fft.fftshift(transformada)

    # Calcular o espectro de magnitude (magnitude da transformada)
    espectro_magnitude = np.abs(transformada_deslocada)

    return espectro_magnitude


def gerar_sinograma(imagem):
    '''
    Gera o sinograma a partir de uma imagem.
    '''
    # Definir os ângulos para a projeção
    theta = np.linspace(0., 180., max(imagem.shape), endpoint=False)

    # Projetar a imagem em diferentes ângulos (radon transform)
    sinograma = radon(imagem, theta=theta)

    # Plotar o sinograma
    plt.figure(figsize=(10, 5))
    plt.imshow(sinograma, cmap='gray', extent=(0, 180, 0, sinograma.shape[0]), aspect='auto')
    plt.colorbar(label='Intensidade')
    plt.xlabel('Ângulo (graus)')
    plt.ylabel('Posição da projeção')
    plt.title('Sinograma')
    plt.show()


# Carregar a imagem
imagem = mpimg.imread('Imagens/phantom2.png')

# Mostrar a imagem
plt.imshow(imagem)
plt.title('Imagem original')
plt.axis('on')
plt.show()

# Converter a imagem para escala de cinza se necessário
if len(imagem.shape) > 2:
    imagem = np.mean(imagem, axis=2)

gerar_sinograma(imagem)

