import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
FNAME1 = "../P0/edge_id.txt"


class DirectedUnweightedGraph:
    def __init__(self):
        self.mat = dict()  # {(id, [id, ...]), ...}
        self.indegree = dict()
        self.outdegree = dict()
        self.n = 0
        self.m = 0

    def check_node(self, u):
        if u not in self.mat:
            self.mat[u] = set()
            self.n += 1
        return


    def add_edge(self, u, v):
        self.check_node(u)
        self.check_node(v)
        self.mat[u].add(v)
        self.m += 1
        self.add_out_degree(u)
        self.add_in_degree(v)

    def add_in_degree(self, u):
        self.indegree[u] = self.indegree.get(u, 0) + 1

    def add_out_degree(self, u):
        self.outdegree[u] = self.outdegree.get(u, 0) + 1

    def clear(self):
        self.dc = dict()
        self.n = 0
        self.m = 0
        self.indegree = dict()
        self.outdegree = dict()

    def get_in_degree(self, u):
        return self.indegree.get(u, 0)

    def get_out_degree(self, u):
        return self.outdegree.get(u, 0)

    def readfile(self, fname):
        f = open(fname)
        for line in f.readlines():
            u, v = map(int, line.strip().split(','))
            self.add_edge(u, v)
        f.close()

    def __str__(self):
        return "Graph No. node = %d, No. edge = %d" % (self.n, self.m)




def plot_in_degree(g):
    dc = dict()   # (degree, number of node)
    for u in range(g.n):
        d = g.get_in_degree(u)
        dc[d] = dc.get(d, 0) + 1
    degrees = dc.keys()
    num_node = dc.values()

    fig, ax = plt.subplots()
    ax.plot(degrees, num_node, 'ro')
    ax.plot(degrees, num_node, 'k')
    plt.show()


def plot_out_degree(g):
    dc = dict()   # (degree, number of node)
    for u in range(g.n):
        d = g.get_out_degree(u)
        dc[d] = dc.get(d, 0) + 1
    degrees = dc.keys()
    num_node = dc.values()

    fig, ax = plt.subplots()
    ax.plot(degrees, num_node, 'ro')
    ax.plot(degrees, num_node, 'k')
    plt.show()


def get_diameter():
    pass


def buid_nx_graph(fname):
    f = open(fname)
    ug = nx.Graph()
    for line in f.readlines():
        u, v = map(int, line.strip().split(','))
        ug.add_edge(u, v)
    f.close()
    return ug



g = DirectedUnweightedGraph()

if __name__ == '__main__':
    g.readfile(FNAME1)
    print g
    # plot degree
    plot_in_degree(g)
    plot_out_degree(g)
    # diameter
    pass