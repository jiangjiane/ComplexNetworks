#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math


def func(x, a, u):
    return a*x**u

# create graph and show
plt.figure('BA_Assortative')
plt.subplot(221)
plt.title('Graph')
G = nx.random_graphs.barabasi_albert_graph(1000, 1)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_label=False, node_size=30)

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


# show mixing
mixing = nx.degree_mixing_matrix(G)
plt.matshow(mixing)
plt.colorbar()
plt.show()

# average neighbor degree
average_neighbor_degree = nx.average_neighbor_degree(G)
print average_neighbor_degree

plt.figure('average neighbor degree')
x = average_neighbor_degree.keys()
y = average_neighbor_degree.values()
plt.title('average neighbor degree')
x1 = []
for temp in x:
    x1.append(float(temp))
popt, pcov = curve_fit(func, np.array(x1), np.array(y))
print popt
print pcov
print 'u:', popt[1]
y1 = [func(i, popt[0], popt[1]) for i in x1]
plt.plot(x1, y1, 'r--')
plt.xlabel('k')
plt.ylabel('Knn(K)')
plt.loglog(x, y, 'o')
plt.show()

# degree pearson correlation coefficient
degree_pearson_correlation_coefficient = nx.degree_pearson_correlation_coefficient(G)
print 'degree pearson correlation coefficient:', degree_pearson_correlation_coefficient