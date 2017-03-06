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


def global_clustering_coefficient(g):
    gcc = nx.transitivity(g)
    print "Average Global Clustering Coefficient of this graph is", gcc


def local_clustering_coefficient(g):
    lcc = nx.average_clustering(g)
    print "Average Local Clustering Coefficient of this graph is", lcc




if __name__ == '__main__':

    g = buid_nx_graph(FNAME1)
    print g.number_of_nodes(), g.number_of_edges()

    # global clustering coefficient  is  nx.transitivity(G) = num of triangles * 3 / num of triads
    global_clustering_coefficient(g)
    # local clustering coefficient is average_clustering(g)
    local_clustering_coefficient

