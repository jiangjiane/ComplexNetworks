#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import networkx as nx
import matplotlib.pyplot as plt

# create edges
f = open('paperauthorID.txt', 'r')
result = []
for line in f.readlines():
    line = line.strip().split('\t')
    result.append(line)

edges = []
for i in range(len(result)):
    for j in range(len(result)):
        if i != j and result[i][0] == result[j][0]:
            edges.append((result[i][1], result[j][1]))
# print edges

# create graph and show
plt.figure('Science Coauthorship')
plt.subplot(221)
plt.title('Graph')
G = nx.Graph(edges)
nx.draw(G)

# Degree_histogram and show
degree_histogram = nx.degree_histogram(G)
d = range(len(degree_histogram))
d_h = [z / float(sum(degree_histogram)) for z in degree_histogram]

plt.subplot(222)
plt.title('Degree histogram')
plt.xlabel('k')
plt.ylabel('Pk')
plt.loglog(d, d_h, 'o')

# cumulative plot
plt.subplot(223)
plt.title('Degree histogram cumulative plot')
d_h1 = []
for k in range(len(d_h)):
    d_h1.append(sum(d_h[k:]))
for h in range(len(d_h)):
    if d_h[h] == 0.0:
        d_h1[h] = d_h[h]
plt.xlabel('k')
plt.ylabel('Pk')
plt.loglog(d, d_h1, 'o')

# Log-binned
d1 = []
d_h2 = []
for n in range(8):
    if 2**n <= max(d):
        d1.append(sum(d[2**n-1:2**(n+1)-1])/len(d[2**n-1:2**(n+1)-1]))
        d_h2.append(sum(d_h[2**n-1:2**(n+1)-1])/len(d_h[2**n-1:2**(n+1)-1]))
    else:
        if len(d[2**n-1:]) != 0:
            d1.append(sum(d[2**n-1:])/len(d[2**n-1:]))
            d_h2.append(sum(d_h[2**n-1:])/len(d_h[2**n-1:]))

plt.subplot(224)
plt.title('Log-binned')
plt.xlabel('k')
plt.ylabel('Pk')
plt.loglog(d1, d_h2, 'o')
plt.show()
