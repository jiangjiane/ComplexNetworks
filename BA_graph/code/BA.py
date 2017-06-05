#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import math
from scipy import linalg
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, a, b):
    return a * x + b

# create graph and show
plt.figure('BA')
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
lnx = math.log(float(d[:]))
lnx = [math.log(f, math.e) for f in d[1:]]
lny = [math.log(f, math.e) for f in d_h[1:]]
lnx.insert(0, 0)
lny.insert(0, 0)
a = np.mat([lnx, [1]*len(d)]).T
b = np.mat(lny).T
t, res, rank, s = linalg.lstsq(a, b)
r = t[0][0]
c = t[1][0]
x1 = d
y1 = [math.e**(r*a + c) for a in lnx]
plt.loglog(x1, y1, 'r-')
# x1 = []
# for temp in x:
#     x1.append(float(temp))
# popt, pcov = curve_fit(func, np.array(np.log(d[:])), np.array(np.log(d_h[:])))
# print 'a:', popt[0]
# y1 = [func(i, popt[0], popt[1]) for i in d]
# plt.plot(d, y1, 'r--')
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

