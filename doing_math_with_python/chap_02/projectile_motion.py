'''
Desenha a trajetória de uma corpo em lançamento oblíquo
'''

import math
import matplotlib.pyplot as plt
from numpy import mat


def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    return numbers

def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel('Coordenada x')
    plt.ylabel('Coordenada y')
    plt.title('Lançamento Oblíquo de uma bola')

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8

    # Tempo de voo
    t_flight = 2 * u * math.sin(theta) / g
    # Intervalos de tempo
    intervals = frange(0, t_flight, 0.001)
    # Lista das coordenadas x e y
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t ** 2)

    draw_graph(x,y)


if __name__ == '__main__':
    try:
        u = float(input('Entre com a velocidade inicial (m/s): '))
        theta = float(input('Entre com o ângulo de lançamento do projétil (graus): '))
    except ValueError:
        print('Você inseriu valores inválidos!!')
    else:
        draw_trajectory(u, theta)
        plt.show()

