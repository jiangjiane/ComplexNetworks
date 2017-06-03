#! /usr/bin/python
# -*- coding: utf-8 -*-

# from __future__ import division
import networkx as nx
import random
import community
import numpy as np
import matplotlib.pyplot as plt

# GN benchmark
zin = 13
zout = 3

N = 128
C = 4

n = N/C
nodes = []
nall = []
for a in ['a', 'b', 'c', 'd']:
    xx = []
    for i in range(n):
        xx.append(a+str(i))
    nodes += xx
    nall.append(xx)

pin = 1.0*zin/(n-1)/2
pout = 1.0*zout/(3*n-1)/2

g = nx.Graph()

for nc in nall:
    for i in nc:
        for j in nc:
            if i == j:
                continue
            p = random.random()
            if p < pin:
                g.add_edge(i, j)
        for j in set(nodes)-set(nc):
            p = random.random()
            if p < pout:
                g.add_edge(i, j)

lap_g = nx.laplacian_matrix(g)  # laplacian matrix of g
eigval, eigvec = np.linalg.eigh(lap_g)
# print eigvec
plt.figure('Girvan Newman')
plt.subplot(121)
plt.title('Graph')
plt.plot(eigvec[:, 1], eigvec[:, 2], 'o')

# first compute the best partition
partition = community.best_partition(g)
# print partition

# drawing
plt.subplot(122)

plt.title('Girvan Newman Network')
size = float(len(set(partition.values())))
pos = nx.spring_layout(g)
count = 0.

colors = ['r', 'g', 'b', 'y']
for com in set(partition.values()):
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
    nx.draw_networkx_nodes(g, pos, list_nodes, node_size=20, node_color=colors[com])

nx.draw_networkx_edges(g, pos, alpha=0.5)

# modularity
m = community.modularity(partition, g)
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
plt.text(xmax-0.1, ymax-0.05, "Modularity: %s" % m, fontsize=12, verticalalignment='top', horizontalalignment='right')
# print m
plt.savefig('Girvan Newman.png')
plt.show()
