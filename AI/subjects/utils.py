import random
import networkx as nx
import matplotlib.pyplot as plt
import time
from collections import defaultdict

def readdimacs(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    G = nx.Graph()
    for line in lines:
        if line[0] == "e":
            vs = [int(s) for s in line.split() if s.isdigit()]
            G.add_edge(vs[0]-1, vs[1]-1)
    return G

def initial_greedy_coloring(G, k):
    nodes = list(G.nodes())
    random.shuffle(nodes)  # náhodně přeházíme pořadí vrcholů
    coloring = {}

    for node in nodes:
        # získáme barvy sousedů
        neighbor_colors = {coloring.get(neighbor) for neighbor in G.neighbors(node) if neighbor in coloring}

        # vybereme nejnižší volnou barvu
        for color in range(k):
            if color not in neighbor_colors:
                coloring[node] = color
                break
        else:
            # pokud jsou všechny barvy použity, vybereme náhodnou barvu
            coloring[node] = random.randint(0, k-1)

    return coloring


def compute_conflicts(G, coloring):
    node_conflicts = defaultdict(int)
    total_conflicts = 0

    for u, v in G.edges():
        if coloring[u] == coloring[v]:
            node_conflicts[u] += 1
            node_conflicts[v] += 1
            total_conflicts += 1

    return node_conflicts, total_conflicts
