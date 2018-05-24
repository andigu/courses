from copy import deepcopy
from random import choice
from typing import Dict

from time import clock as now


class Graph:
    vertices: Dict[int, Dict[int, int]] = {}  # value is dictionary of nbrs that tracks number of edges to that nbr
    m: int = 0
    n: int = 0

    def contract(self):
        u = choice(list(self.vertices.keys()))
        v = choice(list(self.vertices[u].keys()))
        del self.vertices[u][v]
        v_e = self.vertices.pop(v)
        self.m -= v_e[u]
        for nbr in v_e:
            if nbr != u:
                old = self.vertices[nbr][v] + (self.vertices[nbr][u] if u in self.vertices[nbr] else 0)
                self.vertices[nbr][u] = old
                self.vertices[u][nbr] = old
                del self.vertices[nbr][v]
        self.n -= 1


best = 10000000000
vertices = {}
m = 0
n = 0
with open('mincut.txt', 'r') as f:
    for line in f.readlines():
        n += 1
        data = [int(x) for x in line.replace('\t', ' ').strip().split(' ')]
        vertices[data[0]] = {}
        for j in data[1:]:
            vertices[data[0]][j] = 1
            m += 1
m //= 2

g = Graph()
s = now()
for trial in range(int(4.61 * n * n)):
    g.vertices = deepcopy(vertices)
    g.m = m
    g.n = n
    while g.n > 2:
        g.contract()
    best = min(best, g.m)
    if trial % 250 == 0:
        print(trial, best, now() - s)
print(best)
