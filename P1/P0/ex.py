"""
r.txt is init file

Non-anonymized dataset:  edge.txt
Mapping:  mapping.txt
Anonymized dataset:  edge_id.txt


"""


class DirectedUnweightedGraph:
    def __init__(self):
        self.dc = dict()
        self.n = 0
        self.m = 0

    def add_node(self, u):
        pass

    def get_node_id(self, u):

        pass

    def add_edge(self, u, v):

        pass

    def clear(self):
        self.dc = dict()
        self.n = 0
        self.m = 0


def tran2file_1():
    fname1 = "r.txt"
    fname2 = 'edge.txt'
    f = open(fname1)
    fout = open(fname2, 'w')
    for line in f.readlines():
        fout.write(','.join(line.strip().split(' '))+"\n")
    f.close()
    fout.close()


def anonymize():
    dc = dict()

    def add_node(u):
        if u not in dc:
            dc[u] = len(dc) + 1
        return dc[u]

    fin = open('edge.txt', 'r')
    fout = open('edge_id.txt', 'w')

    for line in fin.readlines():
        n1, n2 = line.strip().split(',')
        fout.write("%d,%d\n" % (add_node(n1), add_node(n2)))
    fin.close()
    fout.close()
    fmap = open('mapping.txt', 'w')
    dc1 = dict()
    for name,id in dc.items():
        dc1[id] = name

    for i in range(len(dc1)):
        fmap.write('%s,%d\n' % (dc1[i+1], i+1))

    fmap.close()








if __name__ == "__main__":
    # tran2file_1()
    # anonymize()
    pass