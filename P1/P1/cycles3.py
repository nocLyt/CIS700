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


def buid_nx_graph(fname):
    f = open(fname)
    ug = nx.Graph()
    for line in f.readlines():
        u, v = map(int, line.strip().split(','))
        ug.add_edge(u, v)
    f.close()
    return ug

def build_new_graph(g0):
    ret = nx.Graph()
    for u, v in g0.edges():
        if (g0.degree(u) >= 2 and g0.degree(v) >= 2):
            ret.add_edge(u, v)
    return ret

def cal_3_cycles(g1):
    result = 0
    cnt = 0
    for x in g1.nodes():
        cnt += 1
        print cnt
        for y in g1.neighbors(x):
            for z in g1.neighbors(y):
                if g1.has_edge(x, z):
                    result += 1
    return result



def test():
    g = nx.Graph([(1, 2), (2, 1), (1, 2), (2, 1)])
    print g.degree([1, 2])
    print g.number_of_edges()
    print g.edges()


if __name__ == '__main__':
    g0 = buid_nx_graph(FNAME1)
    print g0.number_of_nodes(), g0.number_of_edges()  # 786,559  831,700

    g1 = build_new_graph(g0)
    print g1.number_of_nodes(), g1.number_of_edges()  # 786,559  831,700
    # print "The number of 3-cycles is ", cal_3_cycles(g1)
    # g1 = nx.Graph([(1,2), (2,3), (3, 1)])
    print "The number of 3-cycles is ", sum(nx.triangles(g1).values())/3

    # data v1 :
    # 979502
    # 5877012

