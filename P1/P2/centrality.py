import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
FNAME1 = "../P0/edge_id.txt"


def buid_nx_directed_graph(fname):
    f = open(fname)
    ug = nx.DiGraph()
    for line in f.readlines():
        u, v = map(int, line.strip().split(','))
        ug.add_edge(u, v)
    f.close()
    return ug


def get_top_3(dc):
    return sorted(dc.items(), reverse=True, key=lambda x: x[1])[:3]


def print_format(title, ret):
    print "--------------------------"
    print "Top 3 %d Node: " % title
    for id, value in ret:
        print "id = %d, Page Rank value = %f" %(id, value)


def cal_page_rank(g):
    pr = nx.pagerank(g)
    ret = get_top_3(pr)
    print_format("Page Rank", ret)


def cal_eigenvector_centrality(g):
    ec = nx.eigenvector_centrality(g)
    ret = get_top_3(ec)
    print_format("Eigenvector Centrality", ret)


def cal_degree_centrality(g):
    dc = nx.degree_centrality(g)
    ret = get_top_3(dc)
    print_format("Degree Centrality", ret)


if __name__ == '__main__':

    g = buid_nx_directed_graph(FNAME1)
    print g.number_of_nodes(), g.number_of_edges()

    # # global clustering coefficient  is  nx.transitivity(G) = num of triangles * 3 / num of triads
    # global_clustering_coefficient(g)
    # # local clustering coefficient is average_clustering(g)
    # local_clustering_coefficient


    cal_page_rank(g)