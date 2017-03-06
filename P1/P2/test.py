import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


if __name__ == '__main__':
    G = nx.path_graph(4)
    centrality = nx.eigenvector_centrality(G)
    print centrality