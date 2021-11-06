'''
Relação entre a força gravitacional e a distância entre dois corpos
'''

import matplotlib.pyplot as plt

# Gráfico
def draw_graph(x,y):
    plt.plot(x,y, marker='o')
    plt.xlabel('Distância em metros')
    plt.ylabel('Força gracitacional em Newtons')
    plt.title('Força Gravitacional e Distância')
    plt.show()

def generate_F_r():
    # Gera valores para r
    r = range(100, 1001, 50)
    # Lista vazia para armazenar os valores de F
    F = []
    # Constante G
    G = 6.674e-11
    # Duas massas
    m1, m2 = 0.5, 1.5
    # Cálculo da força e adição à lista F
    for dist in r:
        force = G * (m1 * m2) / (dist ** 2)
        F.append(force)
    # Chama a função draw_graph
    draw_graph(r, F)

if __name__ == '__main__':
    generate_F_r()