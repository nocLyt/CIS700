import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def get_para():
    return 500, 16, 0.1


def degree_list():
    dc = dict()   # (degree, number of node)
    for u in g.nodes():
        d = g.degree(u)
        dc[d] = dc.get(d, 0) + 1
    degrees = dc.keys()
    num_nodes = dc.values()
    return degrees, num_nodes


def plot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, 'ro')
    ax.plot(x, y, 'k')
    ax.set_xlabel('Degree')
    ax.set_ylabel('Number of node')
    plt.show()


if __name__ == '__main__':
    n, k, p = get_para()

    # 1. Generate  Random Graph, undirected graph
    g = nx.watts_strogatz_graph(n, k, p)
    # print g.edges()
    print g.number_of_edges()
    # print g.nodes()

    # 2. the clustering coefficient coefficient
    # ac = nx.average_clustering(g)
    # print "The Average Clustering Coefficient is ", ac

    # 3. degree distribution

    x, y = degree_list()
    plot(x, y)