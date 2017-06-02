# !/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import networkx as nx
import matplotlib.pyplot as plt


plt.figure(1)
plt.title('Graph')

# create G
G = nx.Graph()
G = nx.read_edgelist('/home/brain/workingdir/ComplexNetworks/data/K_Club.txt', create_using=G)
# G = nx.random_graphs.erdos_renyi_graph(100, 0.05)
nx.draw(G)
# plt.savefig("K_Club.png")


# calculate clustering coefficient
c_coe = nx.clustering(G)
with open('Clustering coefficient.txt', 'w') as handle:
    handle.writelines(["%s %s\n" % item for item in c_coe.items()])
# print c_coe

# degree
degree = G.degree()
with open('Degree.txt', 'w') as handle:
    handle.writelines(["%s %s\n" % item for item in degree.items()])
print degree
plt.figure(2)
plt.title('Clustering coefficient')
k = degree.values()
C = c_coe.values()
plt.xlabel('k')
plt.ylabel('C(k)')
plt.loglog(k, C, 'o')

# degree histogram
degree_histogram = nx.degree_histogram(G)
plt.figure(3)
plt.title('Degree histogram')
d = range(len(degree_histogram))
d_h = [z / float(sum(degree_histogram)) for z in degree_histogram]
plt.xlabel('k')
plt.ylabel('Pk')
plt.loglog(d, d_h, 'o')
# print degree_histogram

# shortest path
path = nx.all_pairs_shortest_path(G)
with open('Path.txt', 'w') as handle:
    handle.writelines(["%s %s\n" % item for item in path.items()])

L = []
for i in path.keys():
    for j in path.keys():
        if i != j:
            L.append(len(path[i][j])-1)
s = set(L)
print s
Fs = []
for item in s:
    Fs.append(L.count(item))
P = []
for i in Fs:
    P.append(i/len(L))

plt.figure(4)
plt.title('Shortest path histogram')
d = list(s)
plt.xlabel('d')
plt.ylabel('Pd')
plt.plot(d, P, '-o')
# print path
plt.show()
