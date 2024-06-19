import matplotlib.pyplot as plt

def plot_graphic(x, y, title, labelx='Tempo (s)', labely='Amplitude'):
    '''Plota gráfico X-Y.

    :param x: eixo X.
    :param y: eixo Y.
    :param title: título do gráfico.
    :param labelx: rótulo do eixo X.
    :param labely: rótulo do eixo Y.
    '''
    plt.figure(figsize=(15, 8))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.show()

def plot_graphics(matrix, x, y, title, labelsy):
    '''Plota matriz de gráficos X-Y.

    :param matrix: matriz com quantidade de linhas e colunas para a visualização
    dos gráficos.
    :param x: eixo x dos gráficos.
    :param y: vetor com valores dos eixos y dos gráficos.
    :param title: título do gráfico.
    :param labelsy: rótulos dos eixo Y.
    '''
    lines = matrix[0]
    columns = matrix[1]

    plt.figure(figsize=(15, 8))
    plt.title(title)
    fig = 0
    for i in range(columns):
        for j in range(lines):
            plt.subplot(lines, columns, fig+1)
            plt.plot(x, y[fig])
            plt.ylabel(f'{labelsy}{fig+1}')
            fig += 1
    
    plt.show()
    
