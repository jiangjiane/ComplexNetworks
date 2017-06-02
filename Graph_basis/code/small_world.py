# !/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import networkx as nx


def Create_Graph(n, k, p):
    WS = nx.random_graphs.watts_strogatz_graph(n, k, p)
    return WS, n, k, p

def Clust_coe(G):
    c_coe = nx.clustering(G[0])  # calculate clustering coefficient
    degree = G[0].degree()  # degree
    with open('Degree.txt', 'w') as handle:
        handle.writelines(["%s %s\n" % item for item in degree.items()])
    k = degree.values()
    c = c_coe.values()
    return k, c

def Degree_histogram(G):
    degree_histogram = nx.degree_histogram(G[0])
    d = range(len(degree_histogram))
    d_h = [z / float(sum(degree_histogram)) for z in degree_histogram]
    return d, d_h

def Shortest_path(G):
    path = nx.all_pairs_shortest_path(G[0])

    L = []
    for i in path.keys():
        for j in path.keys():
            if i != j:
                L.append(len(path[i][j]) - 1)
    s = set(L)
    Fs = []
    for item in s:
        Fs.append(L.count(item))
    P = []
    for i in Fs:
        P.append(i / len(L))
    d = list(s)
    return d, P

def show(G):
    if 'plt' not in dir():
        import matplotlib.pyplot as plt
    # show G
    plt.figure('WS网络及其特性')
    plt.subplot(221)
    plt.title('Graph_WS(n=%s,k=%s,p=%s)' % (G[1], G[2], G[3]))
    nx.draw(G[0])
    # show coe
    k_c = Clust_coe(G)
    plt.subplot(222)
    plt.title('Clustering coefficient')
    plt.xlabel('k')
    plt.ylabel('C(k)')
    plt.loglog(k_c[0], k_c[1], 'o')
    # show degree histogram
    d_h = Degree_histogram(G)
    plt.subplot(223)
    plt.title('Degree histogram')
    plt.xlabel('k')
    plt.ylabel('Pk')
    plt.loglog(d_h[0], d_h[1], 'o')
    # shortest path
    path = Shortest_path(G)
    plt.subplot(224)
    plt.title('Shortest path histogram')
    plt.xlabel('d')
    plt.ylabel('Pd')
    plt.plot(path[0], path[1], '-o')
    plt.show()


if __name__ == '__main__':
    WS = Create_Graph(100, 4, 0.05)
    show(WS)

