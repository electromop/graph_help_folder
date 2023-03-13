import matplotlib.pyplot as plt # библиотека визуализации
import networkx as nx # библиотека графов
import os # библиотека работы системы, в частности создания файлов

def koor_to_set(a, b, c):
    koor = str(a) + str(b) + str(c)
    return frozenset(koor)

path_to_dir = 'graphs'

if os.path.exists(path_to_dir) == False: # это проверка на наличие папки graphs, если есть то уже новую создавать не будет 
    os.mkdir(path_to_dir)

colors_of_edges = {1: 'red', 2: 'green'} # небольшой словарь цветов
num_of_edges = 5 # вводим в переменную кол-во вершин графа

G = nx.complete_graph(num_of_edges) # далее создаем все переменные для будущего графа
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos=pos, edge_color='red')

num = 0 # переменная для создания новых пнгешек графов по нумерации graph1 ... graph + num

for c in range(1):
    x, y, z = 0, 1, num_of_edges # вводим перменные для того чтобы с помощью цикла пробежать по всем возможым тройкам
    koor_of_edges = []
    for i in range(num_of_edges**2): # начало цикла пробега по всем вариантам
        while z != 0:
            z -= 1
            if koor_to_set(x, y, z) not in koor_of_edges:
                if z != x and z != y:
                    # print(koor_to_set(x, y, z))
                    num += 1
                    # print(z)
                    nx.draw_networkx(G, pos=pos, node_color='black', edge_color='black')
                    nx.draw(G.subgraph([x, y, z]), pos=pos, node_color=colors_of_edges[c], edge_color=colors_of_edges[c])
                    plt.savefig(path_to_dir + '/graph' + str(num))
                    plt.show()
                    koor_of_edges.append(koor_to_set(x, y, z))
        x += 1
        y += 1
        if x == 4:
            y = 0
        z = num_of_edges
