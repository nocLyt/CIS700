import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
FNAME1 = "../P0/edge_id.txt"


def buid_nx_graph(fname):
    f = open(fname)
    ug = nx.Graph()
    for line in f.readlines():
        u, v = map(int, line.strip().split(','))
        ug.add_edge(u, v)
    f.close()
    return ug


if __name__ == '__main__':
    ug = buid_nx_graph(FNAME1)
    print "The number of node ", ug.number_of_nodes()
    print "The diameter of this graph is ", nx.diameter(ug)
